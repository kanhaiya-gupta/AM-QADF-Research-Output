# Tables

## Required Tables

### Table 1: Old vs New Alignment (Grid-Based vs Point-First + Bbox-Corner)

- **Location**: Why Our Algorithm section (or Design)
- **Content**: Comparison of deprecated grid-based approach and current point-first + bbox-corner approach
- **Columns**: Aspect | Old (Grid-Based) | New (Point-First + Bbox-Corner)
- **Rows**:
  - Transform when: After voxelization | Before voxelization
  - Correspondence: RANSAC / point matching | Bbox corners only (24×56 fits)
  - Bbox for transform: From queried subset | Full data by default
  - Validation: Same points as fit or raw order | best_ref_corners (reordered by best perm)
  - Pass/fail: Could be inconsistent | Valid when max_error and rms_error ≤ tolerance
  - Tolerance: Fixed or 0.5% | 1% of max extent (adaptive)

**Source**: Content matches `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md` (Comparison: Old vs New).

### Table 2: Transformation Computation Summary

- **Location**: Design section (Spatial Alignment)
- **Content**: Summary of transformation computation steps
- **Columns**: Step | Description
- **Rows**:
  - Input: source_corners (8×3), reference_corners (8×3)
  - Permutations: 24 rotational permutations of reference corner order
  - Triplets: 56 triplets per permutation (C(8,3))
  - Fit: Similarity transform (Kabsch rotation + Umeyama scale + translation) from 3 source to 3 reordered reference corners
  - Quality: Apply transform to all 8 source corners; compare to ref_reordered; max/mean/RMS error
  - Selection: Choose (permutation, triplet) with smallest max error on 8 corners
  - Output: 4×4 matrix, quality, best_ref_corners, optional per-fit errors

### Table 3: Validation Parameters

- **Location**: Design section (Validation) or Implementation and API
- **Content**: Validation tolerance and pass/fail criteria
- **Columns**: Parameter | Value / Criterion
- **Rows**:
  - Adaptive tolerance: max(0.01 * max_extent, 1e-3, validation_tolerance)
  - Pass (max): max_error ≤ tolerance
  - Pass (RMS): rms_error ≤ tolerance
  - Reference: best_ref_corners (reordered by best permutation)

### Table 4: query_and_transform_points Parameters (Summary)

- **Location**: Implementation and API section
- **Content**: Main parameters of UnifiedQueryClient.query_and_transform_points
- **Columns**: Parameter | Type | Description
- **Rows**: model_id, source_types, reference_source, layer_range, bbox, use_full_extent_for_transform, validation_tolerance, save_processed_data, mongo_uri, db_name (see API doc for full descriptions).

### Table 5: Returned Result Structure (Summary)

- **Location**: Implementation and API section
- **Content**: Keys returned in result dict
- **Columns**: Key | Description
- **Rows**: transformed_points, signals, unified_bounds, transformations, validation_results, raw_results; optional layer_alignment_result, layer_indices.

### Table 6: Alignment Quality Metrics (Example)

- **Location**: Results section
- **Content**: (To be filled with experimental data.) Per-source or aggregate: max_error, mean_error, rms_error, validation pass/fail, runtime (ms).
- **Columns**: Source | Max Error (mm) | Mean Error (mm) | RMS (mm) | Pass | Time (ms)
- **Data**: Placeholder until benchmarks are run.

## Table Captions (Draft)

**Table 1**: Comparison of grid-based (deprecated) and point-first + bbox-corner spatial alignment.

**Table 2**: Steps in transformation computation from bbox corners (24×56 fits, Kabsch+Umeyama, quality on 8 corners).

**Table 3**: Validation tolerance (adaptive 1% of max extent) and pass/fail criteria using best_ref_corners.

**Table 4**: Main parameters of query_and_transform_points.

**Table 5**: Main keys in the result dictionary of query_and_transform_points.

**Table 6**: Example alignment quality metrics (to be replaced with actual experimental data).
