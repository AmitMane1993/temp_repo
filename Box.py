import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have the following dataframes
# df_raw: raw data
# df_cleaned: cleaned data (missing values filled)
# df_outliers_handled: outliers handled

# Combine them in a dict for easy iteration
data_versions = {
    'Raw Data': df_raw,
    'Cleaned Data': df_cleaned,
    'Outlier Handled': df_outliers_handled
}

columns = df_raw.columns

# Set plot style
sns.set(style='whitegrid')

# Create boxplots and distribution plots
for plot_type in ['box', 'dist']:
    n_cols = 3  # raw, cleaned, outlier-handled
    n_rows = len(columns)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows))
    fig.suptitle(f"{plot_type.capitalize()} Plot Comparison", fontsize=16, y=1.02)

    for i, col in enumerate(columns):
        for j, (label, df) in enumerate(data_versions.items()):
            ax = axes[i, j] if n_rows > 1 else axes[j]
            if plot_type == 'box':
                sns.boxplot(y=df[col], ax=ax)
            elif plot_type == 'dist':
                sns.histplot(df[col], kde=True, ax=ax, bins=30)
            ax.set_title(f"{col} - {label}")

    plt.tight_layout()
    plt.show()
