Welcome to my analytics and statistical computing portfolio. This repository serves as an active environment for data processing pipelines, visualization tools, and statistical modeling. 

Below is a centralized technical cross-reference index detailing the exact libraries, statistical concepts, and data-manipulation methods implemented across each project.

---

## 🛠️ Global Library Reference Index

| Library | Primary Use Case in Portfolio | Key Methods/Modules Used |
| :--- | :--- | :--- |
| **Pandas** | Data ingestion, outlier filtering, data reshaping, and matrix aggregation. | `pd.read_csv()`, `.quantile()`, `.groupby()`, `.unstack()`, `.reindex()` |
| **Matplotlib** | Low-level canvas architecture, custom trend line rendering, and multi-plot axis grids. | `plt.subplots()`, `ax.plot()`, `fig.savefig()`, `ax.set()` |
| **Seaborn** | High-level statistical visualization, distribution spreads, and multi-variable comparison. | `sns.boxplot()` |
| **SciPy** | Advanced statistical modeling, linear regression calculus, and trend projections. | `scipy.stats.linregress` |

---

## 📂 Project Component & Syntax Ledger

### 1. Page View Time Series Visualizer
* **Core Concept:** Time-series cleaning, identifying growth trajectories, and detecting distribution trends/seasonality across multiple years.
* **Imports:** `pandas`, `matplotlib.pyplot`, `seaborn`

#### Key Code Snippets & Syntax Quick-Reference:
* **Symmetric Outlier Trimming (Filter top/bottom 2.5%):**
  ```
  Python
  df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
  ```
* **Reshaping Long Data to a Wide Matrix (Year/Month Pivot):**
```
Python
df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack().reindex(columns=months)
```
* **Looping Multi-Axis Seaborn Subplots side-by-side:**
```
Python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
for ax, col, title in zip(axes, cols, titles):
    sns.boxplot(data=df_box, x=col, y="value", ax=ax)
```
### 2. Sea Level Predictor
* **Core Concept: Scatter plot analysis, calculating historical line-of-best-fit parameters, and extrapolating future predictive trends through the year 2050.**

* **Imports: pandas, matplotlib.pyplot, scipy.stats.linregress**

#### Key Code Snippets & Syntax Quick-Reference:
* **Executing Linear Regression Calculus:**
```
Python
# Extracts slope, intercept, and standard error variables from the data
lin_re = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
```
* **Projecting Extrapolated Trend Lines (Using Range Arrays):**
```
Python
x_pred = pd.Series([i for i in range(1880, 2051)])
y_pred = lin_re.slope * x_pred + lin_re.intercept
ax.plot(x_pred, y_pred, 'r', label='1880-2050 Trend')
```
* **Filtering Data Based on Recent Timeline Breakpoints:**
```
Python
df_recent = df[df['Year'] >= 2000]
```
### 3. Demographic Data Analyzer
* **Core Concept: Demographic profiling, categorical percentage breakdowns, and macro-financial dataset filtering using multi-conditional index tracking.**

* **Imports: pandas**

#### Key Code Snippets & Syntax Quick-Reference:
* **Calculating Clean Categorical Percentages:**
```
Python
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
pay_over_50k = len(higher_education[higher_education['salary'] == '>50K'])
percentage = round((pay_over_50k / len(higher_education)) * 100, 1)
```
* **Locating Maximum Values relative to a matching Identifier:**
```
Python
highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
```

