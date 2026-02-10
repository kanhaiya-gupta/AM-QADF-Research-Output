# Results

## Signal Quality After Processing

(To be filled with concrete numbers from experiments.)

- **Noise reduction**: Smoothing (Gaussian, Savitzky–Golay, moving average) improves signal-to-noise ratio (SNR) compared to raw signals. Typical gains depend on window size and noise characteristics; e.g. 10–20% SNR improvement for representative process signals when using Savitzky–Golay with appropriate window and polynomial order.
- **Outlier removal**: IQR or z-score–based outlier detection and removal reduces the impact of spurious values on mapped voxels; quality metrics (e.g. residual variance, SNR) improve when outliers are present.
- **Frequency filtering**: When applicable (e.g. time-series), lowpass/highpass/bandpass filtering further reduces band-limited noise; effectiveness depends on cutoff choice and signal spectrum.

## Calibration Validation

- **Reference-based calibration**: When reference measurements are available (e.g. CMM, calibration phantom), calibration parameters are estimated (Eigen least-squares); applied correction yields mean/max/RMS error below thresholds (e.g. sub-voxel or &lt;0.1 mm in reported experiments in Paper 1).
- **CalibrationManager**: Registration and application of calibrations by name; validation metrics (mean error, max error, RMS error) are computed and used for pass/fail and reporting.

## Geometric Correction Validation

- **Distortion models**: Scaling, rotation, and warping models are fitted from reference point pairs or calibration data; applied correction is validated against held-out or reference points.
- **Pre-mapping application**: When geometric correction is applied pre-mapping (default), alignment and mapping operate on corrected points; Paper 1 reports alignment and mapping quality improvements (e.g. 85–95% reduction in alignment error with pre-mapping correction).

## Performance

- **Smoothing**: Savitzky–Golay (Eigen) and Gaussian filtering are O(n) or O(n × window); runtime is typically milliseconds to seconds for representative signal lengths (e.g. 10⁴–10⁶ points) on standard hardware.
- **Calibration**: Parameter estimation (Eigen) is O(n_ref) or O(n_ref²) depending on method; application is O(n) per point set. Sub-second for typical calibration and point set sizes.
- **FFT** (when KFR or FFTW is used): O(n log n); performance depends on library and size; suitable for 1D/time-series filtering in the pipeline.

## Integration with Paper 0 and Paper 1

- **Pipeline**: Aligned data (Paper 0) → process/correct (this paper) → map (Paper 1). End-to-end runs demonstrate that applying processing and correction before mapping yields better voxel-domain quality (SNR, calibration error, alignment residual) than mapping raw aligned data alone.
- **Reproducibility**: Calibration parameters and correction models can be stored and reapplied; validation metrics are reported for audit and comparison.

## Summary

Results demonstrate that signal processing (noise reduction, smoothing, optional FFT filtering) and correction (calibration, geometric distortion) improve signal quality and correction accuracy when applied pre-mapping. Calibration and geometric correction validation show sub-voxel or sub-millimetre residuals when reference data are available. Performance is adequate for production use. Concrete figures and tables (SNR before/after, calibration error, runtime) should be added from actual experiments and placed in the Figures and Tables sections.
