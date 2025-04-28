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

# Set up the figure and the main gridspec
fig = plt.figure(figsize=(18, 7))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

# Overall distribution on the left
ax0 = fig.add_subplot(gs[0])
sns.histplot(data['value'], kde=True, ax=ax0)
ax0.set_title('Overall Distribution')

# Right side: divide into 4 subplots
gs_right = gridspec.GridSpecFromSubplotSpec(2, 2, subplot_spec=gs[1])

categories = data['category'].unique()
for i, cat in enumerate(categories):
    ax = fig.add_subplot(gs_right[i])
    sns.histplot(data[data['category'] == cat]['value'], kde=True, ax=ax)
    ax.set_title(f'Category {cat}')

plt.tight_layout()
plt.show()
