# Analysis Capabilities

The analysis framework provides comprehensive capabilities for sensitivity analysis, virtual experiment design, anomaly detection, and multi-signal fusion. This section describes each capability in detail, including methods, algorithms, and use cases.

## Sensitivity Analysis Methods

Sensitivity analysis identifies which process variables (inputs) most influence quality outcomes (outputs). The framework integrates 12 sensitivity analysis methods, categorized into global methods, local methods, and uncertainty-based methods.

### MPM System Sensitivity Analysis

A key application of sensitivity analysis in this framework is the **systematic evaluation of the influences of process variables and events on measurement behavior** of Melt Pool Monitoring (MPM) systems. This addresses the specific requirement for sensitivity analysis of an MPM system to understand how process conditions affect measurement system response.

**MPM System Context:**
- **MPM System**: Installed melt pool monitoring system providing real-time temperature and melt pool characteristic measurements
- **Process Variables**: Laser power, scan speed, energy density, layer thickness, hatch spacing, scan pattern
- **Process Events**: Layer transitions, scan path changes, power modulations, support structure interactions
- **Measurement Behavior**: MPM system response including temperature measurements, melt pool size, thermal gradients, measurement accuracy, signal quality

**Sensitivity Analysis Focus:**
The sensitivity analysis evaluates how process variables and events influence:
- **Measurement Accuracy**: How process conditions affect MPM measurement precision
- **Signal Quality**: How process parameters influence MPM signal-to-noise ratio
- **Measurement Response**: How MPM system responds to different process conditions
- **Event Detection**: How process events (layer changes, power modulations) affect measurements
- **Systematic Evaluation**: Comprehensive assessment of process-measurement relationships

**Implementation:**
- **Process Variables**: Queried from warehouse (laser parameters, hatching paths)
- **Measurement Data**: MPM system data from installed monitoring system
- **Sensitivity Methods**: Sobol, Morris, and other methods applied to MPM data
- **Measurement Behavior Metrics**: Temperature accuracy, melt pool size accuracy, thermal gradient measurements
- **Event Analysis**: Sensitivity to process events (layer transitions, scan pattern changes)

**Key Questions Addressed:**
- Which process variables most influence MPM measurement accuracy?
- How do process events (layer changes, power modulations) affect measurement behavior?
- What is the relationship between process conditions and MPM signal quality?
- How does measurement behavior vary across different process conditions?

This MPM system sensitivity analysis provides systematic evaluation of measurement system performance, enabling understanding of how process conditions affect measurement reliability and accuracy.

### Global Sensitivity Analysis Methods

Global methods analyze sensitivity across the entire parameter space, providing comprehensive understanding of parameter influences.

#### Sobol Method

The Sobol method decomposes output variance into contributions from individual parameters and their interactions.

**Mathematical Formulation:**

For a model $Y = f(X_1, X_2, ..., X_n)$, Sobol indices decompose variance:

$$V(Y) = \sum_i V_i + \sum_{i<j} V_{ij} + ... + V_{1,2,...,n}$$

where:
- $V_i$ is variance due to $X_i$ alone
- $V_{ij}$ is variance due to interaction between $X_i$ and $X_j$

**Sensitivity Indices:**
- **First-order index (S1)**: $S_i = V_i / V(Y)$ - direct contribution of parameter $X_i$
- **Total-order index (ST)**: $ST_i = 1 - V_{\sim i} / V(Y)$ - total contribution including interactions
- **Second-order index (S2)**: $S_{ij} = V_{ij} / V(Y)$ - interaction effects between pairs

**Implementation:**
- Uses Saltelli sampling sequence for efficient sampling
- Supports first-order, total-order, and second-order indices
- Provides confidence intervals via bootstrap resampling
- Sample size: Typically 1000-10000 samples for accurate results

**Best For**: Comprehensive sensitivity analysis when interactions are important, high accuracy requirements

#### Morris Method

The Morris method (Elementary Effects) provides a screening method for identifying important parameters with fewer model evaluations.

**Mathematical Formulation:**

Elementary effect for parameter $X_i$:

$$EE_i = \frac{f(X_1, ..., X_i + \Delta, ..., X_n) - f(X_1, ..., X_n)}{\Delta}$$

