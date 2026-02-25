# Publication Narrative: PBF-LB/M Data Warehouse with Signal Mapping

## 📖 Research Story

### The Problem

Powder Bed Fusion - Laser Beam/Metal (PBF-LB/M) additive manufacturing generates **massive, heterogeneous, multi-source datasets** that are challenging to integrate and analyze:

- **Hatching paths**: Hundreds of thousands of scan path points
- **Laser parameters**: Real-time process measurements (power, speed, energy density)
- **ISPM monitoring**: In-situ temperature and process monitoring data
- **CT scans**: 3D defect imaging with millions of voxels
- **STL models**: Geometric CAD data

Each data source has:
- **Different coordinate systems** (build platform, CT scanner, ISPM sensor)
- **Different temporal resolutions** (real-time vs. layer-based vs. post-build)
- **Different spatial resolutions** (point-based vs. voxel-based)
- **Different data formats** (structured vs. unstructured)

**The Challenge**: How to create a **unified, queryable, analyzable representation** that enables:
- Multi-source data fusion
- Spatial-temporal analysis
- Quality assessment
- Anomaly detection
- Sensitivity analysis
- Virtual experiments

### The Solution: Signal Mapping to Voxel Domain

**Signal mapping** is the core innovation that transforms heterogeneous point-based data from multiple sources into a **unified 3D voxel domain representation**.

#### Key Innovation

**Signal mapping** enables:
1. **Coordinate System Unification**: All data sources transformed to a common reference frame
2. **Spatial-Temporal Alignment**: Data synchronized across time (layers) and space (coordinates)
3. **Variable Resolution**: Support for uniform, adaptive, and multi-resolution voxel grids
4. **Multi-Signal Integration**: Multiple signals coexist in the same voxel structure
5. **Data Volume Reduction**: Point clouds reduced to structured voxel grids

### The Framework

We developed a comprehensive **NoSQL data warehouse framework** with:

#### 1. Data Warehouse Layer
- **MongoDB**: Document store for flexible PBF process data
- **GridFS**: Large file storage for CT voxel arrays and voxel grids
- **Multi-source query clients**: STL, Hatching, Laser, CT, ISPM
- **Unified query interface**: Spatial, temporal, and parameter-based queries

#### 2. Signal Mapping Engine ⭐ **CORE**
- **Coordinate system transformation**: Automatic alignment of all data sources
- **Voxel grid generation**: Uniform, adaptive, and multi-resolution grids
- **Signal interpolation**: Nearest neighbor, linear, inverse distance weighted
- **Data synchronization**: Temporal (layer/time) and spatial (coordinate) alignment
- **Noise and distortion handling**: Quality-based filtering and correction

#### 3. Analysis and Evaluation Layer
- **Quality Assessment**: Completeness, SNR, alignment accuracy, coverage metrics
- **Statistical Analysis**: Descriptive, correlation, trends, pattern recognition
- **Data Fusion**: Multi-signal fusion with quality-based weighting
- **Anomaly Detection**: 8+ methods (statistical, clustering, ML-based)
- **Sensitivity Analysis**: 12 methods (Sobol, Morris, FAST, RBD, Delta, PAWN, DGSM, Local, MC, Bayesian)
- **Virtual Experiments**: 10 design types (LHS, Factorial, Response Surface, Optimal designs)

#### 4. Visualization and Interaction
- **Interactive Jupyter notebooks**: 7 comprehensive notebooks with widget-based interfaces
- **3D visualization**: PyVista-based voxel visualization
- **Real-time analysis**: Interactive parameter adjustment and result visualization

### Key Contributions

1. **Signal Mapping Framework**
   - First comprehensive framework for multi-source PBF-LB/M data integration via voxel domain
   - Handles coordinate system transformations, temporal/spatial synchronization, and noise reduction
   - Enables variable resolution voxel grids for efficient data representation

2. **NoSQL Data Warehouse Architecture**
   - Extension of existing NoSQL backend to full data warehouse
   - Integration of ISPM and CT datasets with existing process data
   - Multi-model storage optimized for different data types

3. **Comprehensive Analysis Capabilities**
   - 12 sensitivity analysis methods integrated with warehouse data
   - 10 virtual experiment design types
   - 8+ anomaly detection methods
   - Multi-signal fusion with quality-based weighting

