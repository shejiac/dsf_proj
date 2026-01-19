# DSF_DRAFT.IPYNB REORGANIZATION: DETAILED MERGE INSTRUCTIONS

## EXECUTIVE SUMMARY

**Current State:** 189 cells with significant duplication across 5+ instances of dataset assessments
**Target State:** ~151 cells organized into clean 5-phase framework (Ask → Prepare → Analyze → Share → Conclude)
**Reduction:** 38 cells eliminated through consolidation (20% reduction)
**Information Loss:** 0% (all content preserved in merged versions)

---

## PHASE BOUNDARIES IN REORGANIZED NOTEBOOK

| Phase | Cells | Original Cell IDs | Content |
|-------|-------|-------------------|---------|
| **Ask** (Problem Definition) | 1-7 | #VSC-e44fb60a to #VSC-0ee6825a | Imports, title, hypothesis, theory, data requirements |
| **Prepare** (Data Exploration) | 8-37 | #VSC-112fc3c5 to #VSC-825e8a64 | All 5 dataset explorations (consolidated) + feature summary |
| **Analyze** (Modeling) | 38-64 | #VSC-808c47b5 to #VSC-34169682 | Feature engineering, CV setup, training, diagnostics |
| **Share** (Results) | 65-83 | #VSC-cb849978 to #VSC-12c59c14 | Key findings, theory validation, practical implications |
| **Conclude** (Limitations & Rubric) | 84-111 | #VSC-89369677 to #VSC-9aa5d2ab | Limitations, rubric alignment, ethics, future work |

---

## CRITICAL MERGES (DUPLICATE CONTENT CONSOLIDATION)

### MERGE 1: DS1 COMPREHENSIVE ASSESSMENT
**Location:** Prepare Phase, Position 13  
**Merge Cells:** 44, 45, 46  
**Cell IDs:** #VSC-96c061db, #VSC-8cb21f42, #VSC-1eb74055

**Original Content in Each Cell:**
- Cell 44 (Markdown): DS1 description + profiling (description, metrics table, profiling interpretation)
- Cell 45 (Markdown): Quality criteria 1+2 (completeness, volume anomalies)
- Cell 46 (Markdown): Suitability conclusion (decision + note about retention)

**Merge Strategy:**
1. Keep Cell 44 as base (comprehensive description + metrics)
2. Insert "Data Quality Assessment" header from Cell 45
3. Merge both criteria (completeness + anomalies) into single assessment block
4. Add Cell 46's conclusion (keep, rationale for handling spikes)
5. Result: Single consolidated 3-section DS1 block (~200 lines markdown)

**Output Structure:**
```
### DS1: SPY Price Data (OHLCV Time Series) - CONSOLIDATED
#### Description & Profiling
[Content from Cell 44: Full description + table of metrics]

#### Data Quality Assessment
**Criterion 1:** Completeness & Logical Consistency ✅
[Content from Cell 45 Criterion 1 + interpretation]

**Criterion 2:** Volume Anomalies ⚠️
[Content from Cell 45 Criterion 2 + handling approach]

#### Suitability Conclusion
✅ **SELECTED FOR PRIMARY ANALYSIS**
[Content from Cell 46 + note about volume spike handling]
```

**Information Preserved:**
- ✓ All metrics (2.07M rows, dates, missing values %, volume stats)
- ✓ Both quality criteria (completeness + anomaly patterns)
- ✓ Conclusion rationale
- ✓ Handling approach for edge cases

---

### MERGE 2: DS2 COMPREHENSIVE ASSESSMENT
**Location:** Prepare Phase, Position 14  
**Merge Cells:** 47, 48, 49  
**Cell IDs:** #VSC-43ca7866, #VSC-be73f37b, #VSC-1fc03f3a

**Original Content:**
- Cell 47: DS2 full description + profiling (LOBSTER explanation, data types, alignment with DS1)
- Cell 48: Quality criterion 1+2 (realism, sparsity issues)
- Cell 49: Suitability conclusion (use with limitations, synthetic feature approach)

**Merge Strategy:**
1. Cell 47 as base (comprehensive LOBSTER description + metrics)
2. Add "Data Quality Assessment" header
3. Merge criteria 1+2 (microstructure realism, sparsity, temporal alignment)
4. Consolidate conclusion (synthetic OB generation approach explained)
5. Result: Single 3-section DS2 block (~250 lines markdown)

