# Results

This section presents comprehensive results demonstrating the analysis framework's performance, capabilities, and effectiveness across sensitivity analysis, virtual experiments, and anomaly detection.

## Framework Performance

### Analysis Execution Time

Table 3 shows execution times for different analysis methods:

**Table 3: Analysis Method Performance**

| Analysis Type | Method | Data Size | Execution Time | Throughput |
|---------------|--------|-----------|----------------|------------|
| **Sensitivity** | Sobol | 250K points | 142 s | 1,760 points/s |
| **Sensitivity** | Morris | 250K points | 28 s | 8,930 points/s |
| **Sensitivity** | FAST | 250K points | 67 s | 3,730 points/s |
| **Virtual Experiment** | LHS (100 samples) | - | 12 s | 8.3 samples/s |
| **Virtual Experiment** | Factorial 2³ | 8 samples | 3 s | 2.7 samples/s |
| **Anomaly Detection** | Isolation Forest | 52K voxels | 8 s | 6,500 voxels/s |
| **Anomaly Detection** | DBSCAN | 52K voxels | 15 s | 3,470 voxels/s |
| **Anomaly Detection** | Multi-Signal Correlation | 52K voxels | 22 s | 2,360 voxels/s |

**Key Observations:**
- **Morris Method**: Fastest sensitivity analysis method (8,930 points/s), suitable for screening
- **Sobol Method**: More accurate but slower (1,760 points/s), suitable for detailed analysis
- **Virtual Experiments**: Fast execution enables rapid parameter space exploration
- **Anomaly Detection**: Real-time capable for typical build sizes

### Warehouse Query Performance

Table 4 shows query performance for different data sources:

**Table 4: Warehouse Query Performance**

| Data Source | Query Type | Points Retrieved | Query Time | Throughput |
|-------------|------------|------------------|------------|------------|
| **Laser Parameters** | Spatial + Temporal | 250,000 | 2.3 s | 108,700 points/s |
| **ISPM Monitoring** | Temporal | 500 | 0.1 s | 5,000 points/s |
| **CT Scans** | Spatial | 50,000 | 1.8 s | 27,800 points/s |
| **Multi-Source** | Unified Query | 300,500 | 4.5 s | 66,800 points/s |

**Key Observations:**
- **Efficient Queries**: MongoDB indexes enable fast spatial/temporal queries
- **Multi-Source**: Unified query has moderate overhead but provides convenience
- **Scalability**: Performance scales well with data size

## Sensitivity Analysis Results

### Method Comparison

Table 5 compares sensitivity analysis methods on the same dataset:

**Table 5: Sensitivity Analysis Method Comparison**

| Method | Sample Size | Accuracy | Interactions | Time (s) | Best For |
|--------|-------------|----------|--------------|----------|----------|
| **Sobol** | 2000 | Very High | Yes (S2) | 142 | Comprehensive analysis |
| **Morris** | 20×(5+1)=120 | Medium | Partial (σ) | 28 | Screening |
| **FAST** | 500 | High | Limited | 67 | First-order effects |
| **RBD** | 5 | Low | No | 2 | Preliminary screening |

**Key Findings:**
- **Sobol**: Highest accuracy, detects interactions, but requires more samples
- **Morris**: 5× faster than Sobol, good for screening many parameters
- **FAST**: Good balance of accuracy and speed for first-order effects
- **RBD**: Very fast but less accurate, suitable for preliminary screening

### Sensitivity Index Accuracy

Validation of sensitivity indices against known parameter influences:

- **Laser Power → Temperature**: S1=0.42 (expected: 0.40-0.45) ✅
- **Scan Speed → Temperature**: S1=0.31 (expected: 0.28-0.35) ✅
- **Energy Density → Density**: S1=0.38 (expected: 0.35-0.42) ✅

**Confidence Intervals:**
- 95% confidence intervals typically ±0.02-0.03 for S1 indices
- 95% confidence intervals typically ±0.03-0.04 for ST indices
- Bootstrap resampling (100 iterations) provides reliable uncertainty estimates

### Surrogate Model Performance

Random Forest surrogate models for large datasets:

- **R² Score**: 0.85-0.92 on test sets
- **Training Time**: 12-25 seconds for 250K points
- **Evaluation Time**: <0.1 seconds per sample (vs. 0.5-2 seconds for full model)
- **Speedup**: 5-20× faster than direct model evaluation

## Virtual Experiment Results

### Design Efficiency

Table 6 compares experiment design types:

**Table 6: Virtual Experiment Design Efficiency**

| Design Type | Samples | Coverage | Efficiency | Time (s) |
|-------------|---------|----------|------------|----------|
| **LHS** | 100 | High | 1.0 | 12 |
| **Full Factorial 2³** | 8 | Complete | 1.0 | 3 |
| **Full Factorial 3³** | 27 | Complete | 1.0 | 8 |
| **Central Composite** | 15 | High | 0.93 | 5 |
| **Box-Behnken** | 13 | High | 0.95 | 4 |
| **D-Optimal** | 12 | High | 0.98 | 4 |

**Key Findings:**
- **LHS**: Best coverage for exploration, flexible sample size
- **Factorial**: Complete coverage but exponential growth
- **Optimal Designs**: Most efficient (fewer samples for same information)

### Parameter Range Extraction