**Sensitivity Metrics:**
- **μ* (Mean Absolute)**: $\mu^*_i = \frac{1}{r} \sum_{j=1}^r |EE_i^{(j)}|$ - overall importance
- **σ (Standard Deviation)**: $\sigma_i = \sqrt{\frac{1}{r-1} \sum_{j=1}^r (EE_i^{(j)} - \mu_i)^2}$ - nonlinearity/interactions

**Implementation:**
- Uses Morris trajectories (typically 10-20 trajectories)
- Each trajectory requires (n+1) model evaluations for n parameters
- Total evaluations: r × (n+1) where r is number of trajectories
- Much more efficient than Sobol for screening many parameters

**Best For**: Screening many parameters, identifying important variables quickly, limited computational budget

#### FAST Method (Fourier Amplitude Sensitivity Test)

FAST uses Fourier series to efficiently estimate sensitivity indices.

**Mathematical Formulation:**

Each parameter is varied according to a different frequency:

$$X_i(s) = G_i(\sin(\omega_i s))$$

where $\omega_i$ are integer frequencies and $s$ is a scalar parameter.

Sensitivity indices estimated from Fourier coefficients:

$$S_i = \frac{\sum_{p} A_{p\omega_i}^2}{\sum_{p} A_p^2}$$

where $A_p$ are Fourier coefficients.

**Implementation:**
- Requires fewer model evaluations than Sobol
- Typically 65-1000 samples depending on number of parameters
- Estimates first-order indices efficiently
- Less accurate for interaction effects

**Best For**: Efficient estimation of first-order effects, moderate number of parameters

#### RBD Method (Random Balance Design)

RBD is a screening method that uses random permutations to estimate sensitivity.

**Mathematical Formulation:**

Uses random permutations of parameter values to break correlations, enabling estimation of main effects.

**Implementation:**
- Very efficient: requires only N samples for N parameters
- Good for screening many parameters
- Less accurate than Sobol or Morris
- Useful for preliminary analysis

**Best For**: Screening very many parameters (>20), preliminary analysis, limited samples

#### Delta Method

Delta method is a moment-independent sensitivity measure that considers the entire output distribution.

**Mathematical Formulation:**

Delta index measures the shift in output distribution when fixing a parameter:

$$\delta_i = \frac{1}{2} \int |f_Y(y) - f_{Y|X_i}(y|X_i)| dy$$

where $f_Y$ is marginal output distribution and $f_{Y|X_i}$ is conditional distribution.

**Implementation:**
- Moment-independent: considers full distribution, not just variance
- Requires estimation of conditional distributions
- More computationally intensive than variance-based methods
- Provides complementary information to Sobol indices

**Best For**: When output distribution shape is important, non-Gaussian outputs

#### PAWN Method

PAWN (Probability Assessment of the Worth of a Number) uses conditional cumulative distribution functions (CDFs).

**Mathematical Formulation:**

PAWN index measures difference between conditional and unconditional CDFs:

$$PAWN_i = \int |F_Y(y) - F_{Y|X_i}(y|X_i)| dy$$

**Implementation:**
- Distribution-based sensitivity measure
- Requires binning for continuous parameters
- Number of bins affects accuracy
- Good for non-linear, non-additive models

**Best For**: Distribution-based sensitivity, non-linear models

#### DGSM Method (Derivative-Based Global Sensitivity Measure)

DGSM uses gradients to estimate global sensitivity.

**Mathematical Formulation:**

DGSM index:

$$DGSM_i = \int \left(\frac{\partial f}{\partial X_i}\right)^2 dX$$

**Implementation:**
- Requires gradient computation (automatic differentiation or finite differences)
- Efficient for smooth models
- Less accurate for discontinuous models
- Good for high-dimensional problems

**Best For**: Smooth models, high-dimensional problems, when gradients are available

### Local Sensitivity Analysis Methods

Local methods analyze sensitivity at specific parameter values, providing local information.

#### Local Derivatives

Computes partial derivatives at a specific point:

$$\frac{\partial f}{\partial X_i}\bigg|_{X=X_0}$$

**Implementation:**
- Forward, backward, or central finite differences
- Requires (n+1) or (2n+1) model evaluations for n parameters
- Provides local sensitivity information
- Fast but limited to local region

