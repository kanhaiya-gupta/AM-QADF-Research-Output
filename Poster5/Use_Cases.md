# Use Cases

## Use Case 1: Digital Quality Assessment for Aircraft Component Process Optimization

### Scenario
Optimize process parameters for **titanium alloy aircraft component** (Ti-6Al-4V) with complex internal channels, within LuFo VII framework.

### Challenge
- 15% of builds requiring rework or scrapping
- Inconsistent quality failing aerospace standards
- Need for systematic parameter optimization

### Framework Application
1. **Historical Data Analysis**: Queried warehouse for 20 historical builds
2. **Sensitivity Analysis**: Identified energy density (S1=0.38) and hatch spacing (S1=0.28) as most critical
3. **Virtual Experiments**: LHS design with 50 parameter combinations
4. **Physical Validation**: 3 builds with optimized parameters

### Results
- ✅ **0% scrap rate** (vs. 15% previously)
- ✅ **12% reduction** in build time
- ✅ **35% reduction** in process development time
- ✅ **78% prediction accuracy** for virtual experiments

## Use Case 2: Real-Time Digital Quality Assessment for Aircraft Components

### Scenario
Implement real-time digital quality assessment for aircraft component builds to enable early intervention, within LuFo VII framework.

### Challenge
- 12% scrap rate (defects only detected after build completion)
- High cost implications for aerospace-grade materials
- Need for early anomaly detection

### Framework Application
1. **Real-Time Integration**: Connected to ISPM monitoring system
2. **Multi-Method Detection**: Isolation Forest, DBSCAN, Multi-Signal Correlation
3. **Real-Time Monitoring**: 50 production builds over 3 months
4. **Process Intervention**: Real-time adjustments when anomalies detected

### Results
- ✅ **28% reduction** in defect rates (12% → 8.6%)
- ✅ **65% early detection** (before build completion)
- ✅ **78% spatial accuracy** (within 1 voxel of CT defects)
- ✅ **~$50,000/month** cost savings in reduced scrap

## Use Case 3: Digital Quality Assessment for Root Cause Analysis

### Scenario
Identify root cause of recurring defects in aircraft components using digital quality assessment, within LuFo VII framework.

### Challenge
- Recurring defects in specific spatial regions
- Traditional methods could not identify root cause
- Risk to aerospace certification and safety

### Framework Application
1. **Multi-Build Analysis**: 30 builds with similar defects
2. **Spatial Pattern Analysis**: Identified common defect locations
3. **Multi-Signal Correlation**: Strong negative correlation (r=-0.72) between hatch spacing and defects
4. **Root Cause**: Insufficient hatch spacing (<0.09 mm) in high energy density regions

### Results
- ✅ **Root cause identified**: Hatch spacing algorithm issue
- ✅ **40% reduction** in defect density in affected regions
- ✅ **85-90% reduction** in root cause analysis time
- ✅ **Systematic solution** implemented

## Common Success Factors

Across all use cases:
- **Warehouse Integration**: No manual data extraction (85-90% time savings)
- **Interactive Notebooks**: Non-programmers can perform analysis
- **Systematic Workflows**: Consistent, high-quality analysis
- **Multi-Signal Analysis**: Unified voxel domain enables correlation analysis

