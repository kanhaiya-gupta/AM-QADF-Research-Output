# Figures

## Required Figures

1. **Figure 1: Pipeline Position (Paper 0 → Paper 0.5 → Paper 1)**
   - **Location**: Design.md (embedded Mermaid)
   - **Description**: Flowchart showing alignment (Paper 0) → processing and correction (Paper 0.5) → signal mapping (Paper 1). Processing step includes outlier detection, smoothing, optional FFT, calibration, geometric correction.
   - **Purpose**: Illustrates where signal processing and correction sit in the overall framework.

2. **Figure 2: Noise Reduction Sub-Pipeline**
   - **Location**: Design.md (embedded Mermaid)
   - **Description**: Raw signal → outlier detection → clean → smooth (Gaussian / Savitzky–Golay / MA) → optional FFT filter → processed signal.
   - **Purpose**: Details the noise-reduction workflow.

3. **Figure 3: Correction Workflow**
   - **Location**: Design.md (embedded Mermaid)
   - **Description**: Distorted data → identify distortion → select model (scaling / rotation / warping) → estimate parameters → apply correction → validate → accept or refine.
   - **Purpose**: Shows calibration and geometric correction workflow.

4. **Figure 4: SNR Before and After Processing (Example)**
   - **Description**: (To be generated.) Bar chart or table: SNR (dB) for raw vs Gaussian vs Savitzky–Golay vs moving average for one or more representative signals.
   - **Purpose**: Supports Results section (noise reduction effectiveness).

5. **Figure 5: Calibration Error (Example)**
   - **Description**: (To be generated.) Mean/max/RMS error (mm) before and after calibration for a representative calibration set.
   - **Purpose**: Supports Results section (calibration validation).

6. **Figure 6: Eigen and KFR in the Stack**
   - **Description**: Schematic: Input signal → Eigen (Savitzky–Golay, RBF, calibration) + KFR (FFT, filters) → processed/corrected signal. Optional diagram showing which component uses which library.
   - **Purpose**: Supports Why Eigen and KFR section.

## Optional Figures

7. **Figure 7: Application Stages (Pre-Mapping, Post-Mapping, Pre-Fusion, Post-Fusion)**
   - **Description**: Timeline or flowchart showing where calibration/correction can be applied relative to alignment and mapping.
   - **Purpose**: Clarifies flexible application stages.

8. **Figure 8: Savitzky–Golay Window and Polynomial**
   - **Description**: Sketch of sliding window and polynomial fit for one window position.
   - **Purpose**: Supports Design (smoothing) section.

## Figure Captions (Draft)

**Figure 1**: Pipeline position: alignment (Paper 0) → signal processing and correction (Paper 0.5) → signal mapping (Paper 1).

**Figure 2**: Noise reduction sub-pipeline: outlier detection → smoothing → optional FFT filter.

**Figure 3**: Correction workflow: identify distortion, select model, estimate parameters, apply, validate.

**Figure 4**: Example SNR before and after processing (raw, Gaussian, Savitzky–Golay, moving average).

**Figure 5**: Example calibration error (mean, max, RMS) before and after calibration.

**Figure 6**: Role of Eigen (linear algebra) and KFR (FFT, filters) in the processing stack.
