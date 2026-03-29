# Medical Data Visualizer

### Project Overview
This project involves conducting a **Visual Audit** of a medical dataset containing patient information, body measurements, and lifestyle habits. The goal was to clean the data by filtering out statistical outliers (blood pressure and height/weight extremes) and visualize the correlations between health factors like cholesterol, smoking, and cardiovascular disease.

### Key Objectives
* **Data Reconciliation:** Filtered data to ensure physiological consistency (e.g., ensuring diastolic pressure is lower than systolic).
* **Categorical Analysis:** Created a `catplot` to show the distribution of health markers (cholesterol, glucose, etc.) split by cardiovascular outcomes.
* **Correlation Matrix:** Developed a 14-variable heatmap to identify "Moderate Positive Correlations" between lifestyle choices and medical results.

### Technical Stack
* **Language:** Python 3.x
* **Libraries:** * **Pandas:** For data manipulation and quantile-based filtering.
    * **Matplotlib / Seaborn:** For generating the 13x13 correlation matrix and categorical "staircase" plots.
    * **NumPy:** Utilized for upper-triangle masking logic in the heatmap.

---

### Data Cleaning Methodology
To ensure the integrity of the "Medical Ledger," the following filters were applied:
1.  **Diastolic vs. Systolic:** Removed records where `ap_lo > ap_hi`.
2.  **Height/Weight Outliers:** Removed patients falling below the 2.5th percentile or above the 97.5th percentile to eliminate data entry errors.

### Visualizations

#### 1. Categorical Plot
Displays the counts of "good" vs. "bad" health outcomes for active, alcohol, cholesterol, gluc, overweight, and smoke, partitioned by the target variable `cardio`.

#### 2. Heat Map
A correlation matrix utilizing a mask to hide the redundant upper triangle, showing the Pearson correlation coefficients for all 14 variables.

---

### Certification Context
This project was completed as part of the **freeCodeCamp Data Analysis with Python** certification. It demonstrates proficiency in:
* Handling **List Slicing** and **Indexing** for data visualization.
* Managing **Floating Point Precision** in statistical reporting.
* Using **Default Parameters** in complex library functions.

---

### How to Run
1. Ensure you have Python and the required libraries installed:
```bash
pip install pandas seaborn matplotlib numpy
