# Why Our Algorithm

## Point-First vs Grid-Based Alignment

**Grid-based alignment** (deprecated in our pipeline): Transform or align **after** voxelization by resampling or transforming voxel grids. Problems:

- **Resampling artifacts**: Voxelization then transformation introduces interpolation and sampling errors.
- **Loss of precision**: Point-level coordinates are lost; alignment quality is limited by voxel resolution.
- **Validation ambiguity**: Grid sampling can hide alignment errors or make pass/fail dependent on grid spacing.

**Point-first alignment** (our approach): Transform point coordinates **before** voxelization. Benefits:

- **No resampling**: Points are transformed once; voxelization then operates on already-aligned points.
- **Preserved precision**: Alignment quality is limited by numerical precision and bbox fit, not voxel size.
- **Clear validation**: Validation is on the same 8 bbox corners used for fit selection; pass/fail is consistent.

## Bbox-Corner Only vs Point Matching / RANSAC

**Why not use raw coordinates from different data sources?** We attempted to align sources using their raw point sets. **Finding one-to-one correspondence between two such sets is challenging and computationally intractable.** For a point $\mathbf{x}$ in one source (e.g. a hatching path point), there is no reliable way to identify its corresponding point in another source (e.g. an ISPM or CT sample): the sources have heterogeneous spatial sampling, different coverage, and no shared indexing. Establishing correspondence would require either an exhaustive or heuristic matching step that is ill-posed at scale and sensitive to noise and outliers. We therefore **do not** rely on point-to-point correspondence between raw data; instead we use only the bounding-box corners, which avoid the correspondence problem while still determining the transformation when the same-extent assumption holds.

**Point matching / RANSAC** (alternatives we reject for the above reason): Require corresponding point pairs across sources. In our setting:

- **Correspondence ill-posed**: There is no natural bijection between a hatching point and an ISPM or CT point; density and coverage differ strongly across sources.
- **Computationally demanding**: Matching millions of points across sources is intractable; RANSAC or feature-based methods add parameter sensitivity and still assume that inliers can be identified reliably.
- **Unnecessary when same extent holds**: When sources share the **same bounding-box extent**, the eight corners fully define the relative pose and scale; we do not need arbitrary point correspondences.

**Bbox-corner correspondence** (our approach):

- **Minimal input**: Only 8 corners per source (from bbox); no point-to-point matching step.
- **Robust search**: 24 permutations × 56 triplets cover all plausible corner correspondences and guard against degenerate triplets; we select the fit with smallest max error on all 8 corners.
- **Deterministic**: No RANSAC; quality is evaluated on all 8 corners for each candidate.

## Full Extent by Default

**Subset bbox**: If bbox/transform were computed from a filtered subset (e.g. one layer), the transform would align only that subset; a different layer might have a different apparent extent and a different "best" transform, leading to inconsistency.

**Full extent** (our default): Bboxes and transform are computed from the **full** extent of each source. Optional filters (bbox, layer_range) only limit which points are **returned** or **saved**; the transform is stable and consistent across the full build. This gives a single, reproducible alignment for the whole dataset.

## Validation with best_ref_corners

**Wrong reference order**: If we validated by comparing `T * source_corners` to the **raw** reference corners (wrong permutation), we would compare physically corresponding corners to non-corresponding ones and report large errors even when the fit is correct.

**best_ref_corners** (our approach): Validation uses reference corners **reordered by the best permutation** so that `ref_reordered[i]` corresponds to `source_corners[i]`. Then pass/fail (max error and RMS within tolerance) matches the fit. The design document (`implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`) states this explicitly.

## Adaptive Tolerance (1% of Bbox Extent)

**Fixed tolerance**: A single absolute tolerance (e.g. 1e-3 mm) may be too strict for large parts or too loose for small features.

**Adaptive tolerance** (our approach): `max(0.01 * max_extent, 1e-3, validation_tolerance)` — i.e. 1% of the largest bbox axis, with a minimum and user override. This scales with part size and keeps validation meaningful across different build volumes.

## Summary Comparison Table

| Aspect | Grid-based (old) | Point-first + bbox-corner (ours) |
|--------|------------------|----------------------------------|
| Transform when | After voxelization | Before voxelization |
| Correspondence | RANSAC / point matching | Bbox corners only (24×56 fits) |
| Bbox for transform | From queried subset | Full data by default |
| Validation | Same points as fit or raw order | best_ref_corners (reordered by best perm) |
| Pass/fail | Could be inconsistent | Valid when max_error and rms_error ≤ tolerance |
| Tolerance | Fixed or 0.5% | 1% of max extent (adaptive) |

This table appears in full in `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md` (Comparison: Old vs New).
