# System Architecture

The signal mapping framework is built on a NoSQL data warehouse architecture that provides flexible storage and efficient querying of multi-source PBF-LB/M data. This section describes the data warehouse layer, query clients, and their integration with the signal mapping engine.

## Data Warehouse

The data warehouse uses MongoDB as the primary storage system, providing document-based storage for flexible PBF process data and GridFS for large binary files such as CT scan voxel arrays and voxel grids.

### MongoDB Document Store

MongoDB serves as the document store for structured and semi-structured PBF-LB/M data. The database is organized into collections that correspond to different data sources:

**Collection Structure:**

1. **`stl_models`**: STL model metadata and geometric properties
   - Model ID, filename, file path
   - Bounding box, volume, surface area, complexity metrics
   - Coordinate system information
   - Tags and metadata

2. **`hatching_layers`**: Hatching path data organized by layer
   - Model ID, layer index, layer height, z-position
   - Contours: point arrays with scan order
   - Hatches: full laser path coordinates, laser parameters (power, speed, energy density, beam width, hatch spacing, overlap percentage)
   - Support structures
   - Processing timestamps

3. **`laser_parameters`**: Laser parameter measurements
   - Model ID, layer index, point ID
   - Spatial coordinates (x, y, z)
   - Laser power, scan speed, hatch spacing
   - Energy density, exposure time
   - Timestamp, region type (contour, hatch, support)

4. **`ct_scan_data`**: CT scan information and references
   - Model ID, scan ID, scan timestamp
   - Voxel grid metadata (dimensions, spacing, origin)
   - GridFS references for large voxel arrays
   - Density values, porosity maps
   - Defect locations and metadata

5. **`ispm_monitoring_data`**: In-situ process monitoring data
   - Model ID, layer index, timestamp
   - Melt pool data (temperature, size, geometry, position)
   - Thermal data (peak temperature, cooling rate, temperature gradient)
   - Process events and sensor metadata

**Indexing Strategy:**

Collections are indexed for efficient querying:
- **Spatial queries**: Indexes on `model_id`, `layer_index`, `z_position`, `spatial_coordinates`
- **Temporal queries**: Indexes on `timestamp`, `layer_index`, `scan_timestamp`
- **Signal queries**: Indexes on signal-specific fields (e.g., `laser_power`, `temperature`)
- **Composite indexes**: Multi-field indexes for common query patterns (e.g., `model_id + layer_index`)

### GridFS for Large Files

GridFS is used for storing large binary data that exceeds MongoDB's 16MB document size limit:

**Use Cases:**
- **CT Scan Voxel Arrays**: Large 3D voxel arrays from CT scans (millions of voxels)
- **Voxel Grids**: Complete voxel grids with signal data (can be >100MB for high-resolution grids)
- **STL Files**: Original STL model files
- **Large Signal Arrays**: Dense signal arrays from high-resolution mappings

**Storage Architecture:**
- GridFS splits large files into chunks (default: 255KB chunks)
- Metadata stored in `fs.files` collection
- Chunks stored in `fs.chunks` collection
- Enables efficient streaming and partial retrieval
- Supports versioning and metadata attachment

**Voxel Grid Storage:**
- Grid metadata (resolution, bounding box, dimensions) stored in `voxel_grids` collection
- Signal arrays stored in GridFS with references in metadata
- Sparse voxel representation compressed and stored in GridFS
- Enables efficient loading of voxel grids without loading entire arrays

## Query Clients

The framework provides specialized query clients for each data source, enabling efficient retrieval with spatial, temporal, and signal-type filters.

### Multi-Source Query Clients

Each data source has a dedicated query client that implements a standardized interface:

**1. STLModelClient**
- Queries STL model metadata and geometric properties
- Retrieves bounding boxes and coordinate system information
- Supports model filtering by tags and metadata

**2. HatchingClient**
- Queries hatching path data with spatial and temporal filters
- Retrieves full laser path coordinates and associated parameters
- Supports layer-based and spatial bounding box queries
- Returns point arrays with signal values (laser power, speed, energy density)

**3. LaserParameterClient**
- Queries laser parameter measurements
- Supports spatial queries (bounding box, region type)
- Supports temporal queries (timestamp, layer range)
- Returns point data with laser parameter values

