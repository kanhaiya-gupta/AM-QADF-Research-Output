# Tables

## Required Tables

### Table 1: Pipeline Position (Paper 1, 2, 3)

- **Location**: Introduction or Design
- **Content**: Role of each paper in the data-preparation and mapping pipeline
- **Columns**: Paper | Role | Input | Output
- **Rows**:
  - Paper 1: Alignment; multi-source raw; aligned points, signals, unified frame
  - Paper 2: Processing and correction; aligned points/signals; processed, corrected signals
  - Paper 3: Signal mapping; processed/aligned signals; unified voxel domain

### Table 2: Smoothing Methods Comparison

- **Location**: Design (Noise Reduction) or Results
- **Content**: Comparison of Gaussian, Savitzky–Golay, moving average
- **Columns**: Method | Parameters | Derivative preservation | Complexity | Typical use
- **Rows**: Gaussian (σ); Savitzky–Golay (window, polyorder); Moving average (window). Brief notes on derivative preservation, complexity, use case.

### Table 3: Library Roles (Eigen vs KFR)

- **Location**: Why Eigen and KFR
- **Content**: Which component uses which library
- **Columns**: Component | Eigen | KFR
- **Rows**: Savitzky–Golay (Eigen: convolution matrix); RBF (Eigen: linear system); Calibration (Eigen: least-squares); FFT / frequency filter (KFR or FFTW). Checkmarks or brief notes.

### Table 4: Application Stages for Calibration and Correction

- **Location**: Design (Calibration / Geometric Correction)
- **Content**: Pre-mapping, post-mapping, pre-fusion, post-fusion
- **Columns**: Stage | When to use | Input | Output
- **Rows**: Pre-mapping (default); Post-mapping (residual errors); Pre-fusion (signal-specific); Post-fusion (rare). Short description per stage.

### Table 5: C++ and Python Components (Summary)

- **Location**: Implementation and API
- **Content**: Main C++ and Python entry points
- **Columns**: Component | C++ | Python
- **Rows**: Noise reduction (SignalNoiseReduction, SignalSmoother/OutlierDetector); Calibration (calibration.cpp, CalibrationManager); Geometric correction (geometric_correction.cpp, DistortionModel subclasses); Validation (validation.cpp, CorrectionValidator).

### Table 6: Quality Metrics (Example)

- **Location**: Results
- **Content**: (To be filled with experimental data.) SNR before/after, calibration error before/after, runtime
- **Columns**: Metric | Raw | After processing | After correction
- **Data**: Placeholder until benchmarks are run.

## Table Captions (Draft)

**Table 1**: Pipeline position of Paper 1 (alignment), Paper 2 (processing and correction), and Paper 3 (signal mapping).

**Table 2**: Comparison of smoothing methods (Gaussian, Savitzky–Golay, moving average).

**Table 3**: Use of Eigen and KFR in signal processing and correction components.

**Table 4**: Application stages for calibration and geometric correction (pre-mapping default, optional post-mapping/pre-fusion/post-fusion).

**Table 5**: Summary of C++ and Python components for processing and correction.

**Table 6**: Example quality metrics before and after processing and correction (to be replaced with actual data).
