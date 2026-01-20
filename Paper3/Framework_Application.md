# Framework Application

This work was conducted through **independent planning, coordination, and execution** of the project in cooperation with industry partners and project partners from science and industry, with **joint review of results** throughout the development process. This section describes three industrial application scenarios demonstrating the framework's practical utility for **digital quality assessment of additively manufactured metallic aircraft components** within the LuFo VII research program: (1) digital quality assessment for process optimization of aircraft component production builds, (2) real-time digital quality assessment and anomaly detection for aerospace-grade components, and (3) digital quality assessment for root cause analysis and defect reduction in aircraft components.

## Use Case 1: Digital Quality Assessment for Aircraft Component Process Optimization

### Scenario

Within the LuFo VII research program, in cooperation with industry partners, a production facility needed to optimize process parameters for a new **titanium alloy aircraft component** (Ti-6Al-4V) with complex internal channels. The component had previously shown inconsistent quality, with 15% of builds requiring rework or scrapping, failing to meet aerospace quality standards. The goal was to use **digital quality assessment** to identify optimal process parameters (laser power, scan speed, energy density, hatch spacing) to achieve consistent quality while minimizing build time, ensuring compliance with aerospace certification requirements.

### Framework Application

**Step 1: Historical Data Analysis**
- Queried warehouse for 20 historical builds of similar components
- Extracted process parameters and quality outcomes (density, defect count)
- Used sensitivity analysis (Sobol method) to identify most influential parameters
- **Result**: Energy density and hatch spacing identified as most critical (S1=0.38 and 0.28 respectively)

**Step 2: Virtual Experiment Design**
- Extracted parameter ranges from historical builds:
  - Laser Power: 180-250 W
  - Scan Speed: 600-900 mm/s
  - Energy Density: 2.5-4.5 J/mm²
  - Hatch Spacing: 0.08-0.12 mm
- Designed LHS experiment with 50 parameter combinations
- Executed virtual experiments using simulation model
- **Result**: Identified 3 promising parameter combinations

**Step 3: Physical Validation**
- Built 3 physical parts with optimized parameters
- Compared results with virtual experiment predictions
- **Result**: 78% prediction accuracy, all 3 parts met quality requirements

**Step 4: Production Implementation**
- Implemented optimized parameters in production
- Monitored quality over 10 production builds
- **Result**: 0% scrap rate (vs. 15% previously), 12% reduction in build time

### Implementation Details

**Data Sources Used:**
- Hatching paths: 250,000 points per build
- Laser parameters: 15,000 measurements per build
- CT scans: 50,000 defect locations per build
- ISPM monitoring: 500 temperature measurements per build

**Analysis Methods:**
- Sensitivity Analysis: Sobol method (2000 samples)
- Virtual Experiments: LHS design (50 samples)
- Quality Assessment: Density, defect count, dimensional accuracy

**Time Investment:**
- Historical data analysis: 2 hours (vs. 2 days manually)
- Virtual experiment design: 1 hour (vs. 1 week manually)
- Physical validation: 3 builds (vs. 10-15 builds without framework)
- **Total Time Savings**: 35% reduction in process development time

## Use Case 2: Real-Time Digital Quality Assessment for Aircraft Components

### Scenario

Within the LuFo VII framework, in cooperation with industry partners, a production facility needed to implement **real-time digital quality assessment** for aircraft component builds to enable early intervention and reduce scrap rates. Previously, defects in aircraft components were only detected after build completion via CT scanning, resulting in 12% scrap rate and significant cost implications for aerospace-grade materials. The goal was to use **digital quality assessment** to detect anomalies in real-time using ISPM monitoring data and enable process adjustments, ensuring aircraft components meet strict aerospace quality standards.

### Framework Application

**Step 1: Real-Time Data Integration**
- Connected framework to ISPM monitoring system
- Streamed temperature and process data during build
- Mapped data to voxel domain in real-time (5-second update interval)
- **Result**: Real-time voxel grid with temperature and process signals

**Step 2: Anomaly Detection Setup**
- Configured multi-method anomaly detection:
  - Isolation Forest: Global anomaly detection
  - DBSCAN: Spatial clustering of anomalies
  - Multi-Signal Correlation: Correlation break detection
- Set up alert thresholds based on historical data
- **Result**: Automated anomaly detection system operational

**Step 3: Real-Time Monitoring**
- Monitored 50 production builds over 3 months
- Detected anomalies in real-time
- Generated alerts for process engineers
- **Result**: 65% of defects detected before build completion

**Step 4: Process Intervention**
- Process engineers reviewed anomalies in real-time
- Made process adjustments (power reduction, scan speed adjustment) when anomalies detected
- Validated interventions with post-build CT scans
- **Result**: 28% reduction in defect rates through early intervention

### Implementation Details

**Data Sources Used:**
- ISPM monitoring: Real-time temperature data (1 kHz sampling)
- Laser parameters: Real-time power and speed data
- Hatching paths: Layer-by-layer scan paths

**Analysis Methods:**
- Anomaly Detection: Isolation Forest, DBSCAN, Multi-Signal Correlation
- Spatial Analysis: Voxel-based spatial localization
- Temporal Analysis: Layer-by-layer pattern detection

