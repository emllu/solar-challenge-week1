# app/utils.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    """Load and combine cleaned CSV files."""
    try:
        benin = pd.read_csv('data/benin_clean.csv')
        sierraleone = pd.read_csv('data/sierraleone_clean.csv')
        togo = pd.read_csv('data/togo_clean.csv')
        
        benin['Country'] = 'Benin'
        sierraleone['Country'] = 'Sierra Leone'
        togo['Country'] = 'Togo'
        
        combined = pd.concat([benin, sierraleone, togo], ignore_index=True)
        return combined
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: {e}. Ensure CSV files are in the 'data/' folder.")

def get_top_regions(combined, metric='GHI', n=3):
    """Return a table of top regions by average metric."""
    return combined.groupby('Country')[metric].mean().sort_values(ascending=False).head(n).reset_index()

def plot_boxplot(combined, metric='GHI', countries=None):
    """Generate a boxplot for the specified metric and countries."""
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    
    if countries:
        data = combined[combined['Country'].isin(countries)]
    else:
        data = combined
    
    sns.boxplot(x='Country', y=metric, data=data, hue='Country', palette='Set2')
    plt.title(f'{metric} Distribution by Country')
    plt.xlabel('Country')
    plt.ylabel(f'{metric} (W/m²)')
    return plt.gcf()