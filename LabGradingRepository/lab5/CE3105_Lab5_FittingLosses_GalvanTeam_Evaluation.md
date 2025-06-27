
#  CE 3105 Laboratory Report Evaluation  
**Lab 5: Measurement of Fitting Losses in a Pipe System**  
**Team Members:** Parker Galvan, Tristen Martin, Kyle Spinks, Jorden Zarate  
**Instructor:** Dr. Theodore Cleveland  
**Score: 97 / 100**

---

##  General Feedback

This report is a model submission. The team demonstrates a clear understanding of the principles behind fitting losses and applies both theory and computation effectively. The results, including calculated K-values and comparisons to theoretical expectations, are well supported and documented. The report’s organization, depth of analysis, and reflection on potential improvements reflect a high level of engagement and skill.

---

##  Section-by-Section Evaluation

### 1. **Objective and Introduction** — **10/10**
- Comprehensive and well-contextualized.
- Clearly articulates experimental goals, flow principles, and instrumentation strategy.

### 2. **Theory and Background** — **10/10**
- Includes all relevant fluid mechanics equations and concepts (Darcy-Weisbach, velocity head, area ratios).
- Covers loss coefficient expectations across fitting types (bends, expansions, contractions).

### 3. **Materials and Methods** — **10/10**
- Flowrate measured using both stopwatch and Raspberry Pi flowmeter.
- Procedure clearly differentiates between flow and pressure measurements.
- Proper safety and calibration steps included.

### 4. **Results and Data Analysis** — **9/10**
- K-values computed for each fitting using appropriate velocity and head loss.
- Tables and figures are well-structured and clear.
- Loss coefficients for expansion/contraction were significantly lower than expected (0.001), which should be more critically flagged as anomalous or systematically offset.
- Velocity diameter reference (upstream vs. downstream) could be reinforced in the K calculation discussion.

### 5. **Discussion** — **10/10**
- Strong explanation for loss coefficient trends with geometry.
- Demonstrates understanding of how radius-to-diameter ratio (R/D) affects energy loss.
- Addresses observed vs. expected values with sound engineering reasoning.

### 6. **Conclusion** — **10/10**
- Accurately summarizes experimental findings, confirms theory, and reflects on practical implications.
- Effectively justifies why some fittings are preferable in design contexts.

### 7. **Error Analysis and Recommendations** — **10/10**
- Covers manometer difficulty, air bubbles, timing discrepancies, and unit conversion sources.
- Suggestions for digital instrumentation and repeat trials are practical and actionable.

### 8. **References and Attribution** — **8/10**
- Effort report included and signed.
- Minor redundancy in reference formatting (e.g., OpenAI citation).
- Could expand citations to include more technical sources (e.g., ASHRAE or AWWA guides).

### 9. **Clarity, Style, Grammar** — **10/10**
- Well written and formatted throughout.
- Figures, equations, and tables are clearly referenced and explained.

---

##  Results Summary Table (From Report)

| Fitting              | Avg. K (Experimental) | Expected K Range | Notes                            |
|----------------------|------------------------|-------------------|----------------------------------|
| Mitre Bend           | ~2.7                   | 1.4 – 1.6         | Higher than expected; sharp bend |
| Standard Elbow       | ~1.4                   | 1.1 – 1.4         | Within expected range            |
| Long-Sweep Elbow     | ~0.65 – 0.75           | 0.2 – 0.8         | Excellent agreement              |
| Expansion Fitting    | ~0.001                 | 0.3 – 1.0         | Possibly underestimated          |
| Contraction Fitting  | ~0.0007 – 0.0009       | 0.4 – 1.2         | Likely measurement/systematic error |

---

##  Final Score: **97 / 100**

###  **Strengths**
- High quality of computation and presentation
- Excellent theoretical linkage and practical insight
- Professional formatting and structured workflow

###  **Areas to Improve**
- More critically flag outlier K-values (especially for expansion/contraction)
- Clarify upstream/downstream velocity conventions


