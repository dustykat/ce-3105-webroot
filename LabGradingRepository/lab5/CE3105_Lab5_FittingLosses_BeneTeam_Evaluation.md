
# CE 3105 Laboratory Report Evaluation  
**Lab 5: Fitting Losses in Pipe Systems**  
**Team Members:** Aaron Bene, Clayton Folletti, Maxwell Manskie  
**Instructor:** Dr. Theodore Cleveland  
**Score: 94 / 100**

---

## General Feedback

This report demonstrates a solid understanding of pipe fitting losses and applies both manual and electronic data collection techniques effectively. The team correctly implements flow measurements, derives K-values for fittings, and offers meaningful interpretations tied to theoretical benchmarks. The report is well-structured and the error discussion is thorough. Some formatting clarity and graph/data visualization improvements would further strengthen it.

---

##  Section-by-Section Evaluation

### 1. **Objective and Introduction** — **10/10**
-  Well-articulated objective with a strong emphasis on real-world application of minimizing energy loss in pipe networks.
-  Practical motivation tied to fluid efficiency and pump system design.

### 2. **Theory and Background** — **10/10**
-  Includes sound derivation of K-values, including contraction/expansion theory.
-  References importance of R/D ratios and head loss correlation.

### 3. **Materials and Methods** — **10/10**
-  Good procedural breakdown using both stopwatch and Raspberry Pi flow data.
-  Clearly explains fitting sequence and manometer use.

### 4. **Results and Data Analysis** — **8/10**
-  Provides head loss values, velocities, and includes example K-value calculations.
-  Observes and flags negative head loss values, appropriately converting to positive.
- Final summary table with K-values per fitting is implied but not included — would be useful for quick comparison.
- Plots and figures are referenced but not embedded or captioned clearly.

### 5. **Discussion** — **9/10**
-  Correct ranking and trend interpretation of fittings: Bend > Elbow > Mitre > Contraction > Expansion.
-  Theoretical vs experimental values discussed, with attention to R/D effects and turbulence.
- Negative K-values briefly addressed — could expand explanation or propose instrumentation limitations more formally.

### 6. **Conclusion** — **10/10**
-  Clearly summarizes findings and offers good design implications for real systems.
-  Correctly identifies large-radius bends as most efficient fitting.

### 7. **References and Attribution** — **10/10**
-  Proper course reference provided and effort sheet included with signatures.

### 8. **Clarity, Style, Grammar** — **7/10**
- Several typos, minor grammar issues, and inconsistencies in table units/labels.
- Better equation formatting and graph integration would increase technical polish.

---

##  Suggested Summary Table (To Include)

| Fitting              | K (Reported) | Theoretical K | Notes                              |
|----------------------|--------------|----------------|------------------------------------|
| Mitre                | ~1.5         | ~1.3           | Higher, likely due to turbulence   |
| Elbow                | ~1.8         | ~0.9           | Significantly high, geometry-dependent |
| Bend                 | ~2.2         | 0.2–0.5        | High due to tight radius           |
| Expansion            | ~0.38        | ~0.16          | Slightly elevated, expected        |
| Contraction          | ~1.3         | ~0.2           | Vena contracta effect observed     |

---

##  Final Score: **94 / 100**

###  **Strengths**
- Accurate experimental execution and theoretical foundation
- Strong discussion and real-world insight
- Signed effort sheet and consistent group coordination

###  **Areas to Improve**
- Include final K-value summary table and more formal plot integration
- Polish grammar and formatting throughout
- Expand discussion of outliers and possible measurement inaccuracies


