# Paper 2: Analysis Framework

**Title**: Comprehensive Analysis Framework for Multi-Source PBF-LB/M Data: Sensitivity Analysis, Virtual Experiments, and Anomaly Detection

**Target Venue**: Journal of Manufacturing Systems (Elsevier)

**Status**: ✅ Complete - Ready for Review and Refinement

## Paper Structure

This paper focuses on the **Analysis Framework** as the secondary contribution.

### Sections

1. [Abstract](Abstract.md)
2. [Introduction](Introduction.md)
3. [Analysis Capabilities](Analysis_Capabilities.md) (12 sensitivity methods, 10 experiment designs)
4. [Integration with Warehouse](Integration_with_Warehouse.md)
5. [Case Studies](Case_Studies.md) (5 case studies including MPM system sensitivity analysis and PBF-LB/M system/VM experiments)
6. [Results](Results.md)
7. [Discussion](Discussion.md)
8. [Conclusion](Conclusion.md)
9. [References](References.md)
10. [Figures](Figures.md)
11. [Tables](Tables.md)

## Key Contributions

1. **Comprehensive Analysis Capabilities**
   - 12 sensitivity analysis methods (Sobol, Morris, FAST, RBD, Delta, PAWN, DGSM, Local methods, Monte Carlo, Bayesian)
   - 10 virtual experiment design types (LHS, Factorial, Response Surface, Optimal designs)
   - 18 anomaly detection methods (Statistical, Clustering, ML-based, Rule-based)
   - Multi-signal fusion with quality-based weighting

2. **Warehouse Integration Architecture**
   - Seamless integration between analysis methods and NoSQL data warehouse
   - Direct querying of process variables and measurement outputs
   - Automatic parameter range extraction from historical builds
   - Results storage and querying for reproducibility

3. **Voxel Domain Analysis**
   - Spatial-temporal analysis in unified voxel domain
   - Multi-signal correlation at same spatial locations
   - Quality-based fusion using per-voxel quality scores
   - Spatial anomaly localization with voxel-level precision

4. **Interactive Analysis Framework**
   - 7 interactive Jupyter notebooks covering all analysis workflows
   - Widget-based interfaces for non-programmers
   - Real-time visualization and parameter adjustment
   - Guided workflows with error handling and validation

5. **Systematic Analysis Frameworks**
   - Systematic workflows for sensitivity analysis, virtual experiments, and anomaly detection
   - Method selection criteria and comparison tables
   - Best practices and recommendations