4. **Interactive Analysis Framework**
   - 7 interactive Jupyter notebooks covering all analysis workflows
   - Widget-based interfaces for non-programmers
   - Real-time visualization and parameter adjustment

### Research Impact

#### Scientific Contributions
- **Novel approach** to multi-source AM data integration
- **Unified representation** enabling new analysis capabilities
- **Framework** applicable to other AM processes and multi-source data scenarios

#### Practical Impact
- **Reduced data volume**: Point clouds → structured voxel grids
- **Unified analysis**: All data sources in same representation
- **Quality control**: Comprehensive quality assessment framework
- **Process optimization**: Sensitivity analysis and virtual experiments
- **Anomaly detection**: Early detection of process issues

#### Methodological Contributions
- **Signal mapping algorithms**: Novel interpolation and aggregation methods
- **Coordinate system transformation**: Automatic alignment framework
- **Quality-based fusion**: Quality-weighted multi-signal combination
- **Variable resolution**: Adaptive grids based on data density

### Publication Structure

Papers are ordered so that **alignment and synchronization (Paper 1)** come first: they define why transformation must happen *before* any analysis, and why our algorithms are chosen. Design details and algorithm rationale are documented in the repository (see references below).

#### Paper 1: Spatial and Temporal Synchronization (Foundation)

**Focus**: Transformation, spatial alignment, and temporal synchronization of multi-source PBF-LB/M data. This paper establishes that **alignment must be done before analysis** and presents the design and rationale for our algorithms.

**Why this comes first**: Without a common coordinate system and consistent time/layer reference, fusion, signal mapping, and quality assessment are ill-defined. Paper 1 explains the problem, the point-first pipeline (transform points then voxelize), and why our approach is preferable to alternatives (e.g. grid-based alignment, RANSAC/point matching).

**Design and algorithm rationale (where to read more)**:
- **Spatial alignment**: Point-first, bounding-box corner correspondence only (no point-to-point correspondences). We try 24 rotational permutations × 56 triplets per permutation; fit a similarity transform (Kabsch + Umeyama) on 3 corners and validate on all 8; select best fit; validate with adaptive tolerance (1% of bbox extent). This avoids RANSAC, avoids grid resampling, and uses full extent by default for a stable transform.
- **Temporal alignment**: Layer/time mapping and point-based temporal alignment so that “same layer” or “same time window” is well-defined across hatching, ISPM, CT, etc., before voxelization or fusion.
- **Design docs** (in repository):
  - `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md` — full spatial alignment design (bbox-corner, 24×56, Kabsch+Umeyama, validation, comparison old vs new).
  - `implementation_plan/new/Temporal_Alignment_Design.md` — temporal alignment purpose, pipeline position, point-first rationale.
  - `implementation_plan/new/Synchronization_Reorganize_Plan.md` — point vs grid pipeline, naming, pipeline view.
  - `docs/AM_QADF/05-modules/synchronization.md` — module overview and workflow.
  - `docs/AM_QADF/06-api-reference/synchronization-api.md` — API (e.g. `query_and_transform_points`).

**Suggested outline for Paper 1**:
1. Introduction (multi-source coordinate and time mismatch; need for alignment before analysis)
2. Related work (registration, temporal alignment in AM)
3. Design (point-first pipeline; spatial: bbox-corner correspondence, 24×56 fits, Kabsch+Umeyama, validation; temporal: layer/time mapping, point temporal alignment)
4. Why our algorithm (comparison with grid-based alignment and point-matching; full extent, adaptive tolerance, best_ref_corners validation)
5. Implementation and API
6. Results (accuracy, robustness, performance)
7. Conclusion

#### Paper 2: Signal Processing and Correction (Foundation for Mapping)

**Focus**: Signal processing (noise reduction, filtering, FFT) and correction (calibration, geometric distortion) so that the *values* fed into signal mapping are reliable. This paper sits **between Paper 1 (alignment) and Paper 3 (signal mapping)**.

