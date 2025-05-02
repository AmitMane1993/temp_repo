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


##########

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec

# Create dummy DataFrame with 8 columns
df = pd.DataFrame(np.random.randn(1000, 8), columns=[f'col{i}' for i in range(1, 9)])

fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 2, width_ratios=[1, 2])  # Left:1, Right:2 width ratio

# Left subplot - full height
ax0 = plt.subplot(gs[:, 0])
col_main = 'col1'
ax0.hist(df[col_main], bins=30, color='skyblue', edgecolor='black')
stats = df[col_main].describe()
textstr = '\n'.join((
    f'Count: {int(stats["count"])}',
    f'Mean: {stats["mean"]:.2f}',
    f'Median: {df[col_main].median():.2f}',
    f'Std: {stats["std"]:.2f}',
    f'Min: {stats["min"]:.2f}',
    f'Max: {stats["max"]:.2f}'))
ax0.text(0.95, 0.95, textstr, transform=ax0.transAxes,
         fontsize=10, verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax0.set_title(f'Histogram of {col_main}')
ax0.set_xlabel(col_main)
ax0.set_ylabel('Frequency')

# Right subplots - 4x2 grid (fits 8 subplots, we use 7)
gs_right = gridspec.GridSpecFromSubplotSpec(4, 2, subplot_spec=gs[:, 1], hspace=0.5, wspace=0.4)

cols = df.columns[1:]  # col2 to col8
for i, col in enumerate(cols):
    ax = plt.Subplot(fig, gs_right[i])
    fig.add_subplot(ax)
    ax.hist(df[col], bins=20, color='lightgreen', edgecolor='black')
    
    # Add statistics text
    stats = df[col].describe()
    textstr = '\n'.join((
        f'N: {int(stats["count"])}',
        f'Mean: {stats["mean"]:.2f}',
        f'Median: {df[col].median():.2f}',
        f'Std: {stats["std"]:.2f}',
        f'Min: {stats["min"]:.2f}',
        f'Max: {stats["max"]:.2f}'))
    ax.text(0.95, 0.95, textstr, transform=ax.transAxes,
            fontsize=8, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    ax.set_title(col, fontsize=10)
    ax.tick_params(axis='x', labelrotation=30)
    ax.tick_params(axis='y', labelsize=8)

plt.tight_layout()
plt.show()

