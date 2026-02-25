# Implementation and API

## Overview

Spatial alignment (bbox-corner fit, validation, point transformation) and unified bounds are implemented in **C++** (am_qadf_native). Python exposes the pipeline via **UnifiedQueryClient.query_and_transform_points** and optional helpers for temporal alignment.

## Main Entry Point: query_and_transform_points

```python
from am_qadf.query import UnifiedQueryClient

client = UnifiedQueryClient(...)

result = client.query_and_transform_points(
    model_id="...",
    source_types=["hatching", "ispm_thermal", "ispm_optical"],
    reference_source="hatching",
    layer_range=None,           # optional (layer_start, layer_end)
    bbox=None,                  # optional ((x_min,y_min,z_min), (x_max,y_max,z_max))
    use_full_extent_for_transform=True,  # default: bbox from full data
    validation_tolerance=1e-6,
    save_processed_data=False,
    mongo_uri=None,
    db_name=None,
)
```

### Parameters

- **model_id**: Model UUID.
- **source_types**: List of source keys (e.g. hatching, ispm_thermal, ispm_optical).
- **reference_source**: Reference frame (e.g. "hatching"); non-reference sources are transformed to this frame.
- **layer_range**, **bbox**: Optional filters; by default they affect only which points are returned/saved when `use_full_extent_for_transform=True`.
- **use_full_extent_for_transform**: If True (default), bboxes and transform are computed from full data; if False, from the queried subset.
- **validation_tolerance**: Minimum tolerance; adaptive tolerance is `max(0.01 * max_extent, 1e-3, validation_tolerance)`.
- **save_processed_data**: If True, save transformed points (e.g. via MongoDBWriter); requires mongo_uri and db_name when used.

### Returned Structure

- **transformed_points**: `{ source_type: (N, 3) }` points in reference frame.
- **signals**: `{ source_type: { signal_name: array } }` per source.
- **unified_bounds**: BoundingBox (union of returned point sets).
- **transformations**: Per non-reference source: `matrix`, `quality`, `fit_errors`, `best_fit`, `fit_errors_summary`, optional `correspondence_validation`.
- **validation_results**: `{ source_type: ValidationResult }` (pass/fail, errors; uses best_ref_corners internally).
- **raw_results**: Query results before transform.

When temporal alignment is used, the result may also include **layer_alignment_result** and **layer_indices** (or equivalent) for per-layer, per-source indexing.

## C++ Components (Summary)

| Component | Role |
|-----------|------|
| **UnifiedBoundsComputer** | Compute bounds from points; BoundingBox::corners() → 8×3 |
| **TransformationSampling** | Enumerate 56 triplets from 8 corners per permutation |
| **TransformationComputer** | computeTransformationFromBboxCorners: 24×56 fits, Kabsch+Umeyama, quality, best_ref_corners, per-fit errors |
| **TransformationValidator** | validateWithMatrix(source_corners, transform, best_ref_corners, tolerance); isValid when within tolerance |
| **PointTransformer** | Apply 4×4 transform to point sets |

Temporal alignment (e.g. align_points_by_layer) is available as a separate step or integrated where supported; see `docs/AM_QADF/06-api-reference/synchronization-api.md` and `implementation_plan/new/Temporal_Alignment_Design.md`.

## Python Bindings

- **am_qadf_native** must be built (C++ extension).
- TransformationComputer, TransformationValidator, PointTransformer, UnifiedBoundsComputer, BoundingBox, and helpers (e.g. points_to_eigen_matrix) are exposed to Python.
- Notebooks (e.g. `04_Temporal_and_Spatial_Alignment.ipynb`) demonstrate query_and_transform_points and validation.

## Design Documents

Full design and parameter semantics:

- **Spatial**: `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md`
- **Temporal**: `implementation_plan/new/Temporal_Alignment_Design.md`
- **Pipeline/naming**: `implementation_plan/new/Synchronization_Reorganize_Plan.md`
- **API**: `docs/AM_QADF/06-api-reference/synchronization-api.md`
- **Module overview**: `docs/AM_QADF/05-modules/synchronization.md`