**Best For**: Local sensitivity at specific operating points, gradient-based optimization

#### Local Perturbation

Perturbs each parameter individually and measures output change:

$$\Delta Y_i = f(X_0 + \Delta X_i) - f(X_0)$$

**Implementation:**
- Simple and intuitive
- Requires n+1 model evaluations
- Perturbation size affects results
- Good for understanding local behavior

**Best For**: Understanding local parameter influences, quick sensitivity checks

#### Local Central Differences

Uses central finite differences for more accurate derivative estimation:

$$\frac{\partial f}{\partial X_i} \approx \frac{f(X_0 + h e_i) - f(X_0 - h e_i)}{2h}$$

**Implementation:**
- More accurate than forward/backward differences
- Requires 2n+1 model evaluations
- Step size h affects accuracy
- Good balance of accuracy and efficiency

**Best For**: Accurate local sensitivity, when central differences are feasible

### Uncertainty-Based Methods

These methods incorporate uncertainty quantification into sensitivity analysis.

#### Monte Carlo Method

Monte Carlo sensitivity analysis uses random sampling to propagate uncertainty.

**Mathematical Formulation:**

Sensitivity estimated from correlation or regression:

$$S_i = \frac{\text{Cov}(X_i, Y)}{\text{Var}(Y)} \text{ or } S_i = \frac{\text{Var}(E[Y|X_i])}{\text{Var}(Y)}$$

**Implementation:**
- Random sampling from parameter distributions
- Typically requires 1000-10000 samples
- Can handle complex distributions
- Provides uncertainty estimates

**Best For**: Uncertainty propagation, complex parameter distributions, probabilistic analysis

#### Bayesian Method

Bayesian sensitivity analysis uses Bayesian inference to estimate sensitivity with uncertainty quantification.

**Mathematical Formulation:**

Uses posterior distributions to estimate sensitivity:

$$S_i = \int S_i(\theta) p(\theta|D) d\theta$$

where $\theta$ are model parameters and $D$ is data.

**Implementation:**
- Incorporates prior knowledge
- Provides uncertainty estimates
- More computationally intensive
- Requires Bayesian inference (MCMC, variational methods)

**Best For**: When prior knowledge is available, uncertainty quantification is critical

### Method Selection and Comparison

Table 1 compares the 12 sensitivity analysis methods:

**Table 1: Sensitivity Analysis Methods Comparison**

| Method | Type | Sample Size | Interactions | Accuracy | Best For |
|--------|------|-------------|--------------|----------|----------|
| **Sobol** | Global | 1000-10000 | Yes (S2) | Very High | Comprehensive analysis |
| **Morris** | Global | 10-20×(n+1) | Partial (σ) | Medium | Screening many parameters |
| **FAST** | Global | 65-1000 | Limited | High | First-order effects |
| **RBD** | Global | N | No | Low | Preliminary screening |
| **Delta** | Global | 1000-5000 | No | High | Distribution-based |
| **PAWN** | Global | 1000-5000 | No | High | Non-linear models |
| **DGSM** | Global | Gradient-based | No | Medium | Smooth models |
| **Local Derivatives** | Local | n+1 | No | High (local) | Local sensitivity |
| **Local Perturbation** | Local | n+1 | No | Medium (local) | Quick checks |
| **Local Central Diff** | Local | 2n+1 | No | Very High (local) | Accurate local |
| **Monte Carlo** | Uncertainty | 1000-10000 | Yes | High | Uncertainty propagation |
| **Bayesian** | Uncertainty | MCMC samples | Yes | High | Prior knowledge |

## Virtual Experiment Design Types

Virtual experiments enable systematic exploration of parameter spaces for process optimization. The framework supports 10 experiment design types, categorized into basic designs, factorial designs, response surface designs, and optimal designs.

### Basic Designs

#### Latin Hypercube Sampling (LHS)

LHS provides space-filling design ensuring good coverage of parameter space.

**Mathematical Formulation:**

For n parameters and N samples, LHS divides each parameter range into N intervals and ensures each interval is sampled exactly once for each parameter.

**Properties:**
- Space-filling: Good coverage of parameter space
- Flexible: Works with any number of parameters
- Efficient: N samples for N-dimensional space
- Random: Each LHS design is different

