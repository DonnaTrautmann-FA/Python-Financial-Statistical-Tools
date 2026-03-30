import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv(r"C:\Users\donna\Documents\Python\Page_View_Time_Series_Visualizer\fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')


# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

df.count = lambda **kwargs: len(df)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")
    
  

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
   
   
    # Copy and modify data for monthly bar plot
    # create the long format table
    df_bar = df.copy()
    # define the months variable used for the pivot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    # transform the long format to a wide format matrix(group), unstack, & reindex
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack().reindex(columns=months)
    
    
    # Draw bar plot
    # .plot(kind='bar') automatically handles the X-axis and Legend
    fig = df_bar.plot(kind='bar', figsize=(12, 10)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    cols = ["year","month"]
    titles = ["Year-wise Box Plot (Trend)", "Month-wise Box Plot (Seasonality)"]
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, col, title in zip(axes, cols, titles):
        if col == "month":
            sns.boxplot(data=df_box,x=col,y="value", ax=ax, order=months)
        else:
            sns.boxplot(data=df_box,x=col,y="value", ax=ax)
        ax.set_title(title)
        ax.set_xlabel(col.capitalize())
        ax.set_ylabel("Page Views")
    plt.tight_layout()
    #plt.gcf() for testing
    #return fig for testing





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
