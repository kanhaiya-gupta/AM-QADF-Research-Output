# Related Work

## Noise Reduction and Filtering in AM

Additive manufacturing process and monitoring data are often filtered to reduce noise before analysis or mapping. Common approaches include moving average and Gaussian smoothing for time-series and path-based signals; Savitzky–Golay filtering is used when derivative preservation is important. Outlier detection (IQR, z-score, modified z-score) is applied to remove spurious measurements. Frequency-domain filtering (lowpass, highpass) is used when noise is band-limited. Our framework implements these methods in a unified pipeline (outlier detection → smoothing → optional frequency filter) with C++ back ends (Eigen for Savitzky–Golay, KFR or FFTW for FFT) and Python wrappers.

## Calibration and Geometric Correction

Multi-source AM data often require calibration (reference-based correction of sensor/scanner bias) and geometric distortion correction (scaling, rotation, warping) to align with a reference frame and to correct systematic coordinate and intensity errors. Prior work uses reference artifacts, CMM measurements, and CT calibration phantoms to establish calibration parameters. Our framework provides a CalibrationManager, reference measurements, calibration data storage, and validation metrics (mean/max/RMS error), with flexible application at pre-mapping, post-mapping, pre-fusion, or post-fusion stages.

## Eigen and KFR in Scientific Code

**Eigen** is widely used for linear algebra in scientific and machine-learning code (matrix operations, linear systems, SVD). We use it for Savitzky–Golay convolution matrices (polynomial fitting over sliding windows), RBF interpolation systems (shared with signal mapping), and calibration least-squares fits. **KFR** is a modern C++ DSP library (FFT, FIR/IIR filters, convolution) with SIMD optimization; it can replace or complement FFTW for FFT and frequency-domain filtering. The implementation plan (`implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`) recommends KFR + Eigen for signal processing; Eigen is in use in the build; KFR is available in third_party and can be enabled for FFT and filter implementations.

## Relation to Signal Mapping (Paper 3)

Signal mapping (Paper 3) transforms aligned point-based data into a voxel grid via interpolation (nearest, linear, IDW, KDE, RBF). It assumes spatially and temporally aligned data (Paper 1) and *optionally* processed and corrected signals (this paper). Paper 3 references calibration and correction as prerequisites; this paper (Paper 2) provides their design, algorithms, and implementation. There is no duplication: Paper 2 focuses on *what* values to use; Paper 3 focuses on *where* to put them.