**4. CTScanClient**
- Queries CT scan data and defect locations
- Retrieves voxel grid metadata and GridFS references
- Supports spatial queries for defect locations
- Handles large voxel array retrieval from GridFS

**5. InSituMonitoringClient**
- Queries ISPM monitoring data
- Supports temporal queries (timestamp, layer index)
- Supports spatial queries (melt pool position)
- Returns temperature and thermal data

**Base Query Interface:**

All query clients inherit from `BaseQueryClient` and implement:
- `query(spatial, temporal, signal_types)`: Execute queries with filters
- `get_available_signals()`: List available signal types
- `get_bounding_box(component_id)`: Get spatial bounds
- `get_temporal_range(component_id)`: Get temporal bounds

**Query Types:**

- **SpatialQuery**: Bounding box, component ID, layer range
- **TemporalQuery**: Time range, layer range, timestamp filters
- **SignalType**: Enumeration of available signal types per source

### Unified Query Interface

The `UnifiedQueryClient` provides a single interface for querying multiple data sources simultaneously:

**Features:**
- **Multi-Source Queries**: Query all sources with single call
- **Coordinate System Transformation**: Automatic transformation to unified coordinate system
- **Data Merging**: Merge results from multiple sources
- **Consistent Interface**: Same query interface for all sources

**Query Workflow:**

1. **Query Execution**: Execute queries on all requested sources in parallel
2. **Coordinate Transformation**: Transform all results to common coordinate system (build platform)
3. **Temporal Alignment**: Align temporal data using layer mapping
4. **Result Merging**: Combine results into unified structure
5. **Return**: Return merged `QueryResult` with points, signals, and metadata

**Example Usage:**

```python
# Query all sources for a specific model and layer
result = unified_client.query(
    spatial=SpatialQuery(model_id="model_123", layer_range=(10, 20)),
    temporal=TemporalQuery(layer_range=(10, 20)),
    sources=['hatching', 'laser', 'ct', 'ispm']
)

# Result contains:
# - points: Unified point array (N, 3)
# - signals: Dictionary of signal arrays (N,)
# - metadata: Source information, coordinate systems, quality metrics
```

## Integration with Signal Mapping

The query clients integrate seamlessly with the signal mapping engine:

**Data Flow:**

1. **Query Phase**: Query clients retrieve data from MongoDB with spatial/temporal filters
2. **Transformation Phase**: Coordinate system transformer unifies coordinate systems
3. **Mapping Phase**: Signal mapping engine maps points to voxel grid
4. **Storage Phase**: Voxel grids stored back to MongoDB/GridFS for reuse

**Performance Optimizations:**

- **Parallel Queries**: Multiple sources queried in parallel
- **Lazy Loading**: Large arrays loaded only when needed
- **Caching**: Query results cached for repeated access
- **Index Usage**: Efficient use of MongoDB indexes for fast queries
- **Streaming**: Large data streams processed incrementally

## Interactive Analysis Framework

The framework includes seven interactive Jupyter notebooks that provide user-friendly interfaces for:

1. **System Overview**: Architecture visualization and signal mapping flowcharts
2. **Data Explorer**: Multi-source data browsing and querying
3. **Voxel Domain Builder**: Grid creation and signal mapping configuration
4. **Voxel Visualizer**: 3D visualization of voxel grids with multiple signals
5. **Quality & Analytics Dashboard**: Quality assessment and statistical analysis
6. **Fusion & Anomaly Detection**: Multi-signal fusion and anomaly detection
7. **Advanced Analysis**: Sensitivity analysis and virtual experiments

All notebooks use `ipywidgets` for interactive parameter adjustment and real-time visualization updates, enabling non-programmers to use the framework effectively.

## Scalability and Performance

The architecture is designed for scalability:

- **Horizontal Scaling**: MongoDB supports sharding for large datasets
- **Connection Pooling**: Efficient connection management for concurrent queries
- **GridFS Streaming**: Efficient handling of large files without memory issues
- **Sparse Storage**: Voxel grids use sparse representation to minimize memory
- **Index Optimization**: Strategic indexing for common query patterns

The system has been validated with datasets containing >1 million data points and voxel grids with >10 million voxels, demonstrating scalability for large-scale PBF-LB/M builds.

