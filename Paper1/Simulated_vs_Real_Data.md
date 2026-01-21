# Simulated vs. Real Data: Framework Flexibility and Data Updates

## Executive Summary

The AM-QADF framework supports both simulated and real manufacturing data, enabling development and validation before actual builds are completed. The framework includes a Data Generation Workbench (Notebook 23: `23_Data_Generation_Workbench.ipynb`) that generates synthetic data from the same 3D models (STL files) intended for printing, allowing early testing, validation, and demonstration of framework capabilities. When real manufacturing data becomes available, it can seamlessly replace simulated data without requiring changes to the framework or analysis workflows, as both use the same data model and storage structure. Additionally, the framework supports incremental updates and corrections to individual fields within each data source, allowing for precise refinement of data as real measurements become available or as data quality improvements are identified.

## Framework Support for Simulated and Real Data

### The Challenge

In research and development scenarios, real manufacturing data may not be immediately available due to:
- Manufacturing schedules and build planning
- Equipment availability and calibration requirements
- Cost considerations for experimental builds
- Time constraints for framework development

However, framework development, algorithm validation, and user training need to proceed independently of manufacturing schedules.

### The Solution: Data Generation Workbench

The AM-QADF framework includes a comprehensive **Data Generation Workbench** (Notebook 23: `23_Data_Generation_Workbench.ipynb`) that generates realistic synthetic data from STL models, enabling complete framework operation before real data is available.

## Simulated Data Generation via Data Generation Workbench

### Overview

The Data Generation Workbench provides an interactive interface for generating synthetic data that mimics real manufacturing data characteristics:

1. **3D Model Input**: Uses the same STL files intended for printing
2. **Comprehensive Data Generation**: Generates all four data sources:
   - **STL Processing**: Loads and processes STL models, extracting geometry and metadata
   - **Hatching Paths**: Generates layer-by-layer scan paths using pyslm from STL geometry
   - **Laser Parameters**: Simulates realistic laser process parameters (power, speed, energy density)
   - **ISPM Data**: Generates in-situ process monitoring data (temperature, melt pool characteristics, cooling rates)
   - **CT Scan Data**: Creates synthetic CT scan data with density, porosity, and defect information

3. **Interactive Configuration**: The workbench provides interactive widgets to:
   - Configure generation parameters for each data type
   - Preview generated data before committing
   - Select which MongoDB collections to populate
   - Adjust noise levels, coverage, and signal characteristics
   - Set random seeds for reproducibility

4. **Realistic Simulation**: Generated data mimics real data characteristics:
   - Appropriate spatial coverage based on STL geometry
   - Realistic noise levels and signal ranges
   - Expected missing data patterns
   - Configurable random seeds for reproducibility

### Key Features of the Data Generation Workbench

- **User-Friendly Interface**: Interactive widgets for all configuration parameters
- **Preview Capabilities**: Visualize generated data before committing to database
- **MongoDB Integration**: Direct population of MongoDB collections
- **Reproducibility**: Configurable random seeds for consistent results
- **Flexibility**: Generate individual data sources or complete datasets

## Seamless Transition to Real Data

### Same Data Model and Structure

The framework is designed to handle both simulated and real data transparently:

1. **Same Data Model**: Simulated and real data use identical structure and format
2. **Same Storage Schema**: Both stored in MongoDB with the same collections and document structure
3. **Same Processing Pipeline**: All framework modules (signal mapping, fusion, quality assessment) work identically
4. **Transparent Replacement**: Real data can replace simulated data without code changes

### Incremental Data Updates and Field Corrections

A critical feature of the framework is the ability to **update and correct individual fields** within each data source as real data becomes available or as data quality improvements are identified:

#### 1. Field-Level Updates

The framework supports updating specific fields within MongoDB documents without replacing entire documents:

- **Partial Updates**: Update only the fields that have new or corrected data
- **Field-Specific Corrections**: Correct individual signal values, metadata, or parameters
- **Incremental Refinement**: Gradually improve data quality as more accurate measurements become available

**Example Use Cases:**
- Update temperature values in ISPM data when sensor calibration is improved
- Correct coordinate transformations when better alignment data is available
- Refine laser power values when process parameters are recalibrated
- Update CT scan density values when scanner calibration is adjusted

#### 2. Source-Specific Updates

Each data source can be updated independently:

- **Hatching Data**: Update scan paths, power settings, or layer information
- **Laser Parameters**: Correct power, speed, or energy density values
- **ISPM Data**: Update temperature measurements, melt pool characteristics, or sensor positions
- **CT Scan Data**: Refine density values, porosity measurements, or defect locations

#### 3. Metadata Updates

Framework metadata can also be updated:

- **Quality Scores**: Update quality assessment results when new assessments are performed
- **Alignment Parameters**: Correct coordinate transformation parameters
- **Processing History**: Update provenance information as data is refined

#### 4. Update Workflow

The framework supports multiple update strategies:

1. **Complete Replacement**: Replace entire data source when comprehensive real data is available
2. **Incremental Updates**: Update specific fields as corrections are identified
3. **Versioned Updates**: Maintain version history of data updates
4. **Selective Updates**: Update only specific regions or time periods