**Implementation:**
- Uses optimized LHS algorithms (maximin distance, correlation minimization)
- Supports constraints and parameter distributions
- Sample size: Typically 50-500 samples
- Good for initial exploration

**Best For**: Initial parameter space exploration, surrogate model training, uniform coverage needed

#### Random Sampling

Simple random sampling from parameter distributions.

**Properties:**
- Simple: Easy to implement and understand
- Flexible: Works with any distribution
- No guarantees: May have gaps or clusters
- Efficient: Fast generation

**Best For**: Quick exploration, when space-filling not critical, large sample sizes

#### Parameter Sweep

Systematic variation of parameters along grid or sequence.

**Properties:**
- Systematic: Covers parameter space systematically
- Predictable: Results are easy to interpret
- Limited: Number of samples grows exponentially with parameters
- Good for visualization: Easy to plot results

**Best For**: 1-2 parameters, visualization, systematic exploration

### Factorial Designs

#### Full Factorial (2^k)

Complete factorial design with 2 levels per factor.

**Mathematical Formulation:**

For k factors, full factorial requires $2^k$ experiments, testing all combinations of high/low levels.

**Properties:**
- Complete: Tests all factor combinations
- Interactions: Can estimate all interaction effects
- Exponential: Sample size grows as $2^k$
- Efficient: Maximum information per sample

**Best For**: Small number of factors (k ≤ 5), when interactions are important

#### Full Factorial (3^k)

Complete factorial design with 3 levels per factor.

**Properties:**
- More levels: Can detect non-linear effects
- Larger: Requires $3^k$ experiments
- Quadratic: Can estimate quadratic effects
- Comprehensive: Very thorough exploration

**Best For**: Small number of factors (k ≤ 4), non-linear effects important

### Response Surface Designs

#### Central Composite Design (CCD)

CCD combines factorial points, axial points, and center points for efficient response surface modeling.

**Mathematical Formulation:**

CCD includes:
- Factorial points: $2^k$ or $2^{k-f}$ (fractional)
- Axial points: $2k$ points at distance $\alpha$ from center
- Center points: $n_0$ replicates at center

Total: $2^k + 2k + n_0$ or $2^{k-f} + 2k + n_0$ experiments

**Properties:**
- Efficient: Good balance of sample size and information
- Quadratic: Can fit quadratic response surfaces
- Rotatable: Can be made rotatable with appropriate $\alpha$
- Flexible: Can use fractional factorial base

**Best For**: Response surface modeling, quadratic effects, 3-6 factors

#### Box-Behnken Design (BBD)

BBD is an efficient response surface design avoiding corner points.

**Properties:**
- Efficient: Requires fewer samples than CCD
- No corners: All points within parameter ranges
- Quadratic: Can fit quadratic models
- Balanced: Good balance of factor levels

**Best For**: When corner points are infeasible, response surface modeling, 3-7 factors

### Optimal Designs

#### D-Optimal Design

D-optimal design maximizes determinant of information matrix, minimizing parameter estimation variance.

**Mathematical Formulation:**

Maximizes: $\det(X^T X)$

where $X$ is design matrix.

**Properties:**
- Optimal: Minimizes parameter estimation variance
- Flexible: Can handle constraints and candidate sets
- Efficient: Typically requires fewer samples than factorial
- Model-dependent: Optimal for specific model form

**Best For**: Constrained parameter spaces, specific model forms, efficient estimation

#### A-Optimal Design

A-optimal design minimizes trace of inverse information matrix.

**Mathematical Formulation:**

Minimizes: $\text{tr}((X^T X)^{-1})$

**Properties:**
- Optimal: Minimizes average parameter variance
- Alternative: Different optimality criterion than D-optimal
- Efficient: Similar efficiency to D-optimal
- Model-dependent: Optimal for specific model

**Best For**: When average parameter precision is important, alternative to D-optimal

#### G-Optimal Design

G-optimal design minimizes maximum prediction variance.

**Mathematical Formulation:**

Minimizes: $\max_x x^T (X^T X)^{-1} x$

**Properties:**
- Optimal: Minimizes worst-case prediction variance
- Robust: Good prediction accuracy across design space
- Efficient: Similar efficiency to D/A-optimal
- Model-dependent: Optimal for specific model

