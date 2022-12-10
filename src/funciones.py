import pandas as pd
import numpy as np
from numpy import nan
import re
import pylab as plt
import seaborn as sns

def check_nan(df: pd.DataFrame) -> None:
    
    nan_cols=df.isna().mean() * 100  # el porcentaje
    
    display(f'N nan cols: {len(nan_cols[nan_cols>0])}')
    display(nan_cols[nan_cols>0])
    
    plt.figure(figsize=(10, 6))  # inicia la figura y establece tamaño

    sns.heatmap(df.isna(),  # mapa de calor
                yticklabels=False,
                cmap='viridis',
                cbar=False)

    plt.show();
    
def check_value(df: pd.DataFrame, cols) -> None:
    for x in cols:
        print(df[x].value_counts().head())
        
def check_unique(df: pd.DataFrame, cols) -> None:
    for x in cols:
        print(df[x].unique())