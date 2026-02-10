# Introduction

## Problem Statement

PBF-LB/M additive manufacturing generates data from multiple sources that must be combined for process understanding, quality assessment, and anomaly detection:

- **Hatching paths**: Build platform coordinates, layer-based time reference
- **Laser parameters**: Machine coordinates, real-time timestamps
- **ISPM monitoring**: Sensor-specific coordinates (thermal, optical, strain, etc.), sensor timestamps
- **CT scans**: CT scanner coordinates, scan time

Each source has a **different coordinate system** and **different time reference**. Without alignment we cannot:

- Compare data from different sources at the same spatial location
- Fuse signals from multiple sources into a single representation
- Create meaningful quality assessments that combine process and quality data
- Map signals to a unified voxel grid in a consistent way

**The core requirement**: Alignment—both spatial and temporal—must be performed **before** any analysis. Downstream components (signal mapping, fusion, quality assessment) assume that "same location" and "same layer" are well-defined across all sources. Paper 1 (signal mapping), Paper 2 (analysis), and Paper 3 (industrial application) all build on this foundation.

**Spatial alignment and the correspondence problem**: We do not estimate the transformation from raw point-to-point correspondences across sources. Establishing one-to-one correspondence between two point sets from different data sources (e.g. hatching paths and ISPM or CT) is **challenging and computationally demanding**: there is no shared indexing, and spatial sampling, coverage, and density differ strongly. For a given point in one source, we cannot reliably identify its corresponding point in another. We therefore base spatial alignment on **bounding-box corners** only—a small, well-defined set that avoids the correspondence problem while still determining the transformation when sources share the same physical extent (see Design).

## Motivation

### Why Alignment Before Analysis

1. **Unified coordinate system**: All points must reside in one reference frame (e.g. build platform) so that voxelization and fusion operate on consistent spatial indices.

2. **Consistent time/layer semantics**: Per-layer fusion (e.g. "layer 5: hatching + thermal + strain") and time-window analysis require a single, consistent notion of "same layer" or "same time" across hatching, ISPM, and CT.

3. **Avoiding cascading errors**: Transforming or aligning **after** voxelization (grid-based alignment) introduces resampling artifacts, loss of point precision, and potential misalignment that propagates through all downstream analysis.

4. **Traceability**: Storing transformation matrices and validation results allows reproducibility and audit of how each source was aligned.

### Scope of This Paper

This paper focuses on:

- **Spatial alignment**: Transforming points from each source's coordinate system into a common reference frame using only bounding-box geometry (no point-to-point correspondences).
- **Temporal alignment**: Mapping timestamps to build layers and aligning point/signal data by layer (or time window) so that "same layer" is well-defined across sources.
- **Design rationale**: Why we use a point-first pipeline, bbox-corner correspondence, 24×56 fit selection, Kabsch+Umeyama, and adaptive validation—and why alternatives (grid-based alignment, RANSAC/point matching) are less suitable for this setting.

Implementation details and API are summarized; full design documents are in the repository (`implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`, `Temporal_Alignment_Design.md`, `docs/AM_QADF/05-modules/synchronization.md`).

## Paper Outline

The remainder of this paper is organized as follows. **Related Work** reviews registration and temporal alignment in AM and multi-sensor fusion. **Design** describes the point-first pipeline, spatial alignment (bbox-corner, 24×56, Kabsch+Umeyama, validation), and temporal alignment (layer/time mapping, point temporal alignment). **Why Our Algorithm** compares our approach to grid-based and point-matching alternatives. **Implementation and API** summarizes the C++/Python implementation and main entry points. **Results** presents alignment accuracy, validation behaviour, and performance. **Discussion** and **Conclusion** summarize contributions and limitations.
