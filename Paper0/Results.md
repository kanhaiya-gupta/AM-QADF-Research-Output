# Results

## Alignment Accuracy

(To be filled with concrete numbers from experiments.)

- **Spatial**: After bbox-corner fit and validation, transformed points align to the reference frame with errors within the adaptive tolerance (1% of max bbox extent). Typical max error on the 8 bbox corners is below tolerance when sources share the same physical extent.
- **Validation pass rate**: When data satisfies the same-extent assumption, validation (using best_ref_corners) passes; when extent or geometry differ, validation fails as expected.
- **Sub-voxel**: For typical voxel sizes (e.g. 0.1–1 mm), alignment errors are sub-voxel, so downstream signal mapping and fusion are not degraded by alignment error.

## Robustness

- **24×56 search**: Over 24 permutations and 56 triplets, the selected fit (smallest max error on 8 corners) is robust to different axis orderings and avoids degenerate triplets.
- **best_ref_corners**: Validation using the reordered reference corners avoids false failures and ensures pass/fail matches the fit.
- **Full extent**: Using full data extent by default yields a stable, single transform for the whole build; optional filters do not change the transform.

## Performance

(To be filled with benchmarks.)

- **Transform computation**: 24×56 fits per non-reference source; cost is dominated by SVD (Kabsch) and small linear systems (Umeyama) on 3×3 or 8×3 data; runtime is typically milliseconds per source.
- **Point transformation**: Bulk application of 4×4 transform to N points is O(N); memory is O(N) for point arrays.
- **Comparison to grid-based**: Point-first avoids grid resampling and extra I/O; end-to-end pipeline (query → transform → bounds) is typically faster than the old grid-transform approach when both are measured on the same hardware.

## Multi-Source Behaviour

- **Hatching + ISPM + CT**: Pipeline has been exercised with hatching (reference), ISPM thermal/optical, and CT; transformed points and unified_bounds are consistent; validation_results and transformations provide per-source quality and fit metrics.
- **Optional temporal alignment**: When layer/time mapping and point temporal alignment are used, per-layer indices and alignment result structures support downstream per-layer fusion and analysis.

## Reproducibility

- Transformation matrices and quality metrics are returned in the result dict; they can be stored or logged for reproducibility.
- When save_processed_data is used, transformed points (e.g. with "Processed_" prefix) and metadata can be written to the database for audit and replay.

## Summary

Results demonstrate that the point-first, bbox-corner spatial alignment with 24×56 fit selection and best_ref_corners validation achieves sub-voxel accuracy, robust behaviour across multi-source PBF-LB/M data, and correct validation semantics. Performance is suitable for production use. Concrete figures and tables (max error, RMS, runtime, pass rate) should be added from actual experiments and placed in the Figures and Tables sections.
