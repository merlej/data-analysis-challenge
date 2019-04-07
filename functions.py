import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_corr_heat_map(data, ignore_cancelled = True):
    if ignore_cancelled:
        data = data[data['is_cancelled'] == 0].drop('is_cancelled', axis = 1)
    data_to_visualize = data[~data.isin([np.nan, np.inf, -np.inf]).any(1)]
    # Create Correlation df
    corr = data_to_visualize.corr()
    # Plot figsize
    fig, ax = plt.subplots(figsize=(15, 10))
    # Generate Color Map
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    # Generate Heat Map, allow annotations and place floats in map
    sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
    # Apply xticks
    plt.xticks(range(len(corr.columns)), corr.columns);
    # Apply yticks
    plt.yticks(range(len(corr.columns)), corr.columns)
    # show plot
    plt.show()
    
    


