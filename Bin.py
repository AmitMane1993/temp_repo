import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame
# df = pd.DataFrame({
#     'col1': np.random.rand(100),
#     'col2': np.random.rand(100),
#     ...
# })

# Your column list
columns = ['col1', 'col2']  # Replace with your actual column names

# Define bins and labels
bins = np.linspace(0, 1, 11)  # Bins: [0.0, 0.1, 0.2, ..., 1.0]
labels = [f'{int(l*100)}-{int(r*100)}%' for l, r in zip(bins[:-1], bins[1:])]

# Plotting
for col in columns:
    data = df[col].dropna()
    
    # Normalize to [0, 1]
    norm_data = (data - data.min()) / (data.max() - data.min())
    
    # Bin the data
    binned = pd.cut(norm_data, bins=bins, labels=labels, include_lowest=True)
    
    # Count values in each bin
    value_counts = binned.value_counts().sort_index()
    
    # Plot
    plt.figure(figsize=(10, 5))
    value_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(f'Value Count in 10% Bins for {col}')
    plt.xlabel('Percentile Range')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


#№###########

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Your DataFrame and column name
# df = pd.DataFrame({'your_column': np.random.rand(100)})
column = 'your_column'

# Step 1: Calculate decile cut points (quantiles)
quantiles = df[column].quantile(np.linspace(0, 1, 11)).drop_duplicates()

# Step 2: Create labels (1 fewer than number of unique bins)
labels = [f'{int(i*100)}-{int(j*100)}%' for i, j in zip(quantiles.index[:-1], quantiles.index[1:])]

# Step 3: Cut the data into bins
binned = pd.cut(df[column], bins=quantiles.values, labels=labels, include_lowest=True)

# Step 4: Count the values in each bin
value_counts = binned.value_counts().sort_index()

# Display counts
print(value_counts)

# Step 5: Plot
value_counts.plot(kind='bar', color='teal', edgecolor='black')
plt.title(f'Value Count by Percentile Bins for "{column}"')
plt.xlabel('Percentile Range')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
###########

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Your DataFrame and column
# df = pd.DataFrame({'your_column': np.random.rand(100)})
column = 'your_column'

# Step 1: Calculate decile cut points (quantiles)
quantiles = df[column].quantile(np.linspace(0, 1, 11)).drop_duplicates()

# Step 2: Create labels (1 fewer than number of bins)
labels = [f'{int(i*100)}-{int(j*100)}%' for i, j in zip(quantiles.index[:-1], quantiles.index[1:])]

# Optional: Also keep actual value ranges to annotate
range_labels = [f'{round(i, 2)}–{round(j, 2)}' for i, j in zip(quantiles.values[:-1], quantiles.values[1:])]

# Step 3: Cut and count
binned = pd.cut(df[column], bins=quantiles.values, labels=labels, include_lowest=True)
value_counts = binned.value_counts().sort_index()

# Step 4: Plot
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(value_counts.index, value_counts.values, color='teal', edgecolor='black')

# Step 5: Annotate each bar with quantile value range
for bar, label in zip(bars, range_labels):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, label,
            ha='center', va='bottom', fontsize=9, rotation=0, color='black')

# Style the plot
ax.set_title(f'Value Count by Percentile Bins for "{column}"')
ax.set_xlabel('Percentile Range')
ax.set_ylabel('Count')
plt.xticks(rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
