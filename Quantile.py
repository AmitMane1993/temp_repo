import pandas as pd
import numpy as np

# Example: Your 7 feature columns
selected_cols = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7']
n_quantiles = 4  # You can change this to 3, 5, etc.

def transform_column(col, n_quantiles=4):
    # Step 1: Replace nulls with 1
    col_filled = col.fillna(1)

    # Step 2: Identify values > 0 (eligible for quantile binning)
    mask = col_filled > 0

    # Step 3: Apply quantile binning only on values > 0
    try:
        binned = pd.qcut(
            col_filled[mask], 
            q=n_quantiles, 
            labels=range(2, 2 + n_quantiles),
            duplicates='drop'  # Handles fewer unique values
        )
        col_filled.loc[mask] = binned.astype(int)
    except ValueError:
        # If not enough unique values for quantile binning
        col_filled.loc[mask] = 2  # or assign a fixed category

    return col_filled.astype(int)

# Apply transformation to each column
for col in selected_cols:
    df[col + '_cat'] = transform_column(df[col])
