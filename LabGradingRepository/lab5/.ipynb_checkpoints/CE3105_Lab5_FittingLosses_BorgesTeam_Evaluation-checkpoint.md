
# CE 3105 Laboratory Report Evaluation  
**Lab 5: Fitting Losses in a Pipe System**  
**Team Members:** Henrique Borges, David Santiago Cantor, Mitchell Lester, Srihari Saravanan  
**Instructor:** Dr. Theodore Cleveland  
**Score: 91 / 100**

---

##  General Feedback

This report presents a clear, technically sound analysis of fitting losses in pipe systems. The team accurately applies the relevant theory and computes loss coefficients for various fittings. A well-structured discussion supports the numerical results, and the team correctly identifies major error sources. Some data tables are only partially populated or referenced but not shown, and there are minor inconsistencies in unit formatting and result interpretation that slightly impact clarity. Overall, this is a strong and effective report.

---

##  Section-by-Section Evaluation

### 1. **Objective and Introduction** — **10/10**
-  Well-framed objective explaining energy losses due to pipe fittings.
-  Contextualized within real-world applications (HVAC, water distribution).

### 2. **Theory and Background** — **10/10**
-  Clearly presents Darcy-Weisbach and K-loss equations.
-  Good use of visual references and theoretical summaries.

### 3. **Materials and Procedure** — **10/10**
-  Calibration, leak checks, flow rate procedures (manual and automated), and pressure drop measurements are well described.
-  Manometer and Raspberry Pi flowmeter use noted.

### 4. **Results and Data Analysis** — **8/10**
-  Good presentation of flow rate and manometer readings.
- Tables referenced (e.g., Table 4–7) are not shown or filled in the document.
- K-values discussed but not explicitly tabulated or plotted, which limits data transparency.
- Some confusion over diameter usage for expansion/contraction fittings not resolved in results narrative.

### 5. **Discussion** — **9/10**
-  Accurately describes trends across fittings (e.g., mitre > contraction > expansion > elbow).
-  Suggests flow disruptions as source of higher K-values.
- Inconsistent use of singular/plural in K-value summary (“lowest lost coefficients”).
- Trial 1 anomalies not specifically shown but mentioned.

### 6. **Conclusion** — **10/10**
-  Solid summary emphasizing design relevance and agreement with textbook expectations.
-  Recommends instrumentation and procedural improvements.

### 7. **Error Analysis** — **10/10**
-  Thoughtful enumeration of air bubbles, human reaction timing, and volume accuracy.
-  Recognizes cumulative nature of instrumentation error.

### 8. **References and Attribution** — **9/10**
-  Reference to the course lab manual is present.
-  Effort sheet filled out with team contributions.
- One member did not sign; future submissions should ensure full signatures.

### 9. **Clarity, Style, Grammar** — **5/10**
- Several formatting artifacts remain (e.g., “Table 4: Flow Rate Table” has no table).
- Some inconsistent phrasing and incomplete integration of visuals into text.

---

##  Suggested Results Summary Table (To Add for Clarity)

| Fitting              | Avg. K (Observed) | Expected K Range | Notes                          |
|----------------------|-------------------|------------------|--------------------------------|
| Mitre Bend           | High (not shown)  | 1.0 – 2.0        | Sharp turn, consistent with trend |
| Long-Sweep Elbow     | Low (not shown)   | 0.2 – 0.6        | Likely the lowest K             |
| Expansion Fitting    | Moderate          | 0.3 – 1.0        | Direction of velocity unclear   |
| Contraction Fitting  | Moderate-High     | 0.4 – 1.2        | Vena contracta expected         |

---

## Final Score: **91 / 100**

###  **Strengths**
- Clear understanding of fitting losses
- Good procedure and instrumentation narrative
- Strong conclusions and error analysis

###  **Areas to Improve**
- Include populated tables and K-value summary
- Clarify expansion/contraction diameter interpretation
- Improve clarity of result presentation and polish document formatting