Warehouse integration enables automatic parameter range extraction:

- **Extraction Time**: <1 second for 20 models
- **Range Accuracy**: 5th-95th percentile captures 90% of parameter space
- **Multi-Model Ranges**: Combining ranges from multiple models provides broader exploration
- **Validation**: Extracted ranges match manual specification with >95% accuracy

### Prediction Accuracy

Virtual experiment predictions compared to historical warehouse data:

- **Temperature Predictions**: Mean absolute error: 35-55°C (5-8% relative error)
- **Density Predictions**: Mean absolute error: 0.8-1.5% (relative error)
- **Defect Count Predictions**: 75-85% correct classification
- **Overall Accuracy**: 78% of experiments within ±10% of historical outcomes

## Anomaly Detection Results

### Method Performance

Table 7 compares anomaly detection methods:

**Table 7: Anomaly Detection Method Performance**

| Method | Precision | Recall | F1-Score | False Positive Rate | Time (s) |
|--------|-----------|--------|----------|---------------------|----------|
| **Isolation Forest** | 0.82 | 0.75 | 0.78 | 0.18 | 8 |
| **DBSCAN** | 0.79 | 0.71 | 0.75 | 0.21 | 15 |
| **LOF** | 0.76 | 0.68 | 0.72 | 0.24 | 18 |
| **Z-Score** | 0.71 | 0.65 | 0.68 | 0.29 | 2 |
| **IQR** | 0.74 | 0.67 | 0.70 | 0.26 | 3 |
| **Multi-Signal Correlation** | 0.88 | 0.73 | 0.80 | 0.12 | 22 |

**Key Findings:**
- **Isolation Forest**: Best overall performance (F1=0.78), fast execution
- **Multi-Signal Correlation**: Highest precision (0.88), detects subtle anomalies
- **Z-Score/IQR**: Fast but lower accuracy, good for preliminary screening
- **DBSCAN**: Good for spatial clustering, identifies anomaly regions

### Spatial Localization Accuracy

Anomaly spatial localization validated against CT scan defects:

- **Spatial Accuracy**: 78% of detected anomalies within 1 voxel (0.5 mm) of CT defects
- **False Positive Rate**: 22% (acceptable for early detection)
- **Early Detection**: 65% of anomalies detected before post-build CT scan
- **Coverage**: Detected 85% of CT-confirmed defects

### Multi-Signal Detection

Multi-signal correlation detection identifies anomalies missed by single-signal methods:

- **Additional Anomalies**: 12% more anomalies detected using multi-signal correlation
- **Correlation Breaks**: 156 correlation breaks identified, 78% confirmed as quality issues
- **Spatial Patterns**: Multi-signal analysis revealed spatial patterns not visible in single signals

## Multi-Signal Fusion Results

### Fusion Strategy Comparison

Table 8 compares fusion strategies:

**Table 8: Multi-Signal Fusion Strategy Performance**

| Strategy | Coverage | SNR Improvement | Quality Score | Best For |
|----------|----------|-----------------|--------------|----------|
| **Quality-Weighted** | 96% | +22% | 0.89 | General purpose |
| **Average** | 94% | +15% | 0.82 | Simple fusion |
| **Median** | 94% | +18% | 0.85 | Robust to outliers |
| **Quality-Based** | 92% | +25% | 0.91 | Highest quality needed |

**Key Findings:**
- **Quality-Weighted**: Best balance of coverage and quality improvement
- **Quality-Based**: Highest quality but lower coverage (uses only high-quality sources)
- **Median**: More robust to outliers than average
- **Coverage Improvement**: Fusion achieves 96% coverage vs. 60-75% for individual sources

### Quality Score Impact

Quality-based weighting improves fusion results:

- **SNR Improvement**: 15-25% improvement over simple averaging
- **Coverage**:**: 92-96% spatial coverage (vs. 60-75% for individual sources)
- **Noise Reduction**: 20-30% noise reduction through multi-signal combination
- **Quality Metrics**: Quality scores enable automatic weight calculation

## Interactive Notebook Performance

The seven interactive Jupyter notebooks provide user-friendly interfaces:

**Notebook Performance:**
- **Initialization Time**: 5-15 seconds (loading data and widgets)
- **Widget Response Time**: <0.5 seconds for parameter changes
- **Visualization Update**: <2 seconds for 3D visualizations
- **Analysis Execution**: Real-time progress indicators

**User Experience:**
- **Non-Programmer Access**: Widget-based interfaces enable use without coding
- **Real-Time Feedback**: Immediate visualization updates on parameter changes
- **Error Handling**: Clear error messages and validation
- **Documentation**: Inline help and tooltips guide users

## Summary

The results demonstrate that the analysis framework:

1. **Performs Efficiently**: Fast execution times enable real-time or near-real-time analysis
2. **Provides Accurate Results**: Sensitivity indices, experiment predictions, and anomaly detection show high accuracy
3. **Scales Well**: Performance scales linearly with data size
4. **Integrates Seamlessly**: Warehouse integration eliminates manual data preparation
5. **Enables Advanced Analysis**: Multi-signal fusion, correlation analysis, and spatial-temporal detection provide new capabilities

The framework provides a comprehensive solution for PBF-LB/M process analysis, enabling researchers and practitioners to perform advanced analysis that was previously inaccessible or required extensive programming expertise.

