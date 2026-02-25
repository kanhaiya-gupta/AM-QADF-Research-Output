# Related Work

## Literature Review

This section reviews related work in three key areas: (1) additive manufacturing data management systems, (2) multi-source data fusion in manufacturing, and (3) voxel-based representations for spatial data integration.

## AM Data Management Systems

Additive manufacturing generates large volumes of heterogeneous data from multiple sources throughout the manufacturing process. Several research efforts have addressed data management challenges in AM.

**Process Data Management:**

Early work on AM data management focused on structured process data. [Author et al., Year] developed a relational database system for storing process parameters and build metadata. However, relational databases struggle with the heterogeneous, semi-structured nature of AM data, particularly for time-series sensor data and large binary files such as CT scans.

**NoSQL Approaches:**

More recent work has explored NoSQL databases for AM data. [Author et al., Year] proposed a document-based storage system using MongoDB for flexible process data storage. [Author et al., Year] used time-series databases for sensor data management. However, these approaches typically focus on single data sources and do not address the challenge of multi-source data integration.

**Data Warehouse Architectures:**

Some researchers have proposed data warehouse architectures for AM. [Author et al., Year] developed a multi-model data warehouse combining relational and NoSQL databases. [Author et al., Year] proposed a cloud-based data warehouse for distributed AM data. However, these systems primarily focus on data storage and retrieval, with limited support for spatial-temporal data integration and analysis.

**Limitations of Existing Systems:**

Existing AM data management systems have several limitations:
- **Single-Source Focus**: Most systems handle one data source (e.g., process parameters or sensor data) but not multiple sources simultaneously
- **Limited Spatial Integration**: Few systems address coordinate system alignment and spatial data integration
- **Temporal Alignment**: Limited support for aligning data from different temporal resolutions
- **Analysis Capabilities**: Focus on storage rather than enabling advanced analysis through unified representations

Our work addresses these limitations by providing a comprehensive framework for multi-source data integration with signal mapping to a unified voxel domain.

## Multi-Source Data Fusion

Multi-source data fusion is a well-established field in manufacturing and quality control, with applications in process monitoring, defect detection, and quality assessment.

**Sensor Fusion in Manufacturing:**

Sensor fusion has been extensively studied in manufacturing contexts. [Author et al., Year] reviewed sensor fusion techniques for manufacturing process monitoring. [Author et al., Year] applied Kalman filtering for fusing multiple sensor measurements. However, these approaches typically assume synchronized, aligned sensor data, which is not the case for PBF-LB/M data sources.

**Data Fusion in Additive Manufacturing:**

Several researchers have explored data fusion for AM. [Author et al., Year] fused thermal and optical sensor data for process monitoring. [Author et al., Year] combined process parameters with post-build inspection data. However, these approaches typically fuse data at the feature level rather than creating unified spatial representations.

**Spatial Data Fusion:**

Spatial data fusion has been studied in computer vision and remote sensing. [Author et al., Year] reviewed spatial data fusion techniques. [Author et al., Year] applied voxel-based fusion for multi-modal medical imaging. However, these techniques typically assume pre-aligned data and do not address coordinate system transformation challenges.

**Quality-Based Fusion:**

Quality-weighted fusion has been explored in various contexts. [Author et al., Year] proposed quality-based fusion for sensor networks. [Author et al., Year] applied uncertainty-aware fusion for manufacturing data. Our framework extends these concepts to voxel-based representations with quality metrics per voxel.

**Gap in Literature:**

While data fusion is well-studied, there is limited work on:
- **Multi-Source AM Data Fusion**: Fusing hatching paths, laser parameters, CT scans, and ISPM data
- **Spatial-Temporal Alignment**: Handling different coordinate systems and temporal resolutions
- **Voxel-Based Fusion**: Creating unified voxel representations from point-based data

Our signal mapping framework addresses this gap by providing a systematic approach to multi-source data fusion through voxel domain representation.

## Voxel-Based Representations

Voxel-based representations have been used extensively in computer graphics, medical imaging, and 3D data processing.

**Voxel Grids in 3D Processing:**

Voxel grids are a fundamental data structure in 3D processing. [Author et al., Year] reviewed voxel-based 3D representations. [Author et al., Year] used voxel grids for 3D shape analysis. However, these applications typically focus on geometric data rather than signal data from manufacturing processes.

**Point Cloud to Voxel Conversion:**

Converting point clouds to voxel grids is a common operation. [Author et al., Year] reviewed point cloud voxelization techniques. [Author et al., Year] proposed efficient algorithms for point cloud voxelization. However, these approaches typically focus on geometric voxelization (occupancy) rather than signal mapping (assigning signal values to voxels).

**Multi-Resolution Voxel Grids:**

Multi-resolution and adaptive voxel grids have been studied for efficient representation. [Author et al., Year] proposed octree-based multi-resolution voxel grids. [Author et al., Year] developed adaptive resolution grids based on data density. Our framework extends these concepts to signal mapping with adaptive resolution based on data density and spatial importance.

**Voxel-Based Analysis:**

Voxel-based analysis has been applied in various domains. [Author et al., Year] used voxel grids for material property analysis. [Author et al., Year] applied voxel-based methods for defect detection. However, these applications typically work with single data sources rather than multi-source integration.

**Signal Mapping in Voxel Domain:**

Limited work exists on mapping heterogeneous signals to voxel grids. [Author et al., Year] mapped sensor data to voxel grids for visualization. [Author et al., Year] used voxel grids for multi-modal data fusion. However, these approaches do not address the challenges of:
- **Coordinate System Transformation**: Aligning data from different coordinate systems
- **Temporal Synchronization**: Aligning data from different temporal resolutions
- **Interpolation Methods**: Choosing appropriate interpolation for different signal types
- **Quality Assessment**: Quantifying mapping quality and uncertainty

**Our Contribution:**

Our signal mapping framework provides:
- **Systematic Approach**: Five-step process for signal mapping from point data to voxel grids
- **Multi-Source Integration**: Unified framework for all PBF-LB/M data sources
- **Flexible Interpolation**: Support for multiple interpolation methods with selection criteria
- **Quality Metrics**: Comprehensive quality assessment framework
- **Variable Resolution**: Support for uniform, adaptive, and multi-resolution grids

## Summary and Positioning

While significant work exists in AM data management, multi-source data fusion, and voxel-based representations, there is a gap in comprehensive frameworks that:

1. **Integrate Multiple AM Data Sources**: Handle hatching paths, laser parameters, CT scans, and ISPM data simultaneously
2. **Address Coordinate System Challenges**: Transform and align data from different coordinate systems
3. **Handle Temporal Alignment**: Synchronize data from different temporal resolutions
4. **Provide Unified Representation**: Create voxel-based representations enabling multi-signal analysis
5. **Support Analysis Workflows**: Enable downstream analysis (fusion, quality assessment, anomaly detection)

Our signal mapping framework addresses this gap by providing the first comprehensive approach to multi-source PBF-LB/M data integration through voxel domain representation, with systematic handling of coordinate systems, temporal alignment, and quality assessment.

