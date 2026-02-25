# Related Work

## Registration and Coordinate Transformation in AM

Additive manufacturing process chains combine build data (hatching, laser), in-situ monitoring (ISPM), and post-build inspection (CT). Each modality typically uses a different coordinate system. Prior work on AM data integration often assumes known transformation parameters from calibration or fixture design, or applies generic point-cloud registration (ICP, feature-based) that may be brittle when point densities and coverage differ strongly across sources. Our setting assumes **same physical extent** (same bounding box in different frames) but **unknown correspondence** of box orientation; we therefore use bbox corners only and search over rotational permutations and triplets to find the best similarity transform, without requiring point-to-point matches or RANSAC.

## Temporal Alignment in Multi-Source Process Data

Layer-based build data (hatching) and time-series sensor data (ISPM, laser) must be aligned so that "same layer" or "same time window" is well-defined. Prior work maps timestamps to layers via build logs or heuristics. We adopt an explicit **layer/time mapping** (e.g. `LayerTimeMapper`) and **point temporal alignment** that operates on points and signals before voxelization, avoiding grid resampling and preserving point-level accuracy. This is consistent with a point-first pipeline where temporal alignment is an optional step after spatial transformation.

## Grid-Based vs Point-First Alignment

Some frameworks align data **after** voxelization by resampling or transforming voxel grids. That approach can introduce resampling artifacts, loss of precision, and validation ambiguity (grid sampling may hide alignment errors). We argue for **point-first** alignment: transform points, then voxelize. Design documents in the repository (e.g. `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`) compare the old grid-based approach with the current point-first + bbox-corner approach in a dedicated table (transform when, correspondence, bbox for transform, validation, tolerance).

## Similarity Transform and Quality Metrics

We use **Kabsch** (optimal rotation between centered point sets via SVD of cross-covariance) and **Umeyama** (uniform scale and translation given rotation) to fit a 3D similarity transform from minimal point sets. Quality is evaluated on **all 8** bbox corners (max error, mean error, RMS); the candidate with smallest max error is selected. Validation uses the **best_ref_corners** (reference corners reordered by the best permutation) and an **adaptive tolerance** (1% of bbox extent) so that pass/fail is consistent with the fit. This avoids the pitfall of validating against the wrong corner order and reporting spurious large errors.

## Summary

Related work covers registration, temporal alignment, and grid vs point alignment. Our contribution is a **point-first synchronization design** with **bbox-corner-only** spatial alignment (24×56 fits, Kabsch+Umeyama, best_ref_corners validation) and explicit **point temporal alignment**, documented in full in the repository and summarized in the following sections.
