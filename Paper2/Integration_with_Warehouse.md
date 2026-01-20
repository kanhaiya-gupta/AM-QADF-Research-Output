# Integration with Warehouse

The analysis framework seamlessly integrates with the NoSQL data warehouse, enabling direct querying of process variables and measurement outputs without manual data extraction. This integration is a key differentiator, as existing analysis tools typically require manual data preparation. This section describes how each analysis capability integrates with the warehouse.

## Architecture Overview

The integration architecture consists of three layers:

1. **Data Warehouse Layer**: MongoDB collections storing process data (hatching, laser, CT, ISPM)
2. **Query Client Layer**: Specialized clients for querying warehouse data (UnifiedQueryClient, VoxelDomainClient)
3. **Analysis Client Layer**: Analysis-specific clients that use query clients to retrieve data (SensitivityAnalysisClient, VirtualExperimentClient, AnomalyDetectionClient)

**Integration Pattern:**

```
Analysis Method → Analysis Client → Query Client → MongoDB Warehouse
     ↓                ↓                  ↓              ↓
  Results      Query Config      Spatial/Temporal    Collections
  Storage      Parameter Selection   Filters         Data
```

## Sensitivity Analysis Integration

Sensitivity analysis requires two types of data: (1) process variables (inputs) such as laser power and scan speed, and (2) measurement outputs (responses) such as temperature and density.

### Process Variable Querying

The `SensitivityAnalysisClient` queries process variables from the warehouse using the `UnifiedQueryClient`:

**Query Process:**
1. **Variable Selection**: User selects process variables (e.g., `['laser_power', 'scan_speed', 'energy_density']`)
2. **Spatial/Temporal Filtering**: Optional filters for spatial region, layer range, or time range
3. **Warehouse Query**: Client queries `laser_parameters` collection with filters
4. **Data Extraction**: Extracts variable values and spatial coordinates
5. **Data Formatting**: Returns DataFrame with columns: `[x, y, z, layer_index, laser_power, scan_speed, energy_density, ...]`

**Example Query:**
```python
process_data = sensitivity_client.query_process_variables(
    model_id="model_123",
    variables=['laser_power', 'scan_speed', 'energy_density'],
    spatial_region=((0, 0, 0), (100, 100, 50)),  # Bounding box
    layer_range=(10, 20)  # Layers 10-20
)
```

### Measurement Output Querying

Measurement outputs are queried from multiple sources:

**Query Process:**
1. **Source Selection**: User selects measurement sources (e.g., `['ispm', 'ct']`) or signal names (e.g., `['temperature', 'density']`)
2. **Multi-Source Query**: Client queries multiple collections (`ispm_monitoring_data`, `ct_scan_data`)
3. **Coordinate Transformation**: Transforms to unified coordinate system
4. **Data Merging**: Merges data from multiple sources
5. **Data Formatting**: Returns DataFrame with measurement values

**Example Query:**
```python
measurement_data = sensitivity_client.query_measurement_data(
    model_id="model_123",
    sources=['ispm', 'ct'],  # Or signal names: ['temperature', 'density']
    spatial_region=((0, 0, 0), (100, 100, 50)),
    layer_range=(10, 20)
)
```

### Sensitivity Analysis Workflow

**Complete Workflow:**
1. **Query Data**: Query process variables and measurement outputs from warehouse
2. **Data Preparation**: Align data spatially and temporally
3. **Surrogate Modeling**: If dataset is large, create surrogate model (Random Forest) for efficient evaluation
4. **Sensitivity Analysis**: Execute selected method (Sobol, Morris, etc.)
5. **Results Storage**: Store sensitivity results in warehouse (`sensitivity_results` collection)
6. **Results Querying**: Enable querying and comparison of sensitivity results

**Voxel Domain Integration:**

For voxel-based sensitivity analysis:
1. **Voxel Grid Creation**: Create or load voxel grid for model
2. **Signal Mapping**: Map process variables and measurements to voxel grid
3. **Voxel-Level Analysis**: Perform sensitivity analysis at voxel level
4. **Spatial Sensitivity Maps**: Generate spatial sensitivity maps showing how sensitivity varies spatially

### Results Storage and Querying

Sensitivity results are stored in the warehouse for:
- **Reproducibility**: Store analysis configuration and results
- **Comparison**: Compare sensitivity across different models or builds
- **Trend Analysis**: Analyze how sensitivity changes over time
- **Historical Analysis**: Query past sensitivity analyses

