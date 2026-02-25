# Paper 1: Spatial and Temporal Synchronization (Foundation)

**Title**: Spatial and Temporal Synchronization for Multi-Source PBF-LB/M Data: Design, Rationale, and Implementation

**Target Venue**: To be determined (foundation paper; may be submitted to Additive Manufacturing, Journal of Manufacturing Systems, or a conference)

**Status**: In progress — structure complete; content to be refined and filled with experimental results

## Paper Structure

This paper focuses on **transformation, spatial alignment, and temporal synchronization** as the foundation that must be performed **before** any downstream analysis (Papers 3–5).

### Sections

1. [Abstract](Abstract.md) (250 words)
2. [Introduction](Introduction.md) (Problem statement, motivation, scope)
3. [Related Work](Related_Work.md) (Registration, temporal alignment in AM)
4. [Design](Design.md) (Point-first pipeline; spatial bbox-corner, 24×56, Kabsch+Umeyama; temporal layer/time)
5. [Why Our Algorithm](Why_Our_Algorithm.md) (Comparison with grid-based and point-matching; validation, tolerance)
6. [Implementation and API](Implementation_and_API.md) (query_and_transform_points, C++ components)
7. [Results](Results.md) (Accuracy, robustness, performance)
8. [Discussion](Discussion.md) (Advantages, limitations)
9. [Conclusion](Conclusion.md)
10. [References](References.md)
11. [Figures](Figures.md) (Pipeline, bbox-corner, validation, comparison)
12. [Tables](Tables.md) (Old vs new alignment; transformation summary; validation; API)

## Key Contributions

1. **Point-First Pipeline**
   - Transform point coordinates **before** voxelization; avoids grid resampling and preserves precision.

2. **Spatial Alignment: Bbox-Corner Correspondence**
   - Use only 8 bbox corners per source; 24 permutations × 56 triplets; Kabsch + Umeyama similarity transform; select fit with smallest max error on all 8 corners; validate with best_ref_corners and 1% adaptive tolerance.

3. **Temporal Alignment**
   - Layer/time mapping and point-based temporal alignment so that "same layer" or "same time window" is well-defined across sources.

4. **Why Our Algorithm**
   - Comparison with grid-based alignment and RANSAC/point matching; full extent by default; best_ref_corners validation; adaptive tolerance.

5. **Implementation and API**
   - C++ (am_qadf_native) with Python bindings; main entry point `UnifiedQueryClient.query_and_transform_points`.

## Why This Paper Comes First

Without a common coordinate system and consistent time/layer reference across hatching, ISPM, CT, laser, etc.:

- Fusion, signal mapping, and quality assessment are ill-defined
- "Same location" and "same layer" are ambiguous across sources
- Downstream analysis (Papers 3, 4, 5) assumes aligned data

Paper 1 explains the problem, the point-first pipeline, and why our approach is preferable to alternatives.

## Design Documents (Main Repository)

Full design and algorithm rationale are in the **main repository** (not in this publications repo):

| Topic | Path (relative to repo root) |
|-------|------------------------------|
| Spatial alignment (full design, old vs new) | `implementation_plan/new/SPATIAL_ALIGNMENT_DESIGN.md` |
| Temporal alignment (purpose, pipeline position) | `implementation_plan/new/Temporal_Alignment_Design.md` |
| Point vs grid pipeline, naming | `implementation_plan/new/Synchronization_Reorganize_Plan.md` |
| Transformation next steps / implementation | `implementation_plan/new/TRANSFORMATION_NEXT_STEPS.md` |
| Synchronization module overview and workflow | `docs/AM_QADF/05-modules/synchronization.md` |
| Synchronization API (e.g. `query_and_transform_points`) | `docs/AM_QADF/06-api-reference/synchronization-api.md` |
| Notebook: temporal and spatial alignment | `docs/Notebook/04-notebooks/04-alignment.md` |

## Checklist

See the **Publication Checklist** in [Publication_Narrative.md](../Publication_Narrative.md) for Paper 1 items.

---

**Parent**: [Publications README](../README.md)
