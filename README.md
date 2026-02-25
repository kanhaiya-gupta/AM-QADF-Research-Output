# AM-QADF Publications Repository

**Private Git Repository for Research Publications and Documentation**

This repository contains all research publications, posters, and supporting documentation for the AM-QADF (Additive Manufacturing Quality Assessment and Data Fusion) framework project.

## 📋 Repository Overview

This is a **private Git repository** dedicated to managing research publications, including:
- **Research Papers** (Paper1, Paper2, Paper3, Paper4, Paper5)
- **Conference Posters** (Poster1, Poster2, Poster3)
- **Supporting Documentation** (flowcharts, narratives, planning documents)
- **Narrative Explanations** (detailed module descriptions for supervisor presentations)

## 📁 Repository Structure

```
publications/
├── Paper1/              # Spatial and Temporal Synchronization (Foundation)
├── Paper2/              # Signal Processing and Correction (Foundation for Mapping)
├── Paper3/              # Signal Mapping Framework Paper
├── Paper4/              # Analysis Capabilities Paper
├── Paper5/              # Framework Application Paper
├── Poster1/             # Signal Mapping Framework Poster
├── Poster2/             # Analysis Capabilities Poster
├── Poster3/             # Framework Application Poster
├── flowchart_images/     # Mermaid diagrams and PNG images
├── plots/               # Generated plots and figures
├── Publication_Narrative.md  # Overall research narrative
└── Poster_Planning.md   # Poster planning and design notes
```

## 📄 Papers

### Paper 1: Spatial and Temporal Synchronization (Foundation)
**Focus**: Transformation, spatial alignment, and temporal synchronization of multi-source PBF-LB/M data. This paper establishes **why alignment must be done before any analysis** and presents the design and rationale for our algorithms (point-first pipeline, bbox-corner correspondence, 24×56 fits, Kabsch+Umeyama, validation, temporal layer/time alignment).

**Design and algorithm rationale** — full design docs live in the main repository:
- **`implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`** — spatial alignment (bbox-corner, 24×56, Kabsch+Umeyama, validation, old vs new comparison)
- **`implementation_plan/new/Temporal_Alignment_Design.md`** — temporal alignment (point-first, layer/time, pipeline position)
- **`implementation_plan/new/Synchronization_Reorganize_Plan.md`** — point vs grid pipeline, naming
- **`docs/AM_QADF/05-modules/synchronization.md`** — module overview and workflow
- **`docs/AM_QADF/06-api-reference/synchronization-api.md`** — API (e.g. `query_and_transform_points`)

**Location**: [`Paper1/`](Paper1/)

### Paper 2: Signal Processing and Correction (Foundation for Mapping)
**Focus**: Signal processing (noise reduction, filtering, FFT) and correction (calibration, geometric distortion) so that the *values* fed into signal mapping are reliable. Sits between Paper 1 (alignment) and Paper 3 (signal mapping). Covers rationale for **Eigen** (linear algebra: Savitzky–Golay, RBF, calibration) and **KFR** (FFT, filters).

**Design docs (main repo)**: `implementation_plan/new/SIGNAL_PROCESSING_LIBRARIES.md`; `docs/AM_QADF/05-modules/processing.md`, `correction.md`; `docs/Infrastructure/third-party/eigen.md`, `kfr.md`.

**Location**: [`Paper2/`](Paper2/)

### Paper 3: Signal Mapping Framework
**Title**: Unified Voxel Domain Signal Mapping for Multi-Source PBF-LB/M Process Data  
**Target Venue**: Additive Manufacturing (Elsevier)  
**Status**: ✅ Complete - Ready for Review

**Key Contributions:**
- Signal Mapping Framework for multi-source PBF-LB/M data integration
- NoSQL Data Warehouse Architecture
- Quality Assessment Module (see `quality-assessment.md`)
- Data Fusion Module (see `data-fusion.md`)

**Location**: [`Paper3/`](Paper3/)

**Key Files:**
- `quality-assessment.md` - Comprehensive narrative on quality assessment module
- `data-fusion.md` - Comprehensive narrative on data fusion module
- `README.md` - Paper structure and organization

### Paper 4: Analysis Capabilities
**Focus**: Advanced analytics, statistical analysis, and process optimization capabilities

**Location**: [`Paper4/`](Paper4/)

### Paper 5: Framework Application
**Focus**: Industrial deployment, case studies, and real-world applications

**Location**: [`Paper5/`](Paper5/)

## 🎨 Posters

### Poster 1: Signal Mapping Framework
**Focus**: Core signal mapping innovation and framework architecture

**Location**: [`Poster1/`](Poster1/)

### Poster 2: Analysis Capabilities
**Focus**: Analytics tools and interactive capabilities

**Location**: [`Poster2/`](Poster2/)

### Poster 3: Framework Application
**Focus**: Industrial context and business value

**Location**: [`Poster3/`](Poster3/)

## 📊 Supporting Materials

