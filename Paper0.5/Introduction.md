# Introduction

## Problem Statement

PBF-LB/M process and monitoring data are **noisy** and can contain **systematic errors**:

- **Hatching and laser**: Time-series and path-based signals with measurement noise and occasional outliers.
- **ISPM**: Sensor-specific noise, drift, and calibration offsets.
- **CT**: Scanner calibration, geometric distortion (scaling, rotation, warping), and artifact-related bias.

If these signals are mapped directly to a voxel domain (Paper 1), noise and systematic errors propagate into the unified representation and into all downstream analysis (Paper 2, Paper 3). **Signal processing and correction** are therefore **prerequisites** for reliable signal mapping: we must improve *what* values we use (filtering, calibration, distortion correction) before deciding *where* to put them (interpolation to voxels).

## Motivation

### Why Process and Correct Before Mapping

1. **Noise reduction**: Smoothing (Gaussian, Savitzky–Golay, moving average) and outlier detection (IQR, z-score) improve signal-to-noise ratio and reduce the impact of spurious values on mapped voxels.

2. **Calibration**: Reference-based calibration corrects systematic sensor and scanner biases so that mapped values are physically meaningful and comparable across sources.

3. **Geometric correction**: Distortion models (scaling, rotation, warping) correct coordinate and intensity errors that would otherwise propagate through alignment and mapping.

4. **Pipeline clarity**: Applying processing and correction **before** mapping (or at well-defined stages: pre-mapping, optional post-mapping/pre-fusion/post-fusion) keeps the mapping step (Paper 1) focused on interpolation and grid structure, and makes quality traceable.

### Scope of This Paper

This paper focuses on:

- **Noise reduction and filtering**: Outlier detection, smoothing methods (Gaussian, Savitzky–Golay, moving average), and frequency-domain filtering (FFT, inverse FFT, lowpass/highpass/bandpass) where applicable.
- **Calibration**: Reference measurements, calibration data, CalibrationManager, and validation (mean/max/RMS error).
- **Geometric correction**: Distortion models (scaling, rotation, warping, combined), application stages, and validation.
- **Implementation**: Rationale for **Eigen** (linear algebra) and **KFR** (FFT, filters); integration in C++ and Python; pipeline position relative to Paper 0 (alignment) and Paper 1 (signal mapping).

Paper 1 (signal mapping) states that calibration and correction are prerequisites and *where* they fit; this paper provides the **design, algorithms, and implementation** of signal processing and correction, including the choice of Eigen and KFR.

## Paper Outline

The remainder of this paper is organized as follows. **Related Work** reviews noise reduction, calibration, and correction in AM and the use of Eigen/KFR in scientific code. **Design** describes the noise-reduction and filtering pipeline, calibration framework, and geometric correction workflow, with equations and flowcharts. **Why Eigen and KFR** justifies the library choices and their roles. **Implementation and API** summarizes the C++/Python components and entry points. **Results** presents quality metrics, calibration/correction validation, and performance. **Discussion** and **Conclusion** summarize contributions and limitations.