**Output Structure:**
```
### DS2: LOBSTER Order Book Snapshots - CONSOLIDATED
#### Description & Microstructure Features
[Cell 47 content: Full LOBSTER explanation + profiling table]

#### Data Quality Assessment
**Criterion 1:** Microstructure Realism ✅
[Cell 48 Criterion 1: Spread alignment + depth profiles + imbalance range]

**Criterion 2:** Temporal Alignment & Sparsity ⚠️
[Cell 48 Criterion 2: 30-sec vs 1-min alignment + 2-month coverage limitation]

#### Suitability Conclusion
✅ **SELECTED FOR FEATURE ENGINEERING**
[Cell 49: Synthetic OB derivation approach + LOBSTER validation role]
```

**Information Preserved:**
- ✓ Full LOBSTER data description
- ✓ Microstructure feature extraction (spread, imbalance, depth)
- ✓ Quality assessment (realistic ranges, temporal challenges)
- ✓ Solution approach (synthetic features + real validation)

---

### MERGE 3: DS3 COMPREHENSIVE ASSESSMENT
**Location:** Prepare Phase, Position 15  
**Merge Cells:** 51, 52, 53, 54  
**Cell IDs:** #VSC-37bab768, #VSC-1a31898d, #VSC-e26a03c3, #VSC-4aa218d0

**Original Content:**
- Cell 51: DS3 full description (NFCI, STLFSI2, regime role)
- Cell 52: Code for temporal alignment (forward-fill implementation)
- Cell 53: Quality criteria 1+2 (relevance, temporal misalignment)
- Cell 54: Suitability conclusion (regime analysis use case)

**Merge Strategy:**
1. Cell 51 as markdown base (DS3 description)
2. Insert "Data Profiling" from Cell 51 (frequency, coverage, stationarity)
3. Add quality criteria section (conceptual relevance + temporal issues)
4. Consolidate conclusion (forward-fill approach + regime conditioning)
5. Result: Single 3-section DS3 markdown + Code block (~200 lines total)

**Output Structure:**
```
### DS3: FRED Financial Stress Indices - CONSOLIDATED
#### Description & Data Profiling
[Cell 51 content: NFCI + STLFSI2 explanation + metrics table]

#### Data Quality Assessment
**Criterion 1:** Conceptual Relevance ✅
[Cell 53 Criterion 1: Regime shift design + Fed authority + theory link]

**Criterion 2:** Temporal Misalignment ⚠️
[Cell 53 Criterion 2: Daily vs 1-min frequency + forward-fill solution]

#### Suitability Conclusion
✅ **SELECTED FOR REGIME ANALYSIS**
[Cell 54: Grouping variable primary use + forward-fill approach]
```

**Code Integration:**
- Include Cell 52 code snippet showing forward-fill implementation
- Show pandas code for aligning daily→1-minute frequency

**Information Preserved:**
- ✓ NFCI/STLFSI2 definitions and range
- ✓ Temporal frequency and coverage (2015-2024)
- ✓ Regime classification approach
- ✓ Forward-fill implementation for temporal alignment

---

### MERGE 4: DS4 COMPREHENSIVE ASSESSMENT (EXPLORATORY)
**Location:** Prepare Phase, Position 16  
**Merge Cells:** 56, 57, 58, 59  
**Cell IDs:** #VSC-c47af449, #VSC-4f334e75, #VSC-e9993259, #VSC-4ae58fec

**Original Content:**
- Cell 56: DS4 description (volatility, clustering, trade intensity)
- Cell 57: Code for criterion 1 (volatility clustering computation)
- Cell 58: Quality criteria 1+2 (theoretical relevance, redundancy)
- Cell 59: Suitability conclusion (exploratory only, excluded from model)

**Merge Strategy:**
1. Cell 56 as base (DS4 description + metrics)
2. Add "Data Profiling & Quality Assessment"
3. Merge criteria (GARCH relevance + 0.66 correlation redundancy)
4. Consolidate conclusion (exploratory designation + exclusion rationale)
5. Result: Single section with code snippet (~180 lines)

**Output Structure:**
```
### DS4: Volatility & Microstructure Dynamics (Exploratory) - CONSOLIDATED
#### Description & Data Profiling
[Cell 56: Derived measure explanation + metrics table]

#### Data Quality Assessment
**Criterion 1:** Theoretical Relevance ✅
[Cell 58 Criterion 1: GARCH literature + volatility persistence evidence]

**Criterion 2:** Feature Redundancy ⚠️
[Cell 58 Criterion 2: 0.66 correlation with DS1 realized vol + limited marginal value]

#### Suitability Conclusion
🔬 **SELECTED FOR EXPLORATORY ANALYSIS ONLY**
[Cell 59: Academic rigor explanation + exclusion from final 19-feature set]
```

