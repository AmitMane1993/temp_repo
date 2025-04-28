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

# Create overall figure
fig = plt.figure(figsize=(18, 7))
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

# Plot overall distribution
ax0 = fig.add_subplot(gs[0])
sns.histplot(data['value'], kde=True, ax=ax0)
ax0.set_title('Overall Distribution', fontsize=14)

# Create a new axis for FacetGrid
ax1 = fig.add_subplot(gs[1])

# Seaborn FacetGrid
g = sns.FacetGrid(data, col="category", col_wrap=2, sharex=False, sharey=False, height=3.5)
g.map(sns.histplot, "value", kde=True)

# Adjust layout
plt.tight_layout()
plt.show()
