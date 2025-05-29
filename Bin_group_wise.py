import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example setup
# df = pd.read_csv("your_data.csv") or define your df
column = 'your_column'  # Numeric column to analyze
group_col = 'pa_group_name'  # Categorical grouping column

# Group by the categorical column
for group, group_df in df.groupby(group_col):
    print(f"\nPlotting for group: {group}")
    
    # Drop NA for the selected numeric column
    data = group_df[column].dropna()
    
    if data.nunique() < 2:
        print(f"  Skipping group '{group}' due to insufficient unique data.")
        continue

    # Step 1: Quantile cut points (10 bins)
    quantiles = data.quantile(np.linspace(0, 1, 11)).drop_duplicates()

    # Skip if not enough bins
    if len(quantiles) < 2:
        print(f"  Skipping group '{group}' due to too few quantiles.")
        continue

    # Step 2: Create percentile labels
    labels = [f'{int(i*100)}-{int(j*100)}%' for i, j in zip(quantiles.index[:-1], quantiles.index[1:])]
    range_labels = [f'{round(i, 2)}–{round(j, 2)}' for i, j in zip(quantiles.values[:-1], quantiles.values[1:])]

    # Step 3: Bin and count
    binned = pd.cut(data, bins=quantiles.values, labels=labels, include_lowest=True)
    value_counts = binned.value_counts().sort_index()

    # Step 4: Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(value_counts.index, value_counts.values, color='teal', edgecolor='black')

    # Annotate bars with quantile range
    for bar, label in zip(bars, range_labels):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1, label,
                ha='center', va='bottom', fontsize=9, rotation=0, color='black')

    # Plot styling
    ax.set_title(f'Value Count by Percentile Bins for "{column}"\nGroup: {group}')
    ax.set_xlabel('Percentile Range')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
