import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# Define your column list and group column
column_list = ['col1', 'col2']  # Replace with your numeric columns
group_col = 'pa_group_name'    # Your grouping column

# Loop through each numeric column
for column in column_list:
    print(f"\nProcessing column: {column}")
    
    # Get unique groups
    groups = df[group_col].dropna().unique()
    num_groups = len(groups)
    
    # Prepare subplot layout (e.g., 2x3 for 6 groups)
    cols = 2
    rows = math.ceil(num_groups / cols)
    
    fig, axes = plt.subplots(rows, cols, figsize=(cols*6, rows*4), squeeze=False)
    fig.suptitle(f'Quantile Distribution for "{column}" by Group', fontsize=16)
    
    # Iterate through each group and plot in subplot
    for idx, group in enumerate(groups):
        row, col_idx = divmod(idx, cols)
        ax = axes[row][col_idx]
        
        group_df = df[df[group_col] == group]
        data = group_df[column].dropna()
        
        # Skip if too few unique values
        if data.nunique() < 2:
            ax.set_visible(False)
            continue
        
        quantiles = data.quantile(np.linspace(0, 1, 11)).drop_duplicates()
        if len(quantiles) < 2:
            ax.set_visible(False)
            continue
        
        # Create labels
        labels = [f'{int(i*100)}-{int(j*100)}%' for i, j in zip(quantiles.index[:-1], quantiles.index[1:])]
        range_labels = [f'{round(i, 2)}–{round(j, 2)}' for i, j in zip(quantiles.values[:-1], quantiles.values[1:])]

        binned = pd.cut(data, bins=quantiles.values, labels=labels, include_lowest=True)
        value_counts = binned.value_counts().sort_index()

        # Plot
        bars = ax.bar(value_counts.index, value_counts.values, color='steelblue', edgecolor='black')
        ax.set_title(f'Group: {group}')
        ax.set_xlabel('Percentile Range')
        ax.set_ylabel('Count')
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Annotate bars
        for bar, label in zip(bars, range_labels):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 1, label,
                    ha='center', va='bottom', fontsize=8)
    
    # Hide any unused subplots
    for idx in range(num_groups, rows * cols):
        row, col_idx = divmod(idx, cols)
        axes[row][col_idx].set_visible(False)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
