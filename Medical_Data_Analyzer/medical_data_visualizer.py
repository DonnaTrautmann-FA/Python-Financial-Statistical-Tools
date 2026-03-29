import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
                        
# 1
df = pd.read_csv(r"C:\Users\donna\Documents\Python\Medical_Data_Visualizer\medical_examination.csv")

# 2
df['overweight'] = np.where((df['weight'] / ((df['height']/100)) ** 2) >25, 1, 0 ) 

# 3
df[['cholesterol','gluc']] = (df[['cholesterol','gluc']] >1).astype(int)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = 'total')
    

    # 7
    g = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar")

    # 8
    fig = g.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ] #.drop(columns=['id']) for my own visual

    # 12
    corr = df_heat.corr()
    

                
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))      #, k=0 for my visual


    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={"shrink": .5},
        ax = ax
        )
    #these next 2 lines are for my visual
    #ax.set_xticklabels([label.get_text() if i != len(corr)-1 else "" for i, label in enumerate(ax.get_xticklabels())], rotation=45, ha='right')
    #ax.set_yticklabels([label.get_text() if i != 0 else "" for i, label in enumerate(ax.get_yticklabels())])

    

    # 16
    fig.savefig('heatmap.png')
    return fig