### Benefits of Field-Level Updates

1. **Precision**: Correct only the fields that need updating, preserving other data
2. **Efficiency**: Avoid regenerating or reprocessing entire datasets
3. **Traceability**: Track which fields were updated and when
4. **Flexibility**: Support gradual data refinement as measurements improve
5. **Quality Improvement**: Incrementally improve data quality without full replacement

## Real-World Workflow

### Phase 1: Development with Simulated Data

1. **Load STL Model**: Load STL file intended for printing into Data Generation Workbench
2. **Configure Parameters**: Set generation parameters via interactive widgets
3. **Generate Data**: Generate simulated data for all sources (hatching, laser, ISPM, CT)
4. **Populate MongoDB**: Store generated data in MongoDB collections
5. **Process Through Framework**: Run complete workflow (voxelization → mapping → fusion → quality assessment)
6. **Validate Algorithms**: Test and validate framework algorithms with simulated data
7. **Refine Framework**: Improve framework based on simulated data results

### Phase 2: Transition to Real Data

1. **Complete Manufacturing Build**: Execute actual build using the same STL model
2. **Collect Real Data**: Gather data from all sources (hatching, laser, ISPM, CT)
3. **Store Real Data**: Store in MongoDB (same collections, same structure)
4. **Replace Simulated Data**: Replace simulated data with real data (transparent to framework)
5. **Re-run Analysis**: Execute analysis workflows (no code changes needed)
6. **Compare Results**: Validate framework by comparing simulated vs. real data results

### Phase 3: Incremental Data Refinement

1. **Identify Corrections**: Identify fields that need correction or refinement
2. **Update Specific Fields**: Update only the fields requiring correction
3. **Re-process Affected Workflows**: Re-run only the workflows affected by updates
4. **Validate Updates**: Verify that updates improve data quality
5. **Iterate**: Continue refining data as more accurate measurements become available

**Example Scenario:**
- Initial: Simulated ISPM temperature data with base_temperature = 2000°C
- Update 1: Replace with real ISPM data, but some sensor readings need calibration
- Update 2: Correct temperature values in layers 50-60 where sensor calibration was improved
- Update 3: Refine melt pool width measurements when better analysis methods become available
- Result: Gradually improved data quality without replacing entire dataset

## Technical Implementation

### Data Generation Module

The framework's data generation module (`generation/`) provides:

- **STL Processing**: `generation/process/stl_processor.py` - Processes STL files
- **Hatching Generation**: `generation/process/hatching_generator.py` - Generates scan paths using pyslm
- **Laser Parameters**: `generation/sensors/laser_parameter_generator.py` - Simulates laser parameters
- **ISPM Generation**: `generation/sensors/ispm_generator.py` - Generates ISPM sensor data
- **CT Scan Generation**: `generation/sensors/ct_scan_generator.py` - Creates synthetic CT data

### MongoDB Update Capabilities

The framework's MongoDB integration supports:

- **Document Updates**: Update entire documents or specific fields
- **Query-Based Updates**: Update documents matching specific criteria
- **Bulk Updates**: Efficiently update multiple documents
- **Version Tracking**: Maintain update history and provenance

### Framework Processing

All framework modules work identically with simulated and real data:

- **Query Clients**: Same query interface for both data types
- **Signal Mapping**: Same mapping algorithms and parameters
- **Fusion**: Same fusion strategies and quality assessment
- **Analysis**: Same analysis workflows and methods

## Benefits of This Approach

### For Development

1. **Early Development**: Framework development can proceed before manufacturing runs
2. **Algorithm Validation**: Algorithms can be tested and validated with simulated data
3. **User Training**: Users can learn the framework with simulated data
4. **Reproducibility**: Simulated data provides controlled, reproducible test cases

### For Production

1. **Smooth Transition**: Real data integration is seamless when available
2. **Incremental Refinement**: Data can be gradually improved as measurements are refined
3. **Quality Improvement**: Field-level updates enable precise data quality improvements
4. **Risk Mitigation**: Framework can be tested before committing to expensive manufacturing runs

### For Research

1. **Controlled Experiments**: Simulated data enables controlled experimental conditions
2. **Method Comparison**: Compare algorithms on identical simulated datasets
3. **Sensitivity Analysis**: Test framework sensitivity to different data characteristics
4. **Validation**: Validate framework by comparing simulated vs. real data results

## Summary

The AM-QADF framework's support for both simulated and real data, combined with field-level update capabilities, provides:

- ✅ **Early Development**: Framework development independent of manufacturing schedules
- ✅ **Seamless Transition**: Real data replaces simulated data without code changes
- ✅ **Incremental Refinement**: Update and correct individual fields as data improves
- ✅ **Quality Improvement**: Gradually improve data quality through field-level updates
- ✅ **Flexibility**: Support both complete replacement and incremental updates
- ✅ **Traceability**: Track data updates and maintain version history

This approach enables framework development and validation to proceed independently of manufacturing schedules, while ensuring a smooth transition and continuous improvement when real data becomes available. The framework's architecture ensures that the transition from simulated to real data, and subsequent data refinements, are transparent and require no modifications to the codebase.
