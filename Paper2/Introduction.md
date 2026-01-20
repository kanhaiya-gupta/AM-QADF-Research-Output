# Introduction

## Background

This work was developed within the framework of the LuFo VII (Luftfahrtforschungsprogramm VII) aeronautical research program, focusing on digital quality assessment of additively manufactured metallic aircraft components. While the framework was developed for aerospace applications, the analysis capabilities presented here are general and applicable to all PBF-LB/M processes across industries.

The signal mapping framework presented in Paper 1 transforms heterogeneous point-based data from multiple sources (hatching paths, laser parameters, CT scans, ISPM monitoring) into a unified 3D voxel domain representation. This unified representation enables new analysis capabilities that were not possible with separate data sources. However, transforming data is only the first step—the real value lies in the analysis capabilities that the unified representation enables.

## Problem Statement

While the unified voxel domain provides the foundation for analysis, several challenges remain:

1. **Sensitivity Analysis**: Understanding which process variables (laser power, scan speed, energy density) most influence quality outcomes (temperature, density, defects) requires systematic sensitivity analysis methods. However, existing sensitivity analysis tools are not integrated with manufacturing data warehouses, requiring manual data extraction and preparation.

2. **Virtual Experiments**: Process optimization requires systematic exploration of parameter spaces, but designing effective virtual experiments that leverage historical warehouse data is challenging. Existing experiment design tools do not integrate with data warehouses to use historical parameter ranges and distributions.

3. **Anomaly Detection**: Early detection of process anomalies requires analyzing multiple signals simultaneously in spatial and temporal contexts. However, existing anomaly detection methods typically work with single signals or require complex data preparation.

4. **Multi-Signal Analysis**: The unified voxel domain enables analysis of multiple signals at the same spatial locations, but existing analysis tools do not leverage this capability for correlation analysis, fusion, and quality assessment.

5. **Accessibility**: Advanced analysis methods (sensitivity analysis, virtual experiments) are typically accessible only to researchers with programming expertise, limiting their use in industrial settings.

## Motivation

The analysis framework addresses these challenges by:

1. **Comprehensive Method Integration**: Integrating 12 sensitivity analysis methods, 10 virtual experiment design types, and 8+ anomaly detection methods into a single framework

2. **Warehouse Integration**: Seamless integration with the NoSQL data warehouse, enabling direct querying of process variables and measurement outputs without manual data extraction

3. **Voxel Domain Analysis**: Leveraging the unified voxel domain for spatial-temporal analysis, multi-signal correlation, and quality-based fusion

4. **Accessibility**: Interactive Jupyter notebooks with widget-based interfaces enabling non-programmers to perform advanced analysis

5. **Systematic Approach**: Systematic frameworks for sensitivity analysis, virtual experiment design, and anomaly detection that guide users through the analysis process

## Contributions

This paper presents:

1. **Comprehensive Analysis Framework**: Integration of 12 sensitivity analysis methods, 10 virtual experiment design types, and 8+ anomaly detection methods with the data warehouse

2. **Warehouse Integration Architecture**: Seamless integration between analysis methods and the NoSQL data warehouse, enabling direct querying and analysis

3. **Voxel Domain Analysis Capabilities**: Spatial-temporal analysis, multi-signal correlation, and quality-based fusion in the unified voxel domain

4. **Interactive Analysis Tools**: Seven interactive Jupyter notebooks providing widget-based interfaces for all analysis workflows

5. **Systematic Analysis Frameworks**: Guided workflows for sensitivity analysis, virtual experiment design, and anomaly detection

## Paper Organization

The remainder of this paper is organized as follows: Section 2 (Analysis Capabilities) describes the 12 sensitivity analysis methods, 10 virtual experiment design types, and 8+ anomaly detection methods. Section 3 (Integration with Warehouse) describes how analysis methods integrate with the data warehouse. Section 4 (Case Studies) presents case studies demonstrating the framework's capabilities. Section 5 (Results) presents performance metrics and analysis results. Section 6 (Discussion) discusses advantages, limitations, and future work. Section 7 (Conclusion) summarizes contributions and impact.

