# Conclusion

## Summary of Contributions

This paper established **signal processing and correction** as a required step **between** spatial and temporal alignment (Paper 0) and signal mapping (Paper 1). Raw process and monitoring signals are noisy and can contain systematic errors; applying noise reduction, calibration, and geometric correction **before** mapping ensures that the voxel-domain representation (Paper 1) and downstream analysis (Papers 2–3) are reliable.

### 1. Pipeline Position

We made explicit the pipeline: **align (Paper 0) → process and correct (Paper 0.5) → map (Paper 1)**. Processing and correction answer *what* values to use; signal mapping answers *where* to put them. Paper 1 references calibration and correction as prerequisites; this paper provides their design, algorithms, and implementation.

### 2. Noise Reduction and Filtering

We described and implemented outlier detection (IQR, z-score), smoothing (Gaussian, Savitzky–Golay, moving average), and frequency-domain filtering (FFT, inverse FFT, lowpass/highpass/bandpass). Savitzky–Golay uses **Eigen** for the convolution/polynomial matrix; FFT and frequency filtering are intended to use **KFR** (or FFTW when KFR is not enabled). C++ back ends and Python wrappers provide a unified noise-reduction pipeline.

### 3. Calibration and Geometric Correction

We described reference-based calibration (CalibrationManager, reference measurements, calibration data) and geometric distortion correction (scaling, rotation, warping, combined). Validation metrics (mean/max/RMS error) support pass/fail and reporting. Application can be pre-mapping (default), post-mapping, pre-fusion, or post-fusion, as documented in Paper 1.

### 4. Why Eigen and KFR

We justified **Eigen** for linear algebra (Savitzky–Golay, RBF systems, calibration fits): header-only, already in use, sufficient performance. We justified **KFR** for FFT and filters: SIMD-optimized, optional header-only use, recommended in the implementation plan alongside Eigen. We noted that KFR is available in third_party and can be enabled in the build for full FFT/filter support.

### 5. Implementation and API

We summarized the C++ components (SignalProcessing, SignalNoiseReduction, calibration, geometric correction, validation) and Python entry points (processing.noise_reduction, correction). Design and API details are in the repository (processing and correction modules, processing-api and correction-api, third-party docs).

## Impact

- **Foundation for Paper 1**: Signal mapping (Paper 1) assumes optionally processed and corrected signals; this paper defines and implements that step.
- **Quality and traceability**: Calibration parameters and correction models can be stored; validation metrics support reproducibility and audit.
- **Consistent stack**: Eigen (and KFR when enabled) provide a single, modern stack for signal processing and correction without unnecessary dependencies.

## Closing Remark

Signal processing and correction are not an afterthought but a **prerequisite** for reliable signal mapping and analysis in multi-source PBF-LB/M data. This paper presented their pipeline position, design, library rationale (Eigen and KFR), and implementation, completing the data-preparation chain: Paper 0 (alignment) → Paper 0.5 (processing and correction) → Paper 1 (signal mapping) → Papers 2–3 (analysis and application).
