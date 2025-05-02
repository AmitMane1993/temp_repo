import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec

# Create dummy DataFrame with 8 columns
df = pd.DataFrame(np.random.randn(1000, 8), columns=[f'col{i}' for i in range(1, 9)])

fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 2])  # 2 rows, 2 columns; right plot is wider

# Left subplot - plot histogram for the first column
ax0 = plt.subplot(gs[:, 0])  # span both rows
ax0.hist(df['col1'], bins=30, color='skyblue', edgecolor='black')
ax0.set_title('Histogram of col1')

# Right subplots - plot histograms for remaining 7 columns
gs_right = gridspec.GridSpecFromSubplotSpec(4, 2, subplot_spec=gs[:, 1])  # 4x2 grid inside right subplot

axes_right = []
cols = df.columns[1:]  # col2 to col8
for i, col in enumerate(cols):
    ax = plt.Subplot(fig, gs_right[i])
    fig.add_subplot(ax)
    ax.hist(df[col], bins=20, color='lightgreen', edgecolor='black')
    ax.set_title(f'{col}')
    axes_right.append(ax)

plt.tight_layout()
plt.show()