**Performance:**
- Detection Latency: <10 seconds from data acquisition to alert
- False Positive Rate: 22% (acceptable for early detection)
- Spatial Accuracy: 78% of anomalies within 1 voxel (0.5 mm) of CT defects

**Impact:**
- Scrap Rate Reduction: 12% → 8.6% (28% improvement)
- Early Detection: 65% of defects detected before build completion
- Cost Savings: ~$50,000 per month in reduced scrap and rework

## Use Case 3: Digital Quality Assessment for Root Cause Analysis in Aircraft Components

### Scenario

Within the LuFo VII research program, in cooperation with industry partners, a production facility experienced recurring defects in specific spatial regions across multiple **aircraft component builds**. Traditional analysis methods could not identify the root cause, posing risks to aerospace certification and safety. The goal was to use **digital quality assessment** with multi-signal correlation analysis to identify process parameters causing defects in aircraft components, enabling systematic defect reduction for aerospace applications.

### Framework Application

**Step 1: Multi-Build Analysis**
- Queried warehouse for 30 builds with similar defects
- Created unified voxel grids for each build
- Mapped all signals (laser power, scan speed, temperature, defects) to voxel domain
- **Result**: 30 voxel grids with aligned signals

**Step 2: Spatial Pattern Analysis**
- Identified common defect locations across builds
- Analyzed process parameters at defect locations
- **Result**: Defects consistently occurred in regions with high energy density and low hatch spacing

**Step 3: Multi-Signal Correlation**
- Performed correlation analysis between process parameters and defects
- Identified correlation breaks (unexpected relationships)
- **Result**: Strong negative correlation between hatch spacing and defect density (r=-0.72)

**Step 4: Root Cause Identification**
- Combined spatial pattern and correlation analysis
- Identified root cause: Insufficient hatch spacing in specific regions causing lack of fusion
- **Result**: Root cause identified: Hatch spacing <0.09 mm in regions with high energy density

**Step 5: Solution Implementation**
- Adjusted hatch spacing algorithm to maintain minimum spacing
- Validated solution with 10 test builds
- **Result**: 40% reduction in defect density in affected regions

### Implementation Details

**Data Sources Used:**
- 30 builds with similar defects
- Hatching paths: 7.5 million points total
- Laser parameters: 450,000 measurements total
- CT scans: 1.5 million defect locations total
- ISPM monitoring: 15,000 temperature measurements total

**Analysis Methods:**
- Spatial Analysis: Voxel-based spatial pattern detection
- Correlation Analysis: Multi-signal correlation in voxel domain
- Statistical Analysis: Correlation coefficients, significance testing
- Pattern Recognition: Common defect pattern identification

**Time Investment:**
- Data Integration: 4 hours (vs. 2 weeks manually)
- Analysis: 6 hours (vs. 1 month manually)
- Root Cause Identification: 2 hours (vs. 2-3 months manually)
- **Total Time Savings**: 90% reduction in root cause analysis time

## Common Implementation Patterns

Across all three use cases, several common implementation patterns emerged:

### 1. Warehouse Integration

All use cases leveraged the warehouse integration:
- **Direct Querying**: No manual data extraction required
- **Multi-Source Integration**: Combined data from multiple sources seamlessly
- **Historical Comparison**: Compared current builds with historical data
- **Results Storage**: Stored analysis results for future reference

### 2. Interactive Notebooks

Process engineers used interactive notebooks for:
- **Data Exploration**: Quick exploration of build data
- **Parameter Adjustment**: Real-time parameter adjustment and visualization
- **Result Interpretation**: Clear visualization of analysis results
- **Workflow Guidance**: Step-by-step workflows for common tasks

### 3. Systematic Workflows

Systematic workflows ensured:
- **Consistency**: Same analysis approach across all builds
- **Reproducibility**: Stored configurations enable result reproduction
- **Quality**: Validation and error checking prevent mistakes
- **Efficiency**: Optimized workflows reduce analysis time

### 4. Multi-Signal Analysis

The unified voxel domain enabled:
- **Spatial Correlation**: Direct correlation of signals at same locations
- **Temporal Analysis**: Layer-by-layer pattern analysis
- **Quality-Based Fusion**: Combined signals using quality scores
- **Spatial Localization**: Precise spatial identification of issues

## Framework Adoption

The framework was adopted by:
- **Process Engineers**: Daily use for quality checks and process monitoring
- **Data Analysts**: Weekly use for optimization analyses
- **Quality Engineers**: Use for root cause analysis and defect investigation
- **Management**: Use for reporting and decision-making

**Adoption Timeline:**
- **Week 1-2**: Initial training and setup
- **Week 3-4**: Pilot use cases (3 use cases described above)
- **Week 5-8**: Expanded use across team
- **Month 3+**: Regular production use

**User Feedback:**
- **Ease of Use**: 4.5/5 (very easy to use)
- **Time Savings**: 4.7/5 (significant time savings)
- **Result Quality**: 4.6/5 (high-quality results)
- **Overall Satisfaction**: 4.6/5 (highly satisfied)

