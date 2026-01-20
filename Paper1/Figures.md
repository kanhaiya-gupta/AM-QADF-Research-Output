# Figures

## Required Figures

1. **Figure 1: Signal Mapping Process Overview**
   - **Location**: `notebooks/flowchart_images/overview_flowchart.png`
   - **Description**: Complete flowchart showing the signal mapping process from multi-source data (hatching, laser, CT, ISPM) through the five-step mapping process to unified voxel domain and downstream applications
   - **Purpose**: Illustrates the complete signal mapping pipeline and its role in the data warehouse framework

2. **Figure 2: Detailed Signal Mapping Process**
   - **Location**: `publications/flowchart_images/detailed_signal_mapping_process_enhanced.mmd` (included in Methodology section)
   - **Description**: Comprehensive flowchart showing the complete five-step signal mapping process from multi-source data input (hatching, laser, CT, ISPM) through coordinate transformation, voxel index calculation, interpolation method selection, aggregation, and storage to unified voxel domain output
   - **Purpose**: Provides detailed visual understanding of the signal mapping algorithm flow with all steps, mathematical formulations, and method selection logic

3. **Figure 3: Multi-Source Integration Flow**
   - **Location**: `notebooks/flowchart_images/multi_source_integration_flow.png`
   - **Description**: Flowchart showing how data from different sources (STL, hatching, laser, CT, ISPM) are integrated through the data warehouse and signal mapping into unified voxel domain
   - **Purpose**: Demonstrates multi-source data integration capabilities

4. **Figure 4: Complete System Architecture**
   - **Location**: `notebooks/flowchart_images/complete_system_architecture.png`
   - **Description**: Complete system architecture diagram showing data warehouse layer, signal mapping engine, analysis framework, and visualization tools
   - **Purpose**: Provides overview of entire framework architecture

5. **Figure 5: Signal Mapping Algorithm Flow**
   - **Location**: `notebooks/flowchart_images/signal_mapping_algorithm_flow.png`
   - **Description**: Detailed algorithm flowchart with decision points for interpolation method selection, aggregation, and quality metrics calculation
   - **Purpose**: Shows algorithmic details and decision logic

6. **Figure 6: Multi-Signal Correlation Analysis**
   - **Location**: To be generated from `notebooks/04_Quality_Analytics_Dashboard.ipynb` or `demo/Phase12_Step3_Advanced_Analytics_Demo.ipynb`
   - **Description**: Correlation plot showing relationship between laser power and ISPM temperature signals in same voxel locations
   - **Purpose**: Demonstrates multi-signal correlation analysis enabled by unified voxel domain

7. **Figure 7: Data Fusion Visualization**
   - **Location**: To be generated from `notebooks/05_Fusion_Anomaly_Detection.ipynb` or `demo/Phase12_Step3_Advanced_Analytics_Demo.ipynb`
   - **Description**: 2D slice visualization showing original signals (hatching, laser, CT, ISPM) and fused signal with quality-based weighting
   - **Purpose**: Demonstrates multi-signal fusion capabilities

8. **Figure 8: 3D Voxel Visualization**
   - **Location**: `demo/output/pyvista_voxel_visualization.png` or generated from `notebooks/03_Voxel_Visualizer.ipynb`
   - **Description**: 3D visualization of voxel grid showing multiple signals (e.g., laser power, temperature) with interactive controls
   - **Purpose**: Demonstrates visualization capabilities and multi-signal representation

9. **Figure 9: Spatial-Temporal Analysis**
   - **Location**: To be generated from analysis notebooks
   - **Description**: Layer-by-layer analysis showing how process conditions (e.g., energy density, temperature) vary spatially and temporally across build layers
   - **Purpose**: Demonstrates spatial-temporal analysis capabilities

10. **Figure 10: Quality Metrics Dashboard**
    - **Location**: To be generated from `notebooks/04_Quality_Analytics_Dashboard.ipynb`
    - **Description**: Dashboard showing completeness, SNR, alignment accuracy, and coverage metrics for mapped signals
    - **Purpose**: Demonstrates quality assessment capabilities

## Figure Captions

**Figure 1**: Overview of the signal mapping process showing transformation from heterogeneous multi-source data to unified voxel domain representation.

**Figure 2**: Detailed signal mapping process flowchart showing all five steps from multi-source data input through coordinate transformation, voxel indexing, interpolation method selection, aggregation, and storage to unified voxel domain output.

**Figure 3**: Multi-source integration flow demonstrating how data from different sources are unified through the signal mapping framework.

**Figure 4**: Complete system architecture of the PBF-LB/M data warehouse with signal mapping framework.

**Figure 5**: Signal mapping algorithm flowchart with decision points for method selection and quality assessment.

**Figure 6**: Correlation analysis between laser power and ISPM temperature signals in unified voxel domain, demonstrating multi-signal analysis capabilities.

**Figure 7**: Data fusion visualization showing original signals and quality-weighted fused signal in 2D slice view.

**Figure 8**: 3D interactive visualization of voxel grid with multiple signals, demonstrating visualization and analysis capabilities.

**Figure 9**: Spatial-temporal analysis showing layer-by-layer variation of process conditions across build.

**Figure 10**: Quality metrics dashboard showing completeness, SNR, alignment accuracy, and coverage for signal mapping results.

