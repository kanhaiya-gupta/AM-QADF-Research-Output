# Figures

**Note:** Figures 1–4 and the **transformation/validation equations** are embedded in the **Design (methodology)** section ([Design.md](Design.md)) as Mermaid flowcharts and LaTeX equations. The methodology includes: pipeline overview (Fig. 1), spatial alignment sub-flow (Fig. 2), validation flow (Fig. 3), temporal alignment flow (Fig. 4), Kabsch/Umeyama equations, quality metrics, and adaptive tolerance formulae.

## Required Figures (in Design / Methodology)

1. **Figure 1: Synchronization Pipeline Overview** — *in Design.md*
   - **Description**: Mermaid flowchart: Query → Compute bbox per source → Fit transform (24×56) → Validate (best_ref_corners) → Transform points → (Optional) temporal alignment → Output.
   - **Purpose**: Illustrates the point-first pipeline and where spatial and temporal alignment sit relative to query and voxelization.

2. **Figure 2: Spatial Alignment Sub-Flow (24×56 Fit Selection)** — *in Design.md*
   - **Description**: Mermaid flowchart: input source/reference corners → for each permutation reorder → 56 triplets → Kabsch + Umeyama → quality on all 8 corners → select best (smallest max error).
   - **Purpose**: Explains bbox-corner correspondence and the fit-and-select loop.

3. **Figure 3: Validation Flow** — *in Design.md*
   - **Description**: Mermaid flowchart: transform T, source_corners, best_ref_corners → adaptive tolerance τ → compare q̂_i = T s_i to r_best,i → max_error and rms_error ≤ τ → is_valid.
   - **Purpose**: Clarifies why validation must use reordered reference corners so pass/fail matches the fit.

4. **Figure 4: Temporal Alignment Flow** — *in Design.md*
   - **Description**: Mermaid flowchart: transformed_points, layer_indices, timestamps → LayerTimeMapper → bin by layer or time window → group indices per layer per source → layer_alignment_result → slice for layer ℓ.
   - **Purpose**: Shows where temporal alignment fits and what it produces.

## Required Figures (standalone / to generate)

5. **Figure 5: Point-First vs Grid-Based Alignment**
   - **Description**: Side-by-side: (a) Point-first: Query → Transform points → Voxelize; (b) Grid-based (old): Query → Voxelize → Transform grid. Annotate resampling and precision loss in (b).
   - **Purpose**: Motivates point-first design and comparison with deprecated grid-based approach.

6. **Figure 6: Multi-Source Alignment Result (Example)**
   - **Description**: (To be generated from notebooks.) Before/after alignment of two or three sources (e.g. hatching + ISPM thermal) in same reference frame; unified bounds; optional visualization of validation errors.
   - **Purpose**: Demonstrates end-to-end alignment on real or synthetic data.

7. **Figure 7: Alignment Error vs Tolerance (Example)** (to be generated)
   - **Description**: (To be generated.) Max error and RMS error on 8 bbox corners vs adaptive tolerance; pass/fail region; typical values for one or more sources.
   - **Purpose**: Supports Results section (accuracy, validation behaviour).

## Optional Figures

8. **Figure 8: Transformation Quality Metrics**
   - **Description**: Example of quality metrics (rms_error, max_error, mean_error) and fit_errors_summary (min_max_error, max_max_error over 24×56 fits) for one source.
   - **Purpose**: Illustrates what is returned in `transformations[source]`.

9. **Figure 9: Layer-Time Mapping**
   - **Description**: Layer index vs timestamp (or Z height); LayerTimeMapper concept; use in temporal alignment.
   - **Purpose**: Supports temporal alignment section.

## Figure Captions (Draft)

**Figure 1**: Point-first synchronization pipeline: query, bbox-corner fit, validation, point transformation, optional temporal alignment, then voxelization/mapping.

**Figure 2**: Bounding box corners (8×3) in fixed order; 24 permutations of reference corner order and 56 triplets per permutation; selection of similarity transform with smallest max error on all 8 corners.

**Figure 3**: Validation uses reference corners reordered by the best permutation (best_ref_corners); pass when max error and RMS ≤ adaptive tolerance (1% of max extent).

**Figure 4**: Temporal alignment flow (layer/time mapping, point temporal alignment) as optional step after spatial transform (see Design.md).

**Figure 5**: (a) Point-first: transform points then voxelize. (b) Grid-based (deprecated): voxelize then transform grid; resampling and precision loss.

**Figure 6**: Example multi-source alignment: hatching (reference) and ISPM thermal in same frame with unified bounds.

**Figure 7**: Example alignment error vs adaptive tolerance; pass/fail region.