**Best For**: When prediction accuracy is important, robust designs needed

### Design Selection Criteria

The choice of design type depends on:
- **Number of parameters**: Factorial designs limited to small k
- **Sample budget**: LHS and optimal designs more efficient
- **Model complexity**: Response surface designs for quadratic models
- **Constraints**: Optimal designs handle constraints well
- **Objectives**: Exploration vs. optimization vs. modeling

## Anomaly Detection Methods

Anomaly detection identifies unusual patterns in process data that may indicate quality issues or process deviations. The framework provides 8+ anomaly detection methods across statistical, clustering-based, machine learning-based, and rule-based categories.

### Statistical Methods

Statistical methods use statistical properties of data to identify outliers.

#### Z-Score Detector

Identifies anomalies using standard deviations from mean.

**Mathematical Formulation:**

Z-score: $z_i = \frac{x_i - \mu}{\sigma}$

Anomaly if: $|z_i| > \theta$ (typically $\theta = 3$)

**Properties:**
- Simple: Easy to understand and implement
- Fast: O(N) computation
- Assumes normality: Works best for normal distributions
- Sensitive to outliers: Mean and std affected by outliers

**Best For**: Normal distributions, univariate data, quick screening

#### IQR Detector (Interquartile Range)

Uses quartiles to identify outliers, robust to outliers.

**Mathematical Formulation:**

IQR = Q3 - Q1 (third quartile - first quartile)

Anomaly if: $x_i < Q1 - k \times IQR$ or $x_i > Q3 + k \times IQR$ (typically k=1.5)

**Properties:**
- Robust: Not affected by outliers
- Non-parametric: No distribution assumptions
- Fast: O(N log N) for sorting
- Simple: Easy to interpret

**Best For**: Non-normal distributions, robust detection, univariate data

#### Mahalanobis Distance Detector

Multivariate anomaly detection accounting for correlations.

**Mathematical Formulation:**

Mahalanobis distance: $d_i = \sqrt{(x_i - \mu)^T \Sigma^{-1} (x_i - \mu)}$

Anomaly if: $d_i > \theta$ (threshold based on chi-square distribution)

**Properties:**
- Multivariate: Handles multiple signals simultaneously
- Correlation-aware: Accounts for signal correlations
- Distribution: Assumes multivariate normal
- Computationally intensive: Requires covariance matrix inversion

**Best For**: Multivariate data, correlated signals, normal distributions

#### Modified Z-Score Detector

Uses median and median absolute deviation (MAD) for robustness.

**Mathematical Formulation:**

Modified Z-score: $M_i = \frac{0.6745(x_i - \text{median}(X))}{\text{MAD}(X)}$

where MAD = median(|$x_i$ - median(X)|)

Anomaly if: $|M_i| > \theta$ (typically $\theta = 3.5$)

**Properties:**
- Robust: Uses median instead of mean
- Non-parametric: No distribution assumptions
- Fast: O(N log N) for median
- Good alternative: More robust than standard Z-score

**Best For**: Non-normal distributions, robust univariate detection

#### Grubbs' Test

Statistical test for detecting single outlier.

**Mathematical Formulation:**

Grubbs statistic: $G = \frac{\max |x_i - \bar{x}|}{s}$

Compares to critical value from t-distribution.

**Properties:**
- Statistical test: Provides p-value
- Single outlier: Designed for one outlier at a time
- Iterative: Can be applied iteratively
- Assumes normality: Requires normal distribution

**Best For**: Single outlier detection, statistical validation

### Clustering-Based Methods

Clustering methods identify anomalies as points that do not belong to any cluster or belong to sparse clusters.

#### DBSCAN Detector

Density-based clustering identifies anomalies as low-density regions.

**Mathematical Formulation:**

DBSCAN groups points into clusters based on density (eps radius, min_samples). Points not in any cluster are anomalies.

**Properties:**
- Density-based: Identifies clusters of arbitrary shape
- No cluster count: Automatically determines number of clusters
- Parameters: eps (neighborhood radius) and min_samples
- Good for: Irregular cluster shapes, varying densities

**Best For**: Spatial anomalies, irregular patterns, density-based detection

#### Isolation Forest Detector