**Storage Schema:**
```json
{
  "_id": "ObjectId",
  "model_id": "string",
  "method": "sobol",
  "process_variables": ["laser_power", "scan_speed"],
  "measurement_outputs": ["temperature", "density"],
  "sensitivity_indices": {
    "S1_laser_power": 0.45,
    "ST_laser_power": 0.62,
    "S1_scan_speed": 0.28,
    "ST_scan_speed": 0.41
  },
  "confidence_intervals": {...},
  "analysis_config": {...},
  "timestamp": "datetime"
}
```

## Virtual Experiment Integration

Virtual experiments use warehouse data in three ways: (1) parameter range extraction, (2) historical build comparison, and (3) experiment result storage.

### Parameter Range Extraction

Virtual experiments automatically extract parameter ranges from warehouse data:

**Extraction Process:**
1. **Model Selection**: Select model(s) to extract ranges from
2. **Variable Selection**: Select variables to extract (e.g., `['laser_power', 'scan_speed']`)
3. **Warehouse Query**: Query all historical data for selected variables
4. **Range Calculation**: Compute min/max or use percentiles (e.g., 5th-95th percentile)
5. **Range Return**: Return dictionary: `{'laser_power': (min, max), 'scan_speed': (min, max)}`

**Example:**
```python
parameter_ranges = experiment_client.get_parameter_ranges_from_warehouse(
    model_ids=["model_123", "model_456"],  # Use multiple models
    variables=['laser_power', 'scan_speed', 'energy_density']
)
# Returns: {'laser_power': (100.0, 300.0), 'scan_speed': (200.0, 1000.0), ...}
```

**Benefits:**
- **Realistic Ranges**: Uses actual process parameter ranges from historical builds
- **Multi-Model Ranges**: Can combine ranges from multiple models for broader exploration
- **Automatic**: No manual range specification needed
- **Data-Driven**: Ranges reflect actual process capabilities

### Historical Build Comparison

Virtual experiments can compare results with historical warehouse data:

**Comparison Process:**
1. **Experiment Execution**: Execute virtual experiment with design matrix
2. **Historical Query**: Query warehouse for similar historical builds
3. **Matching**: Match experiment conditions with historical builds
4. **Comparison**: Compare experiment results with historical outcomes
5. **Validation**: Validate experiment predictions against real data

**Comparison Metrics:**
- **Parameter Similarity**: How similar are experiment parameters to historical builds?
- **Outcome Comparison**: How do experiment outcomes compare to historical outcomes?
- **Prediction Accuracy**: How well do experiment predictions match reality?

### Experiment Result Storage

Virtual experiment results are stored in the warehouse:

**Storage Schema:**
```json
{
  "_id": "ObjectId",
  "experiment_id": "string",
  "model_id": "string",
  "design_type": "lhs",
  "design_matrix": [[param_values], ...],
  "results": [{"outputs": {...}, "metrics": {...}}, ...],
  "comparison_with_warehouse": {...},
  "timestamp": "datetime"
}
```

**Querying:**
- Query experiments by model, design type, or time range
- Compare experiments across different designs
- Analyze experiment trends over time
- Retrieve experiment results for further analysis

## Anomaly Detection Integration

Anomaly detection integrates with the warehouse in two ways: (1) querying data for detection, and (2) storing detection results.

### Data Querying for Detection

Anomaly detection can work with:
- **Point-Based Data**: Query raw point data from collections
- **Voxel Domain Data**: Query voxel grids created through signal mapping
- **Multi-Signal Data**: Query multiple signals simultaneously for correlation-based detection

**Query Process:**
1. **Data Source Selection**: Select data source(s) for detection
2. **Spatial/Temporal Filtering**: Apply filters for region of interest
3. **Signal Selection**: Select signals to analyze
4. **Data Retrieval**: Query warehouse and retrieve data
5. **Detection**: Apply selected anomaly detection method
6. **Results**: Return anomaly scores and locations

**Voxel Domain Detection:**
- **Spatial Anomalies**: Detect anomalies in spatial patterns using voxel grid structure
- **Multi-Signal Anomalies**: Detect correlation breaks between multiple signals
- **Temporal Anomalies**: Detect anomalies in layer-by-layer patterns

### Anomaly Result Storage

