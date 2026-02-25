# Conclusion

## Summary of Contributions

This paper established **spatial and temporal synchronization** as the foundation that must be performed **before** any downstream analysis of multi-source PBF-LB/M data. Without alignment, "same location" and "same layer" are ill-defined across hatching, laser, ISPM, and CT; fusion, signal mapping, and quality assessment (Papers 3–5) all depend on this foundation.

### 1. Point-First Pipeline

We argued for and implemented a **point-first** pipeline: transform point coordinates **before** voxelization. This avoids grid resampling artifacts, preserves point-level precision, and makes validation consistent. The pipeline is documented in the repository (`implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`, `Synchronization_Reorganize_Plan.md`).

### 2. Spatial Alignment: Bbox-Corner Correspondence

We use **bounding-box corner correspondence** only (no point-to-point matching). For each source we compute an 8-corner bbox (from full data by default), try 24 rotational permutations and 56 triplets per permutation, fit a similarity transform (Kabsch + Umeyama) on 3 corners, evaluate quality on all 8 corners, and select the fit with smallest max error. Validation uses **best_ref_corners** (reordered by the best permutation) and an **adaptive tolerance** (1% of bbox extent) so that pass/fail matches the fit. This design is robust, deterministic, and avoids RANSAC and point-matching complexity.

### 3. Temporal Alignment

We provided explicit **layer/time mapping** and **point temporal alignment** so that "same layer" or "same time window" is well-defined across sources. Point-based temporal alignment operates on points and signals before voxelization, avoiding grid resampling and preserving accuracy. Design and placement in the pipeline are in `implementation_plan/new/Temporal_Alignment_Design.md`.

### 4. Why Our Algorithm

We compared our approach to grid-based alignment and RANSAC/point matching. Point-first avoids resampling; bbox-corner-only avoids correspondence search; full extent by default gives stable transforms; best_ref_corners and adaptive tolerance give consistent validation. A comparison table (old vs new) is in the design document.

### 5. Implementation and API

The pipeline is implemented in C++ (am_qadf_native) with Python bindings. The main entry point is **UnifiedQueryClient.query_and_transform_points**, which returns transformed points, signals, unified bounds, transformation metadata, and validation results. Full API and design details are in `docs/AM_QADF/06-api-reference/synchronization-api.md` and the implementation_plan documents.

## Impact

- **Foundation for Papers 3–5**: Signal mapping (Paper 3), analysis (Paper 4), and industrial application (Paper 5) assume spatially and temporally aligned data; this paper defines and justifies that alignment step.
- **Reproducibility**: Transformation matrices and validation results are returned and can be stored for audit and replay.
- **Design transparency**: All design and algorithm rationale are documented in the repository so that reviewers and users can verify the "why" before relying on the "how."

## Closing Remark

Spatial and temporal synchronization is not an afterthought but a **prerequisite** for multi-source PBF-LB/M analysis. This paper presented the design, rationale, and implementation of a point-first, bbox-corner alignment pipeline with robust validation and optional temporal alignment, establishing the basis for the rest of the AM-QADF framework.