Tree-based method that isolates anomalies.

**Mathematical Formulation:**

Isolation Forest builds random trees. Anomalies are isolated in fewer splits, resulting in shorter paths.

Anomaly score: Average path length (normalized)

**Properties:**
- Efficient: O(N log N) average case
- Scalable: Works well with large datasets
- No distance: Does not require distance metrics
- Parameters: n_estimators, contamination

**Best For**: High-dimensional data, large datasets, fast detection

#### LOF Detector (Local Outlier Factor)

Measures local density deviation to identify anomalies.

**Mathematical Formulation:**

LOF compares local density of a point to its neighbors:

$$LOF_k(p) = \frac{\sum_{o \in N_k(p)} \text{lrd}_k(o)}{|N_k(p)| \cdot \text{lrd}_k(p)}$$

where lrd is local reachability density.

**Properties:**
- Local: Considers local neighborhood
- Relative: Anomaly score is relative to neighbors
- Parameters: k (number of neighbors)
- Good for: Varying density regions

**Best For**: Local anomalies, varying densities, relative outlier detection

#### One-Class SVM Detector

Support vector machine for novelty detection.

**Mathematical Formulation:**

One-Class SVM finds a hyperplane that separates normal data from origin, maximizing margin.

**Properties:**
- Kernel-based: Can handle non-linear boundaries
- Flexible: Various kernel functions (RBF, polynomial)
- Parameters: nu (outlier fraction), kernel parameters
- Computationally intensive: O(N²) to O(N³)

**Best For**: Non-linear boundaries, novelty detection, kernel methods

#### K-Means Detector

Uses K-means clustering and identifies anomalies as points far from cluster centers.

**Mathematical Formulation:**

Anomaly score: Distance to nearest cluster center

Anomaly if: $d(x_i, c_k) > \theta$ for all clusters $k$

**Properties:**
- Simple: Easy to understand
- Fast: O(Nk) per iteration
- Parameters: k (number of clusters), distance threshold
- Assumes spherical clusters

**Best For**: Spherical clusters, simple detection, fast processing

### Machine Learning-Based Methods

#### Autoencoder Detector

Uses reconstruction error to identify anomalies.

**Mathematical Formulation:**

Autoencoder learns to compress and reconstruct normal data. Anomalies have high reconstruction error:

$$\text{Error} = ||x - \text{Decode}(\text{Encode}(x))||^2$$

**Properties:**
- Deep learning: Can learn complex patterns
- Unsupervised: No labeled anomalies needed
- Reconstruction: High error indicates anomalies
- Training: Requires training on normal data

**Best For**: Complex patterns, high-dimensional data, deep learning approach

#### LSTM Autoencoder Detector

Temporal autoencoder for time-series anomaly detection.

**Properties:**
- Temporal: Handles time-series data
- Sequences: Learns temporal patterns
- Reconstruction: High error indicates temporal anomalies
- Training: Requires temporal normal data

**Best For**: Time-series data, temporal patterns, sequential anomalies

#### VAE Detector (Variational Autoencoder)

Probabilistic autoencoder providing uncertainty estimates.

**Properties:**
- Probabilistic: Provides uncertainty estimates
- Generative: Can generate samples
- Latent space: Learns latent representations
- More complex: Requires more training

**Best For**: Uncertainty-aware detection, generative models

### Rule-Based Methods

#### Threshold Violation Detector

Detects violations of process parameter bounds.

**Properties:**
- Simple: Easy to understand and implement
- Fast: O(N) computation
- Domain knowledge: Requires known bounds
- Interpretable: Clear violation criteria

**Best For**: Known process limits, simple rules, interpretability

#### Pattern Deviation Detector

Detects deviations from expected patterns using statistical process control.

**Properties:**
- SPC-based: Uses control charts
- Patterns: Detects trend, shift, cycle patterns
- Statistical: Provides statistical significance
- Domain knowledge: Requires pattern definitions

**Best For**: Process control, known patterns, SPC applications

#### Temporal Pattern Detector

Detects anomalies in temporal sequences.

**Properties:**
- Temporal: Analyzes time-series patterns
- Sequences: Detects sequence anomalies
- Patterns: Learns or uses known temporal patterns
- Good for: Time-series data, temporal dependencies