**Code Integration:**
- Include Cell 57 code for volatility clustering computation
- Show correlation matrix vs DS1 features

**Information Preserved:**
- ✓ Realized volatility formula + rolling windows
- ✓ Vol-of-vol clustering indicator
- ✓ Redundancy quantification (0.66 r)
- ✓ Exclusion rationale (parsimony principle)

---

### MERGE 5: DS5 COMPREHENSIVE ASSESSMENT (VALIDATION)
**Location:** Prepare Phase, Position 17  
**Merge Cells:** 61, 62, 63, 64  
**Cell IDs:** #VSC-c433265d, #VSC-cde6d399, #VSC-29f843c1, #VSC-874baaef

**Original Content:**
- Cell 61: DS5 description (Alpha Vantage API purpose + profiling)
- Cell 62: Code for criterion 2 (volume anomaly detection)
- Cell 63: Quality criteria 1+2 (completeness, anomalies)
- Cell 64: Suitability conclusion (selective QA role)

**Merge Strategy:**
1. Cell 61 as base (API description + purpose)
2. Add "Data Profiling & Quality Assessment"
3. Merge both criteria (100% completeness + 1.88% anomalies)
4. Consolidate conclusion (99.12% quality score + selective role)
5. Result: Single section (~160 lines)

**Output Structure:**
```
### DS5: Alpha Vantage Intraday API (Quality Assurance) - CONSOLIDATED
#### Description & Purpose
[Cell 61: API purpose + rate limits + profiling table]

#### Data Quality Assessment
**Criterion 1:** Data Completeness (DS1) ✅
[Cell 63 Criterion 1: 100% OHLCV completeness, no missing values]

**Criterion 2:** Volume Anomalies ⚠️
[Cell 63 Criterion 2: 1.88% spikes (real market events), 99.12% quality score]

#### Suitability Conclusion
🔍 **SELECTED FOR QUALITY ASSURANCE (Selective Use)**
[Cell 64: Monthly reconciliation role + rate limit constraints + backup strategy]
```

**Code Integration:**
- Include Cell 62 code showing anomaly detection logic
- Quality scoring function

**Information Preserved:**
- ✓ API capabilities and rate limits
- ✓ Data completeness metrics (100%)
- ✓ Anomaly detection approach
- ✓ Quality score (99.12%) and validation strategy

---

## DUPLICATE CELLS TO DELETE (PURE REDUNDANCY)

**Total Cells to Delete:** 11  
**Cells Deleted:** 14, 19, 23, 32-37, 38-41

| Original Cell # | Cell ID | Content | Reason for Deletion |
|---|---|---|---|
| 14 | #VSC-0f63e1e3 | Markdown separator ("---") | Pure navigation marker; consolidate with adjacent sections |
| 19 | #VSC-b0e825c1 | Markdown separator ("---") | Pure navigation marker; consolidate with adjacent sections |
| 23 | #VSC-1669f6ef | Markdown separator ("DS4 Header") | Pure separator; consolidate with merged DS4 section |
| 32 | #VSC-964eea08 | "Research Hypothesis" markdown | EXACT DUPLICATE of Cell 4 (Research Question Section 1.1) |
| 33 | #VSC-28562016 | "Data Requirements" markdown | EXACT DUPLICATE of Cell 5 (Data Source Identification) |
| 34 | #VSC-8a75764e | "Data Source Selection" markdown | EXACT DUPLICATE of Cell 6 (Data Source Justification) |
| 35 | #VSC-811c0ad2 | "Dataset Integration Table" markdown | LARGELY DUPLICATE of Cell 30 (integration summary) |
| 36 | #VSC-ebc8e0a2 | "Redundancy Decisions" markdown | DUPLICATE of redundancy section in Cell 30 |
| 37 | #VSC-78ef0ebe | "Project Overview" markdown | DUPLICATE of Executive Summary (Cell 3) |
| 38 | #VSC-b5073701 | "Section 1 Header" markdown | REDUNDANT header repeat (Section already marked in Cell 7) |
| 39 | #VSC-7c6c3a63 | "Research Hypothesis" markdown (SECOND INSTANCE) | DUPLICATE of Cells 4, 32 |
| 40 | #VSC-15c999e1 | "Data Requirements" markdown (SECOND INSTANCE) | DUPLICATE of Cells 5, 33 (THIRD INSTANCE) |
| 41 | #VSC-4c1b1b65 | "Data Source Selection" markdown (SECOND INSTANCE) | DUPLICATE of Cells 6, 34 (THIRD INSTANCE) |