Anomaly detection results are stored for:
- **Historical Analysis**: Track anomalies over time
- **Pattern Analysis**: Identify recurring anomaly patterns
- **Validation**: Compare detection methods
- **Alerting**: Trigger alerts for new anomalies

**Storage Schema:**
```json
{
  "_id": "ObjectId",
  "model_id": "string",
  "detection_method": "isolation_forest",
  "anomaly_locations": [[x, y, z], ...],
  "anomaly_scores": [0.85, 0.92, ...],
  "anomaly_types": ["spatial", "temporal", ...],
  "detection_config": {...},
  "timestamp": "datetime"
}
```

## Multi-Signal Fusion Integration

Multi-signal fusion leverages the unified voxel domain created by signal mapping (Paper 1):

**Fusion Process:**
1. **Voxel Grid Loading**: Load existing voxel grid from warehouse
2. **Signal Selection**: Select signals to fuse (e.g., `['laser_power', 'temperature', 'density']`)
3. **Quality Assessment**: Query quality scores for each signal
4. **Fusion Execution**: Apply selected fusion strategy with quality-based weighting
5. **Fused Signal Storage**: Store fused signal in voxel grid

**Quality Score Querying:**
- Quality scores stored in voxel grid metadata
- Can be queried per signal or per voxel
- Enables quality-based fusion weighting

## Data Flow Architecture

The complete data flow for analysis workflows:

### Sensitivity Analysis Data Flow

```
MongoDB Warehouse
    ↓ (Query)
UnifiedQueryClient
    ↓ (Process Variables + Measurements)
SensitivityAnalysisClient
    ↓ (Data Preparation)
Surrogate Model (if needed)
    ↓ (Model Evaluation)
Sensitivity Analysis Method (Sobol, Morris, etc.)
    ↓ (Results)
MongoDB Warehouse (sensitivity_results collection)
```

### Virtual Experiment Data Flow

```
MongoDB Warehouse
    ↓ (Query Parameter Ranges)
VirtualExperimentClient
    ↓ (Extract Ranges)
Experiment Design (LHS, Factorial, etc.)
    ↓ (Design Matrix)
Simulation/Evaluation
    ↓ (Results)
Comparison with Warehouse Data
    ↓ (Storage)
MongoDB Warehouse (virtual_experiments collection)
```

### Anomaly Detection Data Flow

```
MongoDB Warehouse / Voxel Grid
    ↓ (Query Data)
AnomalyDetectionClient
    ↓ (Data Preparation)
Anomaly Detection Method (Isolation Forest, DBSCAN, etc.)
    ↓ (Anomaly Scores)
Anomaly Localization
    ↓ (Results)
MongoDB Warehouse (anomaly_results collection)
```

## Query Interface Standardization

All analysis clients use standardized query interfaces:

**Spatial Query:**
- Bounding box: `((x_min, y_min, z_min), (x_max, y_max, z_max))`
- Model ID: Filter by specific model
- Component ID: Filter by component within model

**Temporal Query:**
- Layer range: `(start_layer, end_layer)`
- Time range: `(start_time, end_time)`
- Timestamp: Specific time point

**Signal Query:**
- Variable names: `['laser_power', 'scan_speed']`
- Source names: `['ispm', 'ct']`
- Signal types: Enumeration of available signals

## Performance Optimizations

The integration includes several performance optimizations:

1. **Parallel Queries**: Multiple sources queried in parallel
2. **Caching**: Query results cached for repeated access
3. **Lazy Loading**: Large arrays loaded only when needed
4. **Index Usage**: Efficient use of MongoDB indexes
5. **Surrogate Models**: Random Forest surrogate for large datasets in sensitivity analysis
6. **Incremental Processing**: Large datasets processed incrementally

## Benefits of Warehouse Integration

The warehouse integration provides several key benefits:

1. **No Manual Data Extraction**: Direct querying eliminates manual data preparation
2. **Consistent Data**: All analysis uses same data source, ensuring consistency
3. **Reproducibility**: Analysis configurations and results stored for reproducibility
4. **Scalability**: Can analyze data from multiple models/builds simultaneously
5. **Historical Analysis**: Easy comparison with historical data
6. **Real-Time Analysis**: Can perform analysis on latest warehouse data
7. **Multi-Model Analysis**: Compare results across different models or builds

This integration makes the analysis framework practical for industrial use, as users can perform advanced analysis without programming or manual data preparation.

