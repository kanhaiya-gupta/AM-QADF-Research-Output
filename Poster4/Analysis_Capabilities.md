# Analysis Capabilities

## 1. Sensitivity Analysis (12 Methods)

### Global Methods
- **Sobol**: First-order (S1), Total (ST), Second-order (S2) indices
- **Morris**: Elementary effects screening (μ*, σ)
- **FAST**: Fourier Amplitude Sensitivity Test
- **RBD**: Random Balance Design
- **Delta**: Moment-independent sensitivity
- **PAWN**: Distribution-based sensitivity
- **DGSM**: Derivative-based Global Sensitivity Measure

### Local Methods
- **Local Derivatives**: Gradient-based local sensitivity
- **Local Perturbation**: Parameter perturbation analysis
- **Local Central Differences**: Central finite differences

### Uncertainty Methods
- **Monte Carlo**: Sampling-based sensitivity
- **Bayesian**: Probabilistic sensitivity analysis

**Best For**: Identifying key process variables influencing quality outcomes

## 2. Virtual Experiments (10 Design Types)

### Basic Designs
- **LHS**: Latin Hypercube Sampling (space-filling)
- **Random Sampling**: Simple random sampling
- **Parameter Sweep**: Systematic parameter variation

### Factorial Designs
- **Full Factorial (2^k)**: Complete 2-level factorial
- **Full Factorial (3^k)**: Complete 3-level factorial

### Response Surface Designs
- **Central Composite (CCD)**: Factorial + axial + center points
- **Box-Behnken (BBD)**: Efficient response surface design

### Optimal Designs
- **D-Optimal**: Maximizes determinant of information matrix
- **A-Optimal**: Minimizes trace of inverse information matrix
- **G-Optimal**: Minimizes maximum prediction variance

**Best For**: Systematic parameter space exploration and optimization

## 3. Anomaly Detection (18 Methods)

### Statistical Methods (5)
- **Z-Score**: Standard deviation-based detection
- **IQR**: Interquartile range detection
- **Mahalanobis Distance**: Multivariate detection
- **Modified Z-Score**: Robust median-based detection
- **Grubbs' Test**: Statistical outlier test

### Clustering Methods (5)
- **DBSCAN**: Density-based spatial clustering
- **Isolation Forest**: Tree-based isolation
- **LOF**: Local Outlier Factor
- **One-Class SVM**: Support vector novelty detection
- **K-Means**: Cluster-based detection

### Machine Learning Methods (3)
- **Autoencoder**: Reconstruction error-based
- **LSTM Autoencoder**: Temporal anomaly detection
- **VAE**: Variational autoencoder

### Rule-Based Methods (5)
- **Threshold Violation**: Process bounds checking
- **Pattern Deviation**: Statistical process control
- **Temporal Pattern**: Time-series anomaly detection
- **Spatial Pattern**: Voxel-based spatial detection
- **Multi-Signal Correlation**: Correlation break detection

**Best For**: Early detection of process issues and quality problems

## 4. Multi-Signal Fusion

- **Quality-Based Weighting**: Automatic weight calculation
- **Fusion Strategies**: Average, weighted average, median, quality-based
- **Coverage Improvement**: 96% coverage with fusion (vs. 60-75% individual)
- **SNR Improvement**: 15-25% improvement over simple averaging

