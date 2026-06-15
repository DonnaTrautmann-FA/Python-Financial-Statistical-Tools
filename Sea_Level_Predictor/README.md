# Data Analysis with Python: Sea Level Predictor
## Project Overview
This project analyzes global average sea level change data from 1880 through the present, utilizing historical data from the 
US Environmental Protection Agency (EPA). Using Python, Pandas, and SciPy's regression tools, this application models historical trends 
and projects future sea level changes through the year 2050. 
The analysis explores two distinct temporal scales to highlight how the rate of sea level rise is accelerating in the modern era.
## Key Insights & Analytical Approach
* **Long-Term Trend (1880–2050):** A linear regression model built on the full 130+ year timeline establishes a historical baseline
* rate of change.
* **Modern Acceleration (2000–2050):** A secondary regression model isolates data from the year 2000 onward. By restricting the
* temporal scope, the model exposes an accelerated rate of change (a steeper slope) compared to the long-term historical baseline.
* **Data Sourcing Evaluation:** While this project standardizes on the `CSIRO Adjusted Sea Level` column (coastal tidal gauges)
* for complete historical compliance, the repository contains notes on incorporating `NOAA Adjusted Sea Level`
* (satellite altimetry data) for modern comparative analysis.
---
## Visual Output
The script generates a multi-layered visualization saved as `sea_level_plot.png`:
1. **Scatter Plot:** Historical sea level measurements mapped out by year.
2. **Baseline Model (Red Line):** Linear regression line of best fit reflecting trends from 1880 to the present, projected to 2050.
3. **Accelerated Model (Purple Line):** Linear regression line of best fit reflecting modern trends from 2000 to the present,
4. projected to 2050.
---
## Technologies Used
* **Python 3.14**
* **Pandas:** For data manipulation, data cleaning, and dataset filtering.
* **Matplotlib:** For programmatic, layered data visualization and canvas management.
* **SciPy (`linregress`):** For executing scientific standard linear regressions to extract slopes, intercepts, and standard errors.
---
## Repository Structure
```text
├── epa-sea-level.csv        # Historical sea level source dataset
├── sea_level_predictor.py   # Main Python script containing plotting logic
├── sea_level_plot.png       # Final exported visualization 
└── README.md                # Project documentation

How to Run This Project
This project is structured to run self-contained.
The dataset (`epa_sea_level.csv`) is included directly inside the project folder,
allowing the script to find and process the data automatically without absolute
local path configurations.
### 1. Clone or Download the Repository
Clone this repository to your local machine or download the project files directly into a workspace folder.
### 2. Install Dependencies
Ensure you have the required standard scientific computing libraries installed in your environment:
```bash
pip install pandas matplotlib scipy```
### 3. Execution
Open your terminal or command prompt.
Navigate to the project directory where the files are located and execute the python script:
Bash
```python sea_level_predictor.py```
(The script will automatically read the bundled epa-sea-level.csv file,
generate the predictive visualization trends, save the resulting image as
sea_level_plot.png, and display the canvas interface.)



Future Reference & Extensibility Notes
This repository contains pre-configured, commented-out code blocks designed for future educational extensions, including:
Confidence Interval (CI) Bands: Framework for utilizing lin_re.intercept_stderr and ax.fill_between() to programmatically
paint a translucent variance corridor underneath the trend line, establishing a visual standard error tolerance.
