import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec

# Example data
np.random.seed(0)
data = pd.DataFrame({
    'value': np.concatenate([
        np.random.normal(0, 1, 250),
        np.random.normal(3, 1, 250),
        np.random.normal(-2, 1, 250),
        np.random.normal(5, 1, 250)
    ]),
    'category': ['A']*250 + ['B']*250 + ['C']*250 + ['D']*250
})

# Function to compute and format summary stats
def get_stats_text(values):
    return (f"Mean: {values.mean():.2f}\n"
            f"Median: {values.median():.2f}\n"
            f"Min: {values.min():.2f}\n"
            f"Max: {values.max():.2f}\n"
            f"Std: {values.std():.2f}")

# Set up figure
fig = plt.figure(figsize=(18, 7))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

# Left: Overall distribution
ax0 = fig.add_subplot(gs[0])
sns.histplot(data['value'], kde=True, ax=ax0)
ax0.set_title('Overall Distribution')

# Add text with stats
stats_text = get_stats_text(data['value'])
ax0.text(0.05, 0.95, stats_text, transform=ax0.transAxes,
         verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))

# Right: 4 subplots
gs_right = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=gs[1])

# Initialize first axis
first_ax = fig.add_subplot(gs_right[0])
sns.histplot(data[data['category'] == 'A']['value'], kde=True, ax=first_ax)
first_ax.set_title('Category A')

# Add stats text
cat_values = data[data['category'] == 'A']['value']
stats_text = get_stats_text(cat_values)
first_ax.text(0.05, 0.95, stats_text, transform=first_ax.transAxes,
              verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))

# Create other axes, sharing x and y with first_ax
categories = data['category'].unique()
axes = [first_ax]

for i, cat in enumerate(categories[1:], 1):
    ax = fig.add_subplot(gs_right[i], sharex=first_ax, sharey=first_ax)
    sns.histplot(data[data['category'] == cat]['value'], kde=True, ax=ax)
    ax.set_title(f'Category {cat}')
    
    # Add stats text
    cat_values = data[data['category'] == cat]['value']
    stats_text = get_stats_text(cat_values)
    ax.text(0.05, 0.95, stats_text, transform=ax.transAxes,
            verticalalignment='top', bbox=dict(boxstyle="round", facecolor="white", alpha=0.7))
    
    axes.append(ax)

# Clean x/y labels
for ax in axes:
    if not ax.is_last_row():
        ax.set_xlabel('')
    if not ax.is_first_col():
        ax.set_ylabel('')

plt.tight_layout()
plt.show()