**Why Paper 2**: Signal mapping (Paper 3) answers *where* to put signal values (interpolation from points to voxels). Signal processing and correction answer *what* values to use: raw signals are noisy and can have systematic errors; we need filtering, noise reduction, calibration, and distortion correction **before** (or alongside) mapping. Paper 3 already states that calibration and correction are prerequisites; Paper 2 dedicates a full paper to their **design, algorithms, and implementation**, including the rationale for **Eigen** (linear algebra: Savitzky–Golay, RBF, calibration) and **KFR** (FFT, filters).

**Scope**: Noise reduction (outlier detection, Gaussian, Savitzky–Golay, moving average, FFT/frequency filtering); calibration (reference-based, CalibrationManager); geometric correction (scaling, rotation, warping, validation); pipeline position (pre-mapping default, optional post-mapping/pre-fusion/post-fusion); Eigen and KFR integration.

**Design docs (in repo)**: `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`; `docs/AM_QADF/05-modules/processing.md`, `correction.md`; `docs/Infrastructure/third-party/eigen.md`, `kfr.md`.

**Suggested outline for Paper 2**:
1. Introduction (why process/correct before mapping; pipeline: align → process/correct → map)
2. Related work (noise reduction, calibration, correction in AM; Eigen/KFR in scientific code)
3. Noise reduction and filtering (outlier detection, smoothing, FFT/frequency filtering)
4. Calibration and geometric correction (reference-based calibration, distortion models, validation, multi-stage application)
5. Implementation: Eigen and KFR (rationale, integration, build status)
6. Results (quality metrics, calibration/correction validation, performance)
7. Conclusion

#### Suggested Paper Outline (Framework overview)

1. **Introduction**
   - PBF-LB/M data challenges
   - Need for unified representation
   - Signal mapping as solution (building on aligned data from Paper 1)

2. **Related Work**
   - AM data management systems
   - Multi-source data fusion
   - Voxel-based representations

3. **Methodology**
   - Signal mapping framework (assumes spatially and temporally aligned points from Paper 1, and optionally processed/corrected signals from Paper 2)
   - Coordinate system transformation (see Paper 1)
   - Voxel grid generation
   - Data synchronization algorithms (see Paper 1)
   - Calibration and correction as prerequisites (see Paper 2 for design and algorithms)

4. **System Architecture**
   - NoSQL data warehouse
   - Query clients
   - Analysis framework
   - Visualization tools

5. **Results**
   - Signal mapping performance
   - Data volume reduction
   - Analysis capabilities demonstration
   - Case studies

6. **Discussion**
   - Framework advantages
   - Limitations
   - Future work

7. **Conclusion**
   - Summary of contributions
   - Impact and applications

### Target Venues

#### Journal Papers
1. **Paper 1 (Foundation)** — Spatial and temporal synchronization
   - Focus: Transformation, spatial and temporal alignment of multi-source PBF-LB/M data; design and rationale (point-first, bbox-corner, 24×56 fits, Kabsch+Umeyama, validation). Design details: `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`, `Temporal_Alignment_Design.md`; `docs/AM_QADF/05-modules/synchronization.md`.

2. **Paper 2 (Foundation)** — Signal processing and correction
   - Focus: Noise reduction, calibration, geometric correction; Eigen and KFR; pre-mapping quality. Design: `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`; `docs/AM_QADF/05-modules/processing.md`, `correction.md`.

3. **Additive Manufacturing** (Elsevier)
   - Focus: Signal mapping for AM data integration
   - Title: "Signal Mapping Framework for Multi-Source PBF-LB/M Data Integration in a Unified Voxel Domain"

4. **Journal of Manufacturing Systems** (Elsevier)
   - Focus: Data warehouse architecture and analysis framework
   - Title: "NoSQL Data Warehouse for PBF-LB/M Process Chain: Architecture and Analysis Capabilities"

5. **Computers in Industry** (Elsevier)
   - Focus: Industrial application and practical impact
   - Title: "A Comprehensive Data Analysis Framework for Temporal and Spatial Segmentation of PBF-LB/M Process Data"

#### Conference Papers
1. **International Conference on Additive Manufacturing (ICAM)**
   - Focus: Signal mapping and voxel domain representation

2. **International Manufacturing Science and Engineering Conference (MSEC)**
   - Focus: Data warehouse architecture and analysis capabilities

