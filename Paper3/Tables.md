# Tables

## Required Tables

### Table 1: Comparison of Signal Interpolation Methods
- **Location**: Methodology section (Interpolation Method Comparison)
- **Content**: Comparison of nearest neighbor, linear, IDW, Gaussian KDE, and RBF interpolation methods
- **Columns**: Method, Status, Complexity, Smoothness, Sparse Data, Uncertainty, Parameters, Best For

### Table 2: Comparison of Voxel Grid Types
- **Location**: Methodology section (Grid Type Comparison)
- **Content**: Comparison of uniform, adaptive, and multi-resolution grid types
- **Columns**: Grid Type, Status, Memory Usage, Query Speed, Resolution Flexibility, Complexity, Best For

### Table 3: Signal Mapping Performance
- **Location**: Results section (Performance Metrics)
- **Content**: Processing time and throughput for different configurations
- **Columns**: Configuration, Points, Resolution (mm), Grid Type, Time (s), Points/sec
- **Data**: Performance metrics for small, medium, large, adaptive, and multi-resolution configurations

### Table 4: Data Volume Reduction
- **Location**: Results section (Data Volume Reduction)
- **Content**: Data volume reduction achieved by signal mapping for each data source
- **Columns**: Data Source, Original Points, Voxel Grid Size, Reduction Ratio, Storage (MB)
- **Data**: Reduction metrics for hatching paths, laser parameters, CT defects, ISPM monitoring, and combined

### Table 5: Data Sources and Characteristics
- **Location**: Introduction or Methodology section
- **Content**: Characteristics of each data source including coordinate systems, temporal resolution, spatial resolution, and data format
- **Columns**: Data Source, Coordinate System, Temporal Resolution, Spatial Resolution, Data Format, Typical Point Count
- **Suggested Content**:
  - Hatching Paths: Build platform, Layer-based, Point-based, Structured, 100K-1M points
  - Laser Parameters: Build platform, Real-time, Point-based, Structured, 10K-100K points
  - CT Scans: CT scanner, Post-build, Voxel-based, Large arrays, 50K-500K defect locations
  - ISPM Monitoring: Sensor coordinates, Real-time, Point-based, Time-series, 100-10K measurements

### Table 6: Quality Metrics Summary
- **Location**: Results section (Quality Assessment Results)
- **Content**: Summary of quality metrics including completeness, alignment accuracy, and signal quality
- **Columns**: Metric, Hatching, Laser, CT, ISPM, Overall
- **Suggested Content**:
  - Spatial Coverage: 85-95%, 70-85%, 40-60%, 15-30%, >90%
  - Alignment Error: <0.5 voxel, <0.5 voxel, <1 voxel, <1 voxel, <1 voxel
  - SNR: >20 dB, >20 dB, 10-25 dB, 15-20 dB, Variable

## Table Captions

**Table 1**: Comparison of signal interpolation methods supported and planned in the framework, including complexity, smoothness, and best use cases.

**Table 2**: Comparison of voxel grid types (uniform, adaptive, multi-resolution) with memory usage, query speed, and flexibility characteristics.

**Table 3**: Signal mapping performance metrics showing processing time and throughput for different data sizes and grid configurations.

**Table 4**: Data volume reduction achieved by signal mapping, showing reduction ratios and storage savings for each data source.

**Table 5**: Characteristics of data sources integrated in the framework, including coordinate systems, temporal/spatial resolutions, and typical data volumes.

**Table 6**: Summary of quality assessment metrics including spatial coverage, alignment accuracy, and signal quality for each data source.

