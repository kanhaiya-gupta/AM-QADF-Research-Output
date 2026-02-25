# Discussion

## Advantages

### Point-First Pipeline

Transforming points before voxelization avoids resampling artifacts and preserves point-level precision. Downstream signal mapping (Paper 3) and fusion operate on already-aligned points, so alignment quality is not limited by voxel resolution. Validation is performed on the same bbox corners used for fit selection, so pass/fail is consistent and interpretable.

### Bbox-Corner-Only Correspondence

Using only 8 bbox corners per source avoids the need for point-to-point matching or RANSAC. When sources share the same physical extent, the bbox geometry fully constrains the similarity transform. The 24×56 search over permutations and triplets is deterministic and robust to different axis orderings and degenerate triplets. No tuning of RANSAC thresholds or inlier counts is required.

### Full Extent and Adaptive Tolerance

Computing bboxes and transforms from full data by default yields a single, stable alignment for the whole build. The 1% adaptive tolerance scales with part size and keeps validation meaningful across different build volumes. User override (validation_tolerance) allows stricter or looser checks when needed.

### Temporal Alignment

Explicit layer/time mapping and point-based temporal alignment make "same layer" and "same time window" well-defined across sources. Per-layer fusion and time-window analysis can be implemented without grid resampling. The step is optional so that workflows that only need spatial alignment are not forced to use temporal alignment.

## Limitations

### Same-Extent Assumption

Spatial alignment assumes that each source's bounding box has the **same physical extent** (same size box in different frames). If one source covers only a subset of the build (e.g. a sensor with limited field of view), the bbox-corner fit may be ill-posed or the transform may not align the full build. In such cases, alternative strategies (e.g. partial overlap, known calibration) may be needed; the current design does not address them.

### Similarity Transform Only

We fit a **similarity** transform (rotation, uniform scale, translation). Non-uniform scale, shear, or more general deformations are not modeled. For many PBF-LB/M setups (build platform, CT, ISPM with calibrated geometry), similarity is sufficient; for heavily distorted or non-rigid data, the method would need extension.

### Temporal Alignment Scope

Temporal alignment (layer/time mapping, point temporal alignment) is documented and implemented for point-based workflows. Grid temporal alignment (aligning already-voxelized grids by time/layer) is a separate path and not the focus of this paper. Integration with build logs or machine timestamps for layer-time mapping may require deployment-specific configuration.

### Performance and Scale

The 24×56 fit search is fast for typical builds (milliseconds per source). For very large point sets, the dominant cost is point I/O and applying the transform; the design does not change the O(N) nature of point transformation. Very large builds may require batching or streaming if memory is constrained.

## Future Work

- **Partial overlap**: Relax the same-extent assumption for sources with limited coverage (e.g. sensor FOV) via overlap-based or calibration-augmented alignment.
- **Non-similarity transforms**: Optional support for non-uniform scale or constrained deformations when metadata or calibration indicate the need.
- **Uncertainty**: Propagate transformation uncertainty (e.g. from fit quality) into downstream fusion and quality metrics.
- **Benchmarks**: Publish quantitative benchmarks (accuracy, runtime, pass rate) on public or synthetic multi-source PBF-LB/M datasets.

## Summary

The point-first, bbox-corner spatial alignment with 24×56 fit selection and best_ref_corners validation, combined with optional point temporal alignment, provides a robust and interpretable foundation for multi-source PBF-LB/M data. Advantages include no grid resampling, deterministic fit selection, full-extent stability, and scalable validation. Limitations include the same-extent assumption and similarity-only transform; future work may address partial overlap, non-similarity transforms, and uncertainty propagation.
