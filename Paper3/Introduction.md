# Introduction

## Problem Statement

This work was developed within the framework of the LuFo VII (Luftfahrtforschungsprogramm VII) aeronautical research program, focusing on digital quality assessment of additively manufactured metallic aircraft components. While the framework was developed for aerospace applications, the signal mapping approach presented here is general and applicable to all PBF-LB/M processes across industries.

Powder Bed Fusion - Laser Beam/Metal (PBF-LB/M) additive manufacturing is a complex process that generates massive, heterogeneous datasets from multiple sources throughout the build cycle. These data sources include:

1. **Hatching Paths**: Hundreds of thousands of scan path points extracted from build files (.mtt, .sli, .cli formats), containing point coordinates (x, y, z) and path information with laser parameters (power, speed, energy density, exposure time, beam width), path geometry parameters (hatch spacing, overlap percentage, contour offset), layer parameters (layer thickness), scan strategy parameters (hatch angle, pattern type such as raster/stripe/chessboard/island, scan direction), and build environment parameters (preheat temperature, atmosphere conditions). Scan strategy significantly affects residual stress distribution, part distortion, mechanical properties, and build quality. Each path segment includes a `data_index` that enables direct one-to-one mapping to the corresponding laser parameter measurement that was used to execute that specific segment. The framework supports a comprehensive catalog of signals (see Methodology section for complete list).

2. **Laser Parameters**: Real-time process measurements including laser power, scan speed, energy density, exposure time, beam width, and region-specific settings (contour, hatch, support). Each measurement includes a `data_index` that maps to the corresponding hatching path segment that was executed using those laser parameters, enabling direct comparison between planned and actual process parameters. The framework can handle derived parameters such as volumetric energy density and power density.

3. **CT Scans**: Post-build computed tomography data providing 3D density information (density values, Hounsfield units), porosity maps, defect information (defect maps, defect locations, defect types), and derived geometric properties (wall thickness, surface roughness) with millions of voxels, typically stored as large voxel arrays.

4. **ISPM Monitoring**: In-situ process monitoring data including thermal signals (melt pool temperature, peak temperature, cooling rate, temperature gradient, solidification rate), melt pool characteristics (temperature, size, geometry, position, velocity), process events, and sensor metadata. The framework supports comprehensive thermal analysis including thermal history and derived metrics such as heat input rate and thermal cycles.

Each data source presents unique challenges:

- **Different Coordinate Systems**: Build platform coordinates (hatching, laser), CT scanner coordinates, and ISPM sensor coordinates require transformation to a unified reference frame.

- **Different Temporal Resolutions**: Real-time measurements (laser, ISPM), layer-based data (hatching), and post-build data (CT scans) operate on different time scales.

- **Different Spatial Resolutions**: Point-based data (hatching paths, laser parameters), voxel-based data (CT scans), and sensor-based measurements (ISPM) have varying spatial densities.

- **Different Data Formats**: Structured data (laser parameters), unstructured point clouds (hatching paths), large arrays (CT voxel data), and time-series data (ISPM monitoring).

**The Core Challenge**: How to create a **unified, queryable, analyzable representation** that enables:
- Multi-source data fusion across different coordinate systems and temporal scales
- Spatial-temporal analysis combining point-based and voxel-based data
- Quality assessment and anomaly detection across all data sources
- Sensitivity analysis and virtual experiments using integrated data
- Statistical process control and digital processing

## Motivation

The integration of multi-source PBF-LB/M data is critical for several reasons:

### 1. Process Understanding and Optimization

Understanding the relationship between process parameters (laser power, speed, energy density), process monitoring (ISPM temperature, melt pool characteristics), and final part quality (CT defects, porosity) requires unified analysis across all data sources. Without integration, correlations between process conditions and quality outcomes remain hidden.

### 2. Quality Control and Anomaly Detection

Early detection of process anomalies requires real-time analysis of multiple signals simultaneously. For example, detecting lack of fusion defects requires correlating hatching path parameters (overlap percentage, hatch spacing, layer thickness, scan strategy), laser energy density, and ISPM temperature measurements. Scan strategy parameters (hatch angle, pattern type) are critical for understanding residual stress distribution and part distortion, which can lead to defects. The `data_index` mapping enables direct one-to-one correspondence between planned parameters (from hatching paths) and measured parameters (from laser sensors) that executed those paths, facilitating comprehensive anomaly detection by comparing planned vs. actual execution. A unified representation enables simultaneous analysis of all signals.

### 3. Data Volume Reduction

Point clouds with hundreds of thousands of coordinates are computationally expensive to analyze. Converting to structured voxel grids reduces data volume while preserving spatial relationships, enabling efficient analysis and storage.

### 4. Spatial-Temporal Analysis

Understanding how process conditions vary spatially (across the build platform) and temporally (across layers) requires a unified spatial-temporal representation. Voxel grids provide a natural structure for such analysis.

### 5. Virtual Experiments and Sensitivity Analysis

Designing virtual experiments and performing sensitivity analysis requires a unified data representation where process parameters can be systematically varied and their effects on quality outcomes analyzed. A voxel domain enables such systematic analysis.

### 6. Digital Twin and Process Control

Building digital twins and implementing statistical process control requires integrated data from all sources. A unified representation provides the foundation for such applications.

**Signal Mapping as the Solution**: Signal mapping transforms heterogeneous point-based data into a unified 3D voxel domain representation, addressing all the challenges above. **Critical to the framework's utility is calibration and correction**, which ensures that systematic errors, geometric distortions, and sensor biases are removed before analysis. Without proper calibration and correction, mapped signals would contain systematic errors that would propagate through all downstream analysis, rendering results unreliable. The framework provides comprehensive calibration and correction capabilities that can be applied flexibly at different stages (typically pre-mapping, with optional corrections at post-mapping, pre-fusion, or post-fusion stages as needed) depending on where errors are detected. By converting all data sources to a common voxel grid structure with proper calibration, signal mapping enables:
- Coordinate system unification through transformation and calibration
- Temporal-spatial alignment through synchronization
- Data volume reduction through structured representation
- Multi-signal integration in a single structure with corrected, accurate signals
- Efficient querying and analysis of calibrated, corrected data

This paper presents the first comprehensive framework for signal mapping in PBF-LB/M additive manufacturing, providing algorithms, implementation, and validation through case studies.

