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

# Example: Replace with your actual DataFrame and column name
# df = pd.DataFrame({'your_column': np.random.rand(100)})
column = 'your_column'

# Calculate 10-percentile bins (deciles)
quantile_bins = np.linspace(0, 1, 11)
quantile_labels = [f'{int(q*100)}-{int((q+0.1)*100)}%' for q in quantile_bins[:-1]]

# Create decile cut points using quantiles of the actual data
cut_points = df[column].quantile(quantile_bins).values

# Bin the data using those quantiles
binned = pd.cut(df[column], bins=cut_points, labels=quantile_labels, include_lowest=True, duplicates='drop')

# Count values in each bin
value_counts = binned.value_counts().sort_index()

# Display counts
print(value_counts)

# Plot
value_counts.plot(kind='bar', color='teal', edgecolor='black')
plt.title(f'Value Count by Percentile Bins for "{column}"')
plt.xlabel('Percentile Range')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
