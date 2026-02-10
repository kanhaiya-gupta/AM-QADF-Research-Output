# Paper 0.5: Signal Processing and Correction (Foundation for Mapping)

**Title**: Signal Processing and Correction for Multi-Source PBF-LB/M Data: Noise Reduction, Calibration, and Pre-Mapping Quality

**Target Venue**: To be determined (foundation paper; may be submitted with Paper 0/1 or to a signal processing / AM venue)

**Status**: In progress — structure complete; content to be refined and filled with experimental results

## Paper Structure

This paper focuses on **signal processing and correction** as the step **between** alignment (Paper 0) and signal mapping (Paper 1).

### Sections

1. [Abstract](Abstract.md) (250 words)
2. [Introduction](Introduction.md) (Why process/correct before mapping; pipeline position)
3. [Related Work](Related_Work.md) (Noise reduction, calibration, Eigen/KFR in AM and scientific code)
4. [Design](Design.md) (Pipeline position; noise reduction and filtering; calibration; geometric correction; flowcharts)
5. [Why Eigen and KFR](Why_Eigen_and_KFR.md) (Library rationale, roles, KFR + Eigen vs FFTW + Eigen)
6. [Implementation and API](Implementation_and_API.md) (C++ components, Python wrappers, entry points)
7. [Results](Results.md) (Quality metrics, calibration/correction validation, performance)
8. [Discussion](Discussion.md) (Advantages, limitations)
9. [Conclusion](Conclusion.md)
10. [References](References.md)
11. [Figures](Figures.md) (Pipeline, noise reduction, correction workflow)
12. [Tables](Tables.md) (Pipeline position, smoothing methods, library roles, application stages)

## Key Contributions

1. **Pipeline position**: Explicit placement of signal processing and correction **after** alignment (Paper 0) and **before** signal mapping (Paper 1).
2. **Noise reduction and filtering**: Outlier detection, smoothing (Gaussian, Savitzky–Golay, moving average), optional FFT/frequency filtering; C++ and Python API.
3. **Calibration and geometric correction**: Reference-based calibration (CalibrationManager), distortion models (scaling, rotation, warping), validation, multi-stage application.
4. **Why Eigen and KFR**: Eigen for linear algebra (Savitzky–Golay, RBF, calibration); KFR for FFT and filters (intended; available in third_party, enable in build as needed).
5. **Separation from signal mapping**: Paper 0.5 addresses *what* values to use; Paper 1 addresses *where* to put them.

## Why Paper 0.5?

**Signal mapping** (Paper 1) answers *where* to put signal values (interpolation to voxels). **Signal processing and correction** answer *what* values to use: raw signals are noisy and can have systematic errors; we need filtering, calibration, and distortion correction **before** mapping. Paper 1 states that calibration and correction are prerequisites; Paper 0.5 provides their **design, algorithms, and implementation**, including Eigen and KFR.

## Design Documents (Main Repository)

- **Processing**: `docs/AM_QADF/05-modules/processing.md`, `docs/AM_QADF/06-api-reference/processing-api.md`
- **Correction**: `docs/AM_QADF/05-modules/correction.md`, `docs/AM_QADF/06-api-reference/correction-api.md`
- **Libraries**: `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`; `docs/Infrastructure/third-party/eigen.md`, `kfr.md`, `README.md`
- **C++**: `src/am_qadf_native/src/processing/signal_processing.cpp`, `src/am_qadf_native/src/correction/signal_noise_reduction.cpp`, `calibration.cpp`, `geometric_correction.cpp`
- **Python**: `src/am_qadf/processing/noise_reduction.py`, `src/am_qadf/correction/`

## Checklist

See the **Publication Checklist** in [Publication_Narrative.md](../Publication_Narrative.md) for Paper 0.5 items.

---

**Parent**: [Publications README](../README.md)