3. **International Conference on Advanced Manufacturing (ICAM)**
   - Focus: Multi-source data fusion and quality assessment

### Key Figures and Tables

#### Essential Figures
1. **System Architecture Diagram** (Complete System Architecture flowchart)
2. **Signal Mapping Process** (Detailed Signal Mapping Process flowchart)
3. **Multi-Source Integration** (Multi-Source Integration Flow flowchart)
4. **Analysis Capabilities** (Overview Flowchart with all methods)
5. **Case Study Results** (Example analyses from notebooks)

#### Essential Tables
1. **Data Sources and Characteristics**
2. **Signal Mapping Methods Comparison**
3. **Analysis Methods Summary** (12 sensitivity, 10 experiment designs, 8+ anomaly)
4. **Performance Metrics** (Data volume reduction, query performance)
5. **Quality Metrics Results**

### Data Availability

- **Code**: Open-source framework (GitHub repository)
- **Notebooks**: 7 interactive Jupyter notebooks
- **Documentation**: Comprehensive documentation and flowcharts
- **Demo Data**: Synthetic data generation scripts

### Acknowledgments

- Project partners from science and industry
- MPM system providers
- Research collaborators

---

## 📝 Publication Checklist

### Paper 1: Spatial and Temporal Synchronization (Foundation)
- [ ] Abstract (250 words)
- [ ] Introduction (Multi-source coordinate/time mismatch; alignment before analysis)
- [ ] Related Work (Registration, temporal alignment in AM)
- [ ] Design (Point-first pipeline; spatial bbox-corner, 24×56, Kabsch+Umeyama; temporal layer/time)
- [ ] Why our algorithm (Comparison with grid-based and point-matching; validation, tolerance)
- [ ] Implementation and API
- [ ] Results (Accuracy, robustness, performance)
- [ ] Conclusion
- [ ] References
- [ ] Figures (Pipeline, bbox-corner, validation)
- [ ] Tables (Old vs new alignment; quality metrics)

**Design docs (in repo)**: `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`, `Temporal_Alignment_Design.md`, `Synchronization_Reorganize_Plan.md`; `docs/AM_QADF/05-modules/synchronization.md`, `06-api-reference/synchronization-api.md`.

### Paper 2: Signal Processing and Correction (Foundation for Mapping)
- [ ] Abstract
- [ ] Introduction (why process/correct before mapping; pipeline position)
- [ ] Related Work (noise reduction, calibration, Eigen/KFR)
- [ ] Noise reduction and filtering (outlier, smoothing, FFT)
- [ ] Calibration and geometric correction (reference-based, distortion models, validation)
- [ ] Implementation: Eigen and KFR
- [ ] Results (quality metrics, validation, performance)
- [ ] Conclusion
- [ ] References, Figures, Tables

**Design docs (in repo)**: `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`; `docs/AM_QADF/05-modules/processing.md`, `correction.md`; `docs/Infrastructure/third-party/eigen.md`, `kfr.md`.

### Paper 3: Signal Mapping Framework (Primary Contribution)
- [ ] Abstract (250 words)
- [ ] Introduction (Problem statement, motivation)
- [ ] Related Work (Literature review)
- [ ] Methodology (Signal mapping algorithms; assumes Paper 1 alignment)
- [ ] System Architecture (Data warehouse, clients)
- [ ] Results (Case studies, performance)
- [ ] Discussion (Advantages, limitations)
- [ ] Conclusion
- [ ] References
- [ ] Figures (6 flowcharts + case study results)
- [ ] Tables (Methods comparison, performance metrics)

### Paper 4: Analysis Framework (Secondary Contribution)
- [ ] Abstract
- [ ] Introduction
- [ ] Analysis Capabilities (12 sensitivity methods, 10 experiment designs)
- [ ] Integration with Warehouse
- [ ] Case Studies
- [ ] Results
- [ ] Discussion
- [ ] Conclusion

### Paper 5: Industrial Application (Application Paper)
- [ ] Abstract
- [ ] Industrial Context
- [ ] Framework Application
- [ ] Results and Impact
- [ ] Lessons Learned
- [ ] Conclusion

---

**Last Updated**: 2025-01-01  
**Status**: Ready for Publication Development


