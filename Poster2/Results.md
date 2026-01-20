# Results

## Performance Metrics

### Analysis Execution Time

| Analysis Type | Method | Data Size | Time | Throughput |
|---------------|--------|-----------|------|------------|
| **Sensitivity** | Sobol | 250K points | 142 s | 1,760 pts/s |
| **Sensitivity** | Morris | 250K points | 28 s | 8,930 pts/s |
| **Virtual Experiment** | LHS (100) | - | 12 s | 8.3 samples/s |
| **Anomaly Detection** | Isolation Forest | 52K voxels | 8 s | 6,500 vox/s |

### Warehouse Query Performance

| Data Source | Query Type | Points | Query Time | Throughput |
|-------------|------------|--------|------------|------------|
| **Laser Parameters** | Spatial+Temporal | 250K | 2.3 s | 108,700 pts/s |
| **Multi-Source** | Unified Query | 300K | 4.5 s | 66,800 pts/s |

## Sensitivity Analysis Results

### Method Comparison

| Method | Sample Size | Accuracy | Interactions | Time |
|--------|-------------|----------|--------------|------|
| **Sobol** | 2000 | Very High | Yes (S2) | 142 s |
| **Morris** | 120 | Medium | Partial | 28 s |
| **FAST** | 500 | High | Limited | 67 s |

### Key Findings
- **Laser Power**: Most influential (S1=0.42, ST=0.58)
- **Scan Speed**: Significant influence (S1=0.31, ST=0.45)
- **Energy Density**: Critical for density (S1=0.38)

## Virtual Experiment Results

### Design Efficiency

| Design Type | Samples | Coverage | Efficiency | Time |
|-------------|---------|----------|------------|------|
| **LHS** | 100 | High | 1.0 | 12 s |
| **Full Factorial 2³** | 8 | Complete | 1.0 | 3 s |
| **D-Optimal** | 12 | High | 0.98 | 4 s |

### Prediction Accuracy
- **Temperature**: Mean absolute error: 35-55°C (5-8% relative)
- **Density**: Mean absolute error: 0.8-1.5%
- **Overall**: 78% of experiments within ±10% of historical outcomes

## Anomaly Detection Results

### Method Performance

| Method | Precision | Recall | F1-Score | False Positive |
|--------|-----------|--------|----------|----------------|
| **Isolation Forest** | 0.82 | 0.75 | 0.78 | 0.18 |
| **Multi-Signal Correlation** | 0.88 | 0.73 | 0.80 | 0.12 |
| **DBSCAN** | 0.79 | 0.71 | 0.75 | 0.21 |

### Detection Capabilities
- **Early Detection**: 65% of defects detected before build completion
- **Spatial Accuracy**: 78% within 1 voxel (0.5 mm) of CT defects
- **Coverage**: Detected 85% of CT-confirmed defects

## Multi-Signal Fusion Results

| Strategy | Coverage | SNR Improvement | Quality Score |
|----------|----------|-----------------|---------------|
| **Quality-Weighted** | 96% | +22% | 0.89 |
| **Average** | 94% | +15% | 0.82 |
| **Median** | 94% | +18% | 0.85 |

