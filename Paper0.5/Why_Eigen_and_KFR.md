# Why Eigen and KFR

## Library Roles

**Eigen** (linear algebra) and **KFR** (digital signal processing) are chosen to implement signal processing and correction without introducing heavy binary dependencies and with good performance. The implementation plan (`implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`) recommends **KFR + Eigen** as the preferred modern approach; **FFTW + Eigen** is the traditional alternative.

## Why Eigen

### Purpose

- **Matrix operations**: Linear systems, SVD, least-squares. Used for Savitzky–Golay convolution matrices (polynomial design matrix over sliding window), RBF interpolation systems (shared with signal mapping), and calibration parameter estimation (least-squares from reference point pairs).
- **Header-only**: No separate build or link step; easy integration into the native C++ project. Already used in the build (e.g. synchronization, transformation).
- **Performance**: Template-based, SIMD-friendly; well-suited for small to medium matrices (e.g. Savitzky–Golay window, RBF kernel matrix).
- **Adoption**: Widely used in scientific and ML code (TensorFlow, PyTorch, robotics); well-documented and maintained.

### Use in This Framework

- **Savitzky–Golay**: Build the convolution coefficient matrix from the polynomial least-squares problem over the window; apply via matrix-vector product or explicit convolution. Eigen solves the normal equations or uses QR/SVD as needed.
- **RBF**: Assemble the RBF kernel matrix and solve the linear system for interpolation weights (shared with signal mapping). Eigen provides the solver (e.g. ColPivHouseholderQR).
- **Calibration**: Fit calibration parameters (e.g. scale, rotation, translation) from reference point pairs; Eigen for the design matrix and least-squares solution.

## Why KFR

### Purpose

- **FFT**: Fast Fourier Transform (forward and inverse). Used for frequency-domain filtering (lowpass, highpass, bandpass) when processing 1D or time-series signals.
- **Filters**: FIR/IIR filter design and application (e.g. lowpass, bandpass); convolution. Can replace or complement hand-written or FFTW-based implementations.
- **Header-only (optional)**: KFR can be used as header-only; SIMD-optimized (SSE, AVX, NEON). Often competitive with or faster than FFTW for many sizes.
- **Modern C++**: Template-based, no global state; fits well with the rest of the native codebase.

### Use in This Framework

- **FFT / iFFT**: Implement `SignalProcessing::fft`, `ifft` in C++ using KFR’s FFT (when KFR is enabled in the build). Used for frequency-domain filtering.
- **Frequency filter**: Implement `frequencyFilter` (lowpass, highpass, bandpass) using FFT → mask/gain in frequency domain → iFFT.
- **Status**: KFR is present in `third_party/kfr` and documented in `docs/Infrastructure/third-party/kfr.md`; the build currently has KFR disabled. The paper describes the *intended* use and rationale; enabling KFR is a build/config step.

## KFR + Eigen vs FFTW + Eigen

| Aspect | KFR + Eigen | FFTW + Eigen |
|--------|-------------|--------------|
| FFT | KFR (header-only or linked) | FFTW (binary library) |
| Filters | KFR (FIR/IIR, convolution) | Hand-written or other libs |
| Matrix ops | Eigen | Eigen |
| Build | No FFTW dependency if KFR used | Requires FFTW install |
| Performance | SIMD-optimized, often faster | Industry standard, very fast |

The implementation plan recommends **KFR + Eigen** for a modern, header-only-friendly stack with a single DSP library (KFR) for both FFT and filters. Eigen remains the choice for all linear algebra (Savitzky–Golay, RBF, calibration) regardless of FFT backend.

## Summary

- **Eigen**: Used for Savitzky–Golay, RBF systems, and calibration fits; header-only, already in use.
- **KFR**: Intended for FFT and frequency-domain filtering (and optionally FIR/IIR filters); available in third_party, enable in build for full FFT/filter pipeline.
- Together they cover noise reduction (smoothing, FFT filter), calibration (Eigen for parameter estimation), and geometric correction (Eigen for distortion model solves), providing a consistent foundation for Paper 0.5 without duplicating the mapping algorithms of Paper 1.
