# Page View Time Series Visualizer

This project is a data visualization pipeline built using Python, Pandas, Matplotlib, and Seaborn. It processes and analyzes time-series traffic data from the freeCodeCamp.org online forum between May 2016 and December 2019. 

The tool performs data cleaning to eliminate statistical outliers and generates three distinct visualizations to uncover growth trends, monthly variation, and yearly seasonality patterns.

---

## Visualizations Generated

1. **Line Plot:** Shows daily forum traffic growth over time, tracking overall trajectory from 2016 to 2019.
2. **Bar Plot:** Groups daily page views into monthly averages for each year to compare year-over-year growth per calendar month.
3. **Box Plots:** Side-by-side comparison displaying structural distribution data. The year-wise plot reveals long-term trends, while the month-wise plot reveals recurring annual seasonality.

---

## Data Pipelines & Integrity

To ensure clean statistical modeling, the dataset undergoes an initial cleaning phase to filter out anomalies:
* Rows where page views fall outside the **top 2.5%** or **bottom 2.5%** of the dataset are removed.
* This removes temporary traffic spikes (such as major external promotions) and anomalies (such as system downtime) to leave a stable, true reflection of platform growth.

---

## How to Run This Project

This project is structured to run self-contained. The dataset (`fcc-forum-pageviews.csv`) should be placed directly inside the project directory, allowing the script to find and process data using relative pathways.

### 1. Clone or Download the Repository
Clone this repository to your local machine or download the project files directly into a workspace folder.

### 2. Install Dependencies
Ensure you have the required standard data analysis and visualization libraries installed in your execution environment:

```
Bash
pip install pandas matplotlib seaborn
```
### 3. Execution
Open your terminal or command prompt, navigate to the directory containing the files, and run the main Python script:

```
Bash
python time_series_visualizer.py
```
(The script will automatically read the local csv file, execute the cleaning filters, and output three high-resolution files: line_plot.png, bar_plot.png, and box_plot.png directly into the folder.)

Output Gallery
1. Daily Growth (Line Plot)
2. Monthly Distribution Across Years (Bar Plot)
3. Trend and Seasonality Analysis (Box Plots)

***