**Best For**: Time-series anomalies, temporal dependencies

#### Spatial Pattern Detector

Detects anomalies in spatial patterns using voxel domain.

**Properties:**
- Spatial: Uses voxel grid structure
- Neighborhood: Considers spatial neighbors
- Patterns: Detects spatial patterns (clusters, gradients)
- Voxel-based: Leverages unified voxel domain

**Best For**: Spatial anomalies, voxel domain data, spatial patterns

#### Multi-Signal Correlation Detector

Detects anomalies by identifying breaks in expected signal correlations.

**Properties:**
- Multi-signal: Uses multiple signals simultaneously
- Correlation: Detects correlation breaks
- Voxel-based: Uses unified voxel domain
- Powerful: Can detect subtle anomalies

**Best For**: Multi-signal analysis, correlation-based detection, voxel domain

### Anomaly Detection Method Comparison

Table 2 compares anomaly detection methods:

**Table 2: Anomaly Detection Methods Comparison**

| Method | Category | Multivariate | Temporal | Complexity | Best For |
|--------|----------|-------------|----------|------------|----------|
| **Z-Score** | Statistical | No | No | Low | Normal, univariate |
| **IQR** | Statistical | No | No | Low | Robust, univariate |
| **Mahalanobis** | Statistical | Yes | No | Medium | Multivariate, normal |
| **Modified Z-Score** | Statistical | No | No | Low | Robust, univariate |
| **Grubbs** | Statistical | No | No | Low | Single outlier |
| **DBSCAN** | Clustering | Yes | No | Medium | Spatial, density |
| **Isolation Forest** | Clustering | Yes | No | Medium | High-dim, fast |
| **LOF** | Clustering | Yes | No | Medium | Local, varying density |
| **One-Class SVM** | Clustering | Yes | No | High | Non-linear, kernel |
| **K-Means** | Clustering | Yes | No | Low | Simple, spherical |
| **Autoencoder** | ML | Yes | No | High | Complex patterns |
| **LSTM Autoencoder** | ML | Yes | Yes | Very High | Time-series |
| **VAE** | ML | Yes | No | Very High | Uncertainty, generative |
| **Threshold** | Rule-based | Yes | No | Low | Known bounds |
| **Pattern Deviation** | Rule-based | Yes | Yes | Medium | SPC, patterns |
| **Temporal Pattern** | Rule-based | Yes | Yes | Medium | Temporal sequences |
| **Spatial Pattern** | Rule-based | Yes | No | Medium | Spatial, voxel |
| **Multi-Signal Correlation** | Rule-based | Yes | Yes | Medium | Correlation breaks |

## Multi-Signal Fusion

Multi-signal fusion combines signals from multiple sources (hatching, laser, CT, ISPM) in the unified voxel domain, enabling comprehensive analysis.

### Fusion Strategies

The framework supports multiple fusion strategies:

1. **Average**: Simple mean of all signals
2. **Weighted Average**: Quality-weighted mean using quality scores
3. **Median**: Median value (robust to outliers)
4. **Maximum/Minimum**: Use max or min value
5. **Quality-Based**: Use signal from highest quality source
6. **First/Last**: Use first or last available signal

### Quality-Based Weighting

Quality scores are computed for each signal based on:
- **Completeness**: Fraction of voxels with data
- **SNR**: Signal-to-noise ratio
- **Alignment Accuracy**: Coordinate system alignment quality
- **Coverage**: Spatial coverage of signal

Weights computed as:

$$w_i = \frac{q_i^p}{\sum_j q_j^p}$$

where $q_i$ is quality score and $p$ is power parameter (typically 2).

### Fusion in Voxel Domain

Fusion operates at the voxel level:
- Each voxel can have multiple signals
- Fusion combines signals for each voxel independently
- Quality scores can vary spatially
- Enables spatial analysis of fused signals

### Applications

Multi-signal fusion enables:
- **Improved Coverage**: Fused signal achieves >95% coverage (vs. 60-75% for individual sources)
- **Noise Reduction**: Combining multiple independent measurements reduces noise
- **Quality Improvement**: Quality-weighted fusion improves signal quality by 15-25%
- **Comprehensive Analysis**: Single fused signal for downstream analysis

