# Implementation and API

## Overview

Signal processing and correction are implemented in **C++** (am_qadf_native) with **Python** wrappers. Eigen is used for linear algebra; KFR is intended for FFT and filters (available in third_party, enable in build as needed).

## C++ Components

### Processing

- **SignalProcessing** (`src/am_qadf_native/src/processing/signal_processing.cpp`): `normalize`, `movingAverage`, `derivative`, `integral`, `fft`, `ifft`, `frequencyFilter`. FFT/frequencyFilter may use KFR or placeholders until KFR is enabled.
- **SignalNoiseReduction** (`src/am_qadf_native/src/correction/signal_noise_reduction.cpp`): Gaussian filter, Savitzky–Golay (Eigen for convolution/polynomial matrix), outlier removal interfaces. Used by Python `SignalSmoother` and `OutlierDetector`.

### Correction

- **Calibration** (`src/am_qadf_native/src/correction/calibration.cpp`): Reference measurements, calibration data, parameter application; interfaces for CalibrationManager.
- **Geometric correction** (`geometric_correction.cpp`, `geometric_distortion.py`): Scaling, rotation, warping models; combined model application.
- **Validation** (`validation.cpp`, `validation.py`): Alignment quality, validation metrics, correction validator.

### Python Wrappers

- **processing/noise_reduction.py**: `OutlierDetector`, `SignalSmoother`, `NoiseReductionPipeline`; call C++ `SignalNoiseReduction` (e.g. `apply_gaussian_filter`, `apply_savitzky_golay`).
- **correction/**: `CalibrationManager`, `ReferenceMeasurement`, `CalibrationData`; `DistortionModel`, `ScalingModel`, `RotationModel`, `WarpingModel`, `CombinedDistortionModel`; `CorrectionValidator`, `AlignmentQuality`, `ValidationMetrics`.

## Main Entry Points

### Noise Reduction (Python)

```python
from am_qadf.processing import SignalSmoother

smoother = SignalSmoother()
smoothed = smoother.smooth(values, method="gaussian", sigma=1.0)
# or method="savitzky_golay" with window_size, polyorder
```

### Calibration (Python)

```python
from am_qadf.correction import CalibrationManager, ReferenceMeasurement

manager = CalibrationManager()
manager.register_calibration(name="ct_scanner", reference_measurements=[ref])
corrected = manager.apply_calibration_correction(points=points, calibration_name="ct_scanner")
```

### Geometric Correction (Python)

```python
from am_qadf.correction import ScalingModel, RotationModel, CombinedDistortionModel

combined = CombinedDistortionModel([ScalingModel(...), RotationModel(...)])
corrected_points = combined.correct(distorted_points)
```

## Build and Dependencies

- **Eigen**: Required for processing and correction (Savitzky–Golay, RBF, calibration). Found via CMake (conda or third_party).
- **KFR**: Optional; when enabled, used for FFT and frequency filtering. Set KFR root in CMake; see `docs/Infrastructure/third-party/kfr.md` and `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`.

## Design Documents

- **Processing**: `docs/AM_QADF/05-modules/processing.md`, `docs/AM_QADF/06-api-reference/processing-api.md`
- **Correction**: `docs/AM_QADF/05-modules/correction.md`, `docs/AM_QADF/06-api-reference/correction-api.md`
- **Libraries**: `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`, `docs/Infrastructure/third-party/eigen.md`, `kfr.md`
