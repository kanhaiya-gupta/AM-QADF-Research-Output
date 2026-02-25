# Figures

## Required Figures

1. **Figure 1: Analysis Framework Architecture**
   - **Location**: To be generated from system architecture documentation
   - **Description**: Complete architecture diagram showing data warehouse, query clients, analysis clients, and interactive notebooks
   - **Purpose**: Illustrates the integration between warehouse and analysis methods

2. **Figure 2: Sensitivity Analysis Workflow**
   - **Location**: To be generated from `notebooks/06_Advanced_Analysis.ipynb` or `demo/Phase13_Sensitivity_Analysis_Demo.ipynb`
   - **Description**: Flowchart showing sensitivity analysis workflow from warehouse querying to results visualization
   - **Purpose**: Demonstrates systematic sensitivity analysis process

3. **Figure 3: Sobol Sensitivity Indices**
   - **Location**: To be generated from sensitivity analysis notebooks
   - **Description**: Bar plot showing first-order (S1) and total-order (ST) Sobol indices for process variables
   - **Purpose**: Visualizes sensitivity analysis results, showing relative importance of variables

4. **Figure 4: Virtual Experiment Design Matrix**
   - **Location**: To be generated from virtual experiment notebooks
   - **Description**: 3D scatter plot or parallel coordinates plot showing LHS design matrix in parameter space
   - **Purpose**: Demonstrates space-filling property of LHS design

5. **Figure 5: Virtual Experiment Results Comparison**
   - **Location**: To be generated from virtual experiment notebooks
   - **Description**: Scatter plot comparing virtual experiment predictions with historical warehouse data
   - **Purpose**: Validates virtual experiment accuracy

6. **Figure 6: Anomaly Detection Results - Spatial Distribution**
   - **Location**: To be generated from `notebooks/05_Fusion_Anomaly_Detection.ipynb` or `demo/Phase13_Anomaly_Detection_Demo.ipynb`
   - **Description**: 3D visualization showing spatial distribution of detected anomalies in voxel domain
   - **Purpose**: Demonstrates spatial localization of anomalies

7. **Figure 7: Anomaly Detection Method Comparison**
   - **Location**: To be generated from anomaly detection analysis
   - **Description**: ROC curves or precision-recall curves comparing different anomaly detection methods
   - **Purpose**: Compares method performance

8. **Figure 8: Multi-Signal Fusion Visualization**
   - **Location**: To be generated from fusion notebooks
   - **Description**: 2D slice visualization showing original signals and quality-weighted fused signal
   - **Purpose**: Demonstrates multi-signal fusion capabilities

9. **Figure 9: Interactive Notebook Interface**
   - **Location**: Screenshot from `notebooks/06_Advanced_Analysis.ipynb`
   - **Description**: Screenshot showing widget-based interface for sensitivity analysis
   - **Purpose**: Demonstrates user-friendly interface for non-programmers

10. **Figure 10: Warehouse Integration Data Flow**
    - **Location**: To be generated from architecture documentation
    - **Description**: Data flow diagram showing how analysis methods query warehouse and store results
    - **Purpose**: Illustrates warehouse integration architecture

## Figure Captions

**Figure 1**: Analysis framework architecture showing integration between NoSQL data warehouse, query clients, analysis clients, and interactive notebooks.

**Figure 2**: Sensitivity analysis workflow from warehouse data querying through analysis execution to results storage and visualization.

**Figure 3**: Sobol sensitivity indices (first-order S1 and total-order ST) for process variables, showing relative influence on temperature output.

**Figure 4**: Latin Hypercube Sampling design matrix showing space-filling coverage of 3D parameter space (laser power, scan speed, energy density).

**Figure 5**: Comparison of virtual experiment predictions with historical warehouse data, demonstrating prediction accuracy.

**Figure 6**: Spatial distribution of detected anomalies in voxel domain, showing precise spatial localization enabled by unified representation.

**Figure 7**: Performance comparison of anomaly detection methods using ROC curves, showing Isolation Forest and Multi-Signal Correlation achieve best performance.

**Figure 8**: Multi-signal fusion visualization showing original signals (hatching, laser, CT, ISPM) and quality-weighted fused signal in 2D slice view.

**Figure 9**: Interactive Jupyter notebook interface with widget-based controls for sensitivity analysis, demonstrating accessibility for non-programmers.

**Figure 10**: Data flow architecture for warehouse integration, showing query processes, analysis execution, and results storage.

