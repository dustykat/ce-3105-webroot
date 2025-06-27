from pathlib import Path

# Markdown evaluation content for the Lab 5 report from Le team
markdown_content_30 = """
#  CE 3105 Laboratory Report Evaluation  
**Lab 5: Fitting Losses in Pipe Systems**  
**Team Members:** Hien Le, Daesen Kemp, Nimat Amoussa  
**Instructor:** Dr. Theodore Cleveland  
**Score: 91 / 100**

---

##  General Feedback

This report demonstrates a strong grasp of fitting loss principles and delivers a thorough set of experimental observations. The team includes detailed measurements and performs consistent K-value calculations across fittings. The report structure is effective, and the discussion provides a thoughtful interpretation of the deviations from expected values. The primary limitations are unusually high loss coefficients, which should be more critically discussed and linked to flow measurement error or unit mis...

---

##  Section-by-Section Evaluation

### 1. **Objective and Introduction** — **10/10**
-  Clear articulation of the experiment’s purpose.
-  Connects measurement with practical design considerations.

### 2. **Theory and Background** — **9/10**
-  Solid inclusion of equations and fluid mechanics concepts.
- Could benefit from more contextual values for expected K-ranges for each fitting.

### 3. **Materials and Methods** — **10/10**
-  Complete listing of equipment and procedures.
-  Both volumetric and automated flow measurements described.

### 4. **Results and Data Analysis** — **8/10**
-  K-values clearly presented in tables for each reading ID.
-  Flowrates and head losses systematically varied.
- Some K-values for standard fittings (e.g., mitre, elbow) are 20x theoretical—need to be flagged as suspicious.
- Graphs are mentioned but under-labeled and not fully embedded in the narrative.

### 5. **Discussion** — **9/10**
-  Attempts to reconcile discrepancies between experimental and theoretical K-values.
-  Notes fitting geometry and flow instability as contributors to variation.
- Anomalies (e.g., K = 47 for mitre) should be contextualized more rigorously—was this due to velocity basis? misaligned manometers?

### 6. **Conclusion** — **10/10**
-  Clearly summarizes results, theoretical alignment, and experimental limitations.
-  Includes strong takeaways on fluid energy loss and practical system design.

### 7. **References and Attribution** — **9/10**
-  Informal citations to course materials and textbook.
- Would benefit from inclusion of outside technical references or standards (e.g., Crane TP-410 or Moody chart).

### 8. **Clarity, Style, Grammar** — **6/10**
- Some equations are hard to follow due to formatting issues.
- Plot and table formatting could be improved for readability.
- Language is clear but would benefit from revision for precision and flow in technical writing.

---

## Summary of Observed K-Values (Reading ID 1 Example)

| Fitting              | K (Reported) | Theoretical Range | Comment                          |
|----------------------|--------------|-------------------|----------------------------------|
| Mitre Bend           | 47.4         | 1.4 – 1.6         | Extremely high – possible error |
| Elbow                | 18.5         | 1.1 – 1.4         | Too high – investigate velocity or Δh |
| Large Radius Bend    | 8.9          | 0.2 – 0.8         | Significantly above expected     |
| Expansion            | 6.26         | ~0.3              | Possibly valid for flow instability |
| Contraction          | 19.96        | ~0.6 – 1.2        | Very high – confirm Δh and velocity |

---

## Final Score: **91 / 100**

### **Strengths**
- Detailed data collection with strong experimental procedure
- Well-organized and logically structured
- Thoughtful discussion of trends and losses

### **Areas to Improve**
- Provide more rigorous justification for high K-values
- Clarify formatting and embed plots more effectively
- Add technical references for K-value expectations and standards

# Save the markdown file
file_path_30 = Path("/mnt/data/CE3105_Lab5_FittingLosses_LeTeam_Evaluation.md")
file_path_30.write_text(markdown_content_30)

file_path_30.name