### Flowchart Images
**Location**: [`flowchart_images/`](flowchart_images/)

Contains Mermaid source files (`.mmd`) and generated PNG images for:
- System architecture diagrams
- Signal mapping process flowcharts
- Decision trees for method selection
- Multi-source integration flows

### Plots
**Location**: [`plots/`](plots/)

Generated plots and figures for papers and posters.

### Documentation

- **`Publication_Narrative.md`**: Overall research narrative explaining the problem, solution, and framework
- **`Poster_Planning.md`**: Planning and design notes for posters

## 🔧 Module Narratives

Detailed narrative explanations for supervisor presentations:

- **`Paper1/quality-assessment.md`**: Comprehensive explanation of the Quality Assessment Module
- **`Paper1/data-fusion.md`**: Comprehensive explanation of the Data Fusion Module

These narratives explain:
- The problem each module solves
- What was built and how it works
- Real-world examples and use cases
- Technical achievements
- Integration with other modules

## 🚀 Getting Started

### For Authors

1. **Navigate to specific paper/poster**: Each has its own README.md with structure
2. **Edit markdown files**: All content is in Markdown format
3. **Update flowcharts**: Edit `.mmd` files in `flowchart_images/` and regenerate PNGs
4. **Commit changes**: Use descriptive commit messages

### For Reviewers

1. **Start with Paper3/README.md**: Overview of paper structure
2. **Review sections in order**: Abstract → Introduction → Methodology → Results
3. **Check narrative files**: `quality-assessment.md` and `data-fusion.md` for detailed explanations
4. **Review flowcharts**: Visual representations in `flowchart_images/`

## 📝 Git Workflow

### Initial Setup

This repository has been initialized as a private Git repository:

```bash
cd publications/
git init
```

### Recommended Workflow

1. **Create feature branches** for major edits:
   ```bash
   git checkout -b feature/paper1-quality-section
   ```

2. **Commit frequently** with descriptive messages:
   ```bash
   git add Paper3/quality-assessment.md
   git commit -m "Add comprehensive quality assessment narrative"
   ```

3. **Use meaningful commit messages**:
   - `Add: [description]` - New content
   - `Update: [description]` - Content updates
   - `Fix: [description]` - Bug fixes or corrections
   - `Refactor: [description]` - Reorganization

4. **Tag releases** for paper submissions:
   ```bash
   git tag -a v1.0-paper3-submission -m "Paper 3 submission version"
   ```

## 🔒 Privacy and Access

This is a **private repository** containing:
- Research publications in progress
- Detailed technical narratives
- Planning documents
- Supporting materials

**Do not make this repository public** without removing sensitive information.

## 📚 Related Repositories

- **Main AM-QADF Repository**: Contains source code, notebooks, and implementation
- **This Publications Repository**: Contains only publications and documentation

## 🤝 Contributing

### Adding New Content

1. **New paper section**: Add markdown file in appropriate paper folder
2. **New flowchart**: Add `.mmd` file to `flowchart_images/` and generate PNG
3. **New narrative**: Add markdown file with comprehensive explanation
4. **Update README**: Update this file when adding major new content

### File Naming Conventions

- **Papers**: Use descriptive names (e.g., `Introduction.md`, `Methodology.md`)
- **Narratives**: Use kebab-case (e.g., `quality-assessment.md`, `data-fusion.md`)
- **Flowcharts**: Use descriptive names (e.g., `signal_mapping_process.mmd`)

## 📖 Documentation Standards

All markdown files should:
- Use clear headings and structure
- Include real-world examples where applicable
- Reference related sections and files
- Maintain consistent formatting
- Include code blocks with syntax highlighting when needed

## 🔍 Quick Navigation

- **Paper 1 Overview**: [`Paper1/README.md`](Paper1/README.md) — synchronization/transformation; design docs in main repo `implementation_plan/new/` and `docs/AM_QADF/`
- **Paper 2 Overview**: [`Paper2/README.md`](Paper2/README.md) — signal processing and correction; Eigen and KFR; design docs in main repo `implementation_plan/new/`, `docs/AM_QADF/`, `docs/Infrastructure/third-party/`
- **Paper 3 Overview**: [`Paper3/README.md`](Paper3/README.md)
- **Quality Assessment Narrative**: [`Paper3/quality-assessment.md`](Paper3/quality-assessment.md)
- **Data Fusion Narrative**: [`Paper3/data-fusion.md`](Paper3/data-fusion.md)
- **Research Narrative**: [`Publication_Narrative.md`](Publication_Narrative.md)
- **Flowchart Images**: [`flowchart_images/`](flowchart_images/)

## 📧 Contact

For questions about this repository or publications:
- Review individual paper README files for paper-specific information
- Check narrative files for detailed module explanations
- Refer to main AM-QADF repository for implementation details

---

**Last Updated**: 2024  
**Repository Type**: Private Git Repository  
**Purpose**: Research Publications and Documentation Management