**Total Information Loss:** 0% (all content already present in consolidated cells)

---

## CONSOLIDATION CELLS (KEEPING WITH MINOR MODIFICATIONS)

### Cells Kept as-is:
**Cells 1-13, 15-18, 20-22, 24-31, 42-50, 65+**

### Cells with Minor Edits:

**Cell 7 (#VSC-0ee6825a):** "Section 2: Prepare Phase" Header
- *Edit:* Change heading from subsection to main phase header
- *Before:* "## Section 2: Prepare Phase - Dataset Exploration (All 5 Datasets)"
- *After:* "## PREPARE PHASE: Data Exploration & Feature Engineering"
- *Why:* Standardize phase naming across notebook

**Cell 42 (#VSC-96c061db):** "Dataset Exploration Guidelines" 
- *Edit:* Add reference note linking to consolidated DS1-DS5 sections
- *Before:* General guidelines only
- *After:* Guidelines + note "See consolidated assessments below for DS1-DS5"
- *Why:* Maintain readability while pointing to merged sections

**Cell 107-108:** Duplicate Aggregation Descriptions
- *Edit:* DELETE both (consolidate with Cell 68)
- *Why:* Cells 107-108 are exact repeats of Cell 68 aggregation explanation

---

## FEATURE ENGINEERING CONSOLIDATION

### Cells 109-111: Feature Code Consolidation

**Situation:** Three cells (109, 110, 111) contain near-identical feature engineering code

**Cell 109 (#VSC-808c47b5):** Price Features (return, range, volume, volatility)  
**Cell 110 (#VSC-0b55fb0c):** Data Cleaning (outlier detection, anti-leakage)  
**Cell 111 (#VSC-2b2cb71f):** Feature Normalization (StandardScaler, feature selection)

**Consolidation Strategy:**
1. **KEEP Cell 109** as primary price features implementation
2. **MERGE Cell 110** into Cell 109:
   - If code is identical: DELETE Cell 110
   - If code differs slightly: Keep Cell 110 but add comment "Alternative approach: [brief description]"
3. **MERGE Cell 111** into Cell 109:
   - If code is identical: DELETE Cell 111
   - If code differs slightly: Keep Cell 111 but add comment "Normalization variant: [brief description]"

**Decision Rule:** 
- If >90% code overlap → DELETE duplicate
- If <90% overlap (unique logic) → KEEP both with clarifying comments

---

## REPRISE CELLS (EXPANDED DUPLICATE SECTIONS)

**Total Reprise Cells:** 18  
**Cells 44-64** represent expanded, more detailed versions of earlier cells

### Consolidation Strategy:

**For Each Reprise Set:**
1. Keep the **first occurrence** (condensed version) in Ask/early-Prepare
2. Delete the **reprise** (expanded version) from later Prepare sections
3. Cross-reference: "See detailed analysis below" → link to consolidated section

**Example: DS1 Reprises**
- **Cell 9** (#VSC-e794b946): DS1 condensed (2 criteria, brief)
- **Cells 44-46:** DS1 expanded (full description, metrics, detailed assessment)

**Decision:** 
- KEEP Cell 9 in overview section (quick reference)
- CONSOLIDATE Cells 44-46 into **single comprehensive section** (Position 13 in Prepare)
- Remove redundant "second reading" of DS1

---

## FINAL CELL COUNTS BY PHASE

| Phase | Original Range | New Range | Cells | Reduction |
|-------|---|---|---|---|
| **Ask** | 1-7 (+ duplicates 32-41) | 1-7 | 7 | 11 cells removed (duplicates) |
| **Prepare** | 8-65 (+ reprises 44-64) | 8-37 | 30 | 28 cells consolidated |
| **Analyze** | 66-147 (+ reprises 109-111) | 38-64 | 27 | 9 cells consolidated |
| **Share** | 148-166 | 65-83 | 19 | 0 cells (kept as-is) |
| **Conclude** | 167-189 | 84-111 | 28 | 0 cells (kept as-is) |
| **TOTAL** | **189 cells** | **~151 cells** | - | **38 cells reduced (20%)** |

---

## VERIFICATION CHECKLIST

After applying all merges, verify:

- [ ] **Cell 1-7 (Ask Phase):** Problem definition, hypothesis, data requirements (7 cells)
- [ ] **Cell 8-37 (Prepare Phase):** Consolidated DS1-DS5 explorations + feature summary (30 cells)
  - [ ] Cell 13: Consolidated DS1 (merged from 44-46)
  - [ ] Cell 14: Consolidated DS2 (merged from 47-49)
  - [ ] Cell 15: Consolidated DS3 (merged from 51-54)
  - [ ] Cell 16: Consolidated DS4 (merged from 56-59)
  - [ ] Cell 17: Consolidated DS5 (merged from 61-64)
- [ ] **Cell 38-64 (Analyze Phase):** Feature engineering, modeling, diagnostics (27 cells)
- [ ] **Cell 65-83 (Share Phase):** Results, findings, theory validation (19 cells)
- [ ] **Cell 84-111 (Conclude Phase):** Limitations, rubric, ethics, future work (28 cells)

**No Information Loss Check:**
- [ ] All DS1-DS5 content present in consolidated sections
- [ ] All feature engineering logic preserved
- [ ] All model code intact
- [ ] All results/findings present
- [ ] All limitations/ethics/rubric content included

**Structural Validation:**
- [ ] No cells out of dependency order
- [ ] All code cells have required inputs from prior cells
- [ ] Phase transitions clear and marked
- [ ] Cross-references updated where applicable

---

## IMPLEMENTATION SEQUENCE

**Step 1: Prepare** (Non-destructive)
- Create backup copy of DSF_draft.ipynb as DSF_draft_BACKUP.ipynb

**Step 2: Delete Duplicates** (11 cells)
- Remove Cells: 14, 19, 23, 32-41
- Verify: No information lost (all content in consolidated cells)

**Step 3: Merge Cells (5 major merges)**
- **Merge 1:** Cells 44-46 → Single consolidated DS1 section
- **Merge 2:** Cells 47-49 → Single consolidated DS2 section
- **Merge 3:** Cells 51-54 → Single consolidated DS3 section
- **Merge 4:** Cells 56-59 → Single consolidated DS4 section
- **Merge 5:** Cells 61-64 → Single consolidated DS5 section

**Step 4: Consolidate Feature Code** (3 cells)
- Evaluate Cells 109-111 for overlap
- DELETE if >90% identical, or KEEP with differentiation comments

**Step 5: Delete Reprises** (18 cells)
- Remove expanded versions from later Prepare sections
- Keep first occurrences as "quick reference"

**Step 6: Validate**
- Run notebook end-to-end
- Verify all variables created in expected order
- Check for look-ahead bias (temporal order integrity)
- Confirm all 189 cell contents preserved

---

## MERGE EXAMPLE (DETAILED)

### How to Merge Cells 44-46 (DS1 Consolidation)

**BEFORE (3 separate cells):**
```
CELL 44 (Markdown): ### 2.2 DS1: SPY Price Data...
[Description + metrics table + interpretation]

CELL 45 (Markdown): #### **Data Quality Assessment**
**Criterion 1: Completeness & Logical Consistency** ✅
[Content...]
**Criterion 2: Volume Anomalies** ⚠️
[Content...]

CELL 46 (Markdown): #### **Suitability Conclusion**
✅ **SELECTED FOR PRIMARY ANALYSIS**
[Content...]
```

**AFTER (1 consolidated cell):**
```
CELL 13 (Markdown): ### DS1: SPY Price Data (OHLCV Time Series)

#### Description & Profiling
The primary dataset contains 1-minute OHLCV bars for SPY spanning 3+ years...
[Full content from Cell 44]

#### Data Quality Assessment

**Criterion 1: Completeness & Logical Consistency** ✅
- No missing OHLCV values
- High ≥ Low constraint: 100% compliance
- [Full content from Cell 45 Criterion 1]

**Criterion 2: Volume Anomalies** ⚠️
- Volume outliers (>3σ): 1.88% of observations
- [Full content from Cell 45 Criterion 2]

#### Suitability Conclusion
✅ **SELECTED FOR PRIMARY ANALYSIS**
- Complete, high-frequency price data enables target variable construction
- [Full content from Cell 46]
```

---

This mapping provides the complete operational blueprint for reorganizing DSF_draft.ipynb while preserving 100% of content.
