# Discussion

## Advantages

### Pre-Mapping Processing and Correction

Applying noise reduction and correction **before** signal mapping (Paper 3) keeps the mapping step focused on interpolation and grid structure, and ensures that systematic errors and noise do not propagate into the voxel domain. Validation metrics (SNR, calibration error, correction residual) are computed at the signal and point level, making quality traceable. Flexible application stages (pre-mapping default; optional post-mapping, pre-fusion, post-fusion) allow addressing residual errors when they are detected later.

### Eigen for Linear Algebra

Eigen provides a single, header-only dependency for Savitzky–Golay (convolution matrix), RBF systems (shared with signal mapping), and calibration fits. No separate linear-algebra library is required; performance is sufficient for the window and matrix sizes used in this framework. The same library is already used in synchronization (e.g. Kabsch, Umeyama), so the dependency is consistent across the codebase.

### KFR for FFT and Filters

KFR offers FFT and filter implementations in one DSP library, with SIMD optimization and optional header-only use. When enabled in the build, it can replace FFTW for FFT and frequency-domain filtering, reducing external dependencies. The implementation plan recommends KFR + Eigen as the preferred modern stack; the paper documents this choice and the intended use even if KFR is not yet enabled in all builds.

### Clear Separation from Signal Mapping

Paper 2 (processing and correction) addresses *what* values to use; Paper 3 (signal mapping) addresses *where* to put them. This separation keeps each paper focused and avoids duplication. Paper 3 continues to state that calibration and correction are prerequisites and references Paper 2 for their design and implementation.

## Limitations

### KFR Build Status

KFR is available in third_party and documented but currently **disabled** in the build. FFT and frequencyFilter in C++ may use placeholders or an alternative (e.g. FFTW) until KFR is enabled. The paper describes the intended design and rationale; full FFT/filter results depend on build configuration.

### Calibration and Reference Data

Calibration quality depends on the availability and quality of reference measurements (CMM, phantom, etc.). When reference data are scarce or noisy, calibration parameters may be uncertain; validation metrics should be reported and used for decision-making. Geometric correction (warping) may require sufficient reference point density to avoid overfitting.

### Processing Parameters

Smoothing window size, polynomial order (Savitzky–Golay), and filter cutoffs (frequency domain) are user- or application-dependent. The framework provides the methods and APIs; parameter selection (e.g. from SNR or cross-validation) is not fully automated. Best practices and guidelines can be documented in user docs or future work.

### 3D and Voxel-Level Processing

This paper emphasizes 1D/time-series and point-level processing (smoothing, calibration, geometric correction). 3D voxel-level filtering (e.g. Gaussian or median on the voxel grid) can be done with ITK or similar tools and is complementary; it may be mentioned as future work or in relation to post-mapping correction.

## Future Work

- **Enable KFR in build**: Complete FFT and frequencyFilter implementation using KFR; benchmark vs FFTW; document build and usage.
- **Automated parameter selection**: Heuristics or cross-validation for window size, polynomial order, and filter cutoffs based on SNR or residual metrics.
- **3D filtering**: Integration with ITK (or similar) for voxel-grid smoothing when post-mapping correction is used.
- **Uncertainty propagation**: Propagate calibration and correction uncertainty into mapped values and downstream analysis.

## Summary

Signal processing and correction improve the quality of the inputs to signal mapping and are a necessary step in the pipeline. Eigen and KFR (when enabled) provide a consistent, modern implementation stack. Limitations include KFR build status, dependence on reference data for calibration, and the need for user-tuned or heuristic processing parameters. Future work can address full KFR enablement, automation of parameter choice, and 3D/voxel-level filtering.
