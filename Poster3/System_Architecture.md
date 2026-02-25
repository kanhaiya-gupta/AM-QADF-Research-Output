# System Architecture

## Data Flow Architecture

```
Multi-Source Data
    ↓
[Data Warehouse]
    ↓
[Signal Mapping Engine]
    ↓
[Unified Voxel Domain]
    ↓
[Analysis & Visualization]
```

## Components

### 1. NoSQL Data Warehouse
- **MongoDB**: Document store for flexible PBF process data
- **GridFS**: Large file storage for CT voxel arrays and voxel grids
- **Collections**: STL models, hatching layers, laser parameters, CT scans, ISPM monitoring

### 2. Signal Mapping Engine
- **Coordinate Transformation**: Automatic alignment of coordinate systems
- **Voxel Grid Generation**: Uniform, adaptive, multi-resolution grids
- **Signal Interpolation**: Nearest neighbor, linear, IDW methods
- **Data Synchronization**: Temporal and spatial alignment

### 3. Query Clients
- **UnifiedQueryClient**: Multi-source queries with automatic transformation
- **VoxelDomainClient**: Voxel grid creation and signal mapping
- **Specialized Clients**: STL, Hatching, Laser, CT, ISPM clients

### 4. Interactive Analysis Framework
- **7 Jupyter Notebooks**: Widget-based interfaces
- **3D Visualization**: PyVista-based voxel visualization
- **Real-Time Analysis**: Interactive parameter adjustment

## Integration

All components seamlessly integrate:
- **Direct Querying**: No manual data extraction
- **Automatic Processing**: Signal mapping happens automatically
- **Real-Time Updates**: Voxel grids update as new data arrives
- **Quality Assessment**: Built-in quality metrics

