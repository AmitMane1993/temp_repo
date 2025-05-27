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

# code 2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example DataFrames
# df_raw = ...
# df_cleaned = ...
# df_outliers_handled = ...

data_versions = {
    'Raw Data': df_raw,
    'Cleaned Data': df_cleaned,
    'Outlier Handled': df_outliers_handled
}

columns = df_raw.columns
sns.set(style='whitegrid')

def get_stats_text(series):
    desc = series.describe()
    return (f"min: {desc['min']:.2f} | 25%: {desc['25%']:.2f} | "
            f"50%: {desc['50%']:.2f} | 75%: {desc['75%']:.2f} | "
            f"max: {desc['max']:.2f} | mean: {desc['mean']:.2f} | "
            f"std: {desc['std']:.2f}")

for plot_type in ['box', 'dist']:
    n_cols = 3
    n_rows = len(columns)
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(6 * n_cols, 4.5 * n_rows))
    fig.suptitle(f"{plot_type.capitalize()} Plot Comparison with Summary Stats", fontsize=18, y=1.02)

    for i, col in enumerate(columns):
        for j, (label, df) in enumerate(data_versions.items()):
            ax = axes[i, j] if n_rows > 1 else axes[j]
            data = df[col].dropna()

            if plot_type == 'box':
                sns.boxplot(y=data, ax=ax)
            elif plot_type == 'dist':
                sns.histplot(data, kde=True, ax=ax, bins=30)

            ax.set_title(f"{col} - {label}", fontsize=12)
            # Add summary stats as text
            stats_text = get_stats_text(data)
            ax.text(0.5, -0.25, stats_text, fontsize=9, ha='center', va='top', transform=ax.transAxes, wrap=True)

    plt.tight_layout(rect=[0, 0.03, 1, 0.98])
    plt.show()

