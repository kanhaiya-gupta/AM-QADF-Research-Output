# Signal Processing and Correction for Multi-Source PBF-LB/M Data

## Abstract

Powder Bed Fusion - Laser Beam/Metal (PBF-LB/M) additive manufacturing integrates data from multiple sources—hatching paths, laser parameters, in-situ process monitoring (ISPM), and computed tomography (CT)—that exhibit noise, outliers, and systematic errors. Signal mapping (Paper 3) places these signals onto a unified voxel domain; the *quality* of the mapped result depends on the *quality* of the signals before mapping. This paper presents the **design and implementation of signal processing and correction** that must be applied **before or alongside** signal mapping: noise reduction (outlier detection, smoothing via Gaussian, Savitzky–Golay, and moving average), frequency-domain filtering (FFT, inverse FFT, lowpass/highpass/bandpass), calibration (reference-based, CalibrationManager), and geometric distortion correction (scaling, rotation, warping). We justify the use of **Eigen** for linear algebra (Savitzky–Golay convolution matrices, RBF systems, calibration fits) and **KFR** for digital signal processing (FFT, FIR/IIR filters). The pipeline position is explicit: aligned data (Paper 0) → process and correct signals (this paper) → map to voxel domain (Paper 1). Results demonstrate improved signal-to-noise ratio, calibration validation, and correction accuracy when processing and correction are applied pre-mapping. This paper establishes the foundation for reliable signal mapping and downstream analysis in the AM-QADF framework.

## Keywords

Signal processing; Noise reduction; Calibration; Geometric correction; PBF-LB/M; Savitzky–Golay; Eigen; KFR; Pre-mapping quality; Additive manufacturing
