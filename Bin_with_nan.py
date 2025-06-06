import pandas as pd
import numpy as np

def quantile_binning_with_nulls_and_zeros(df, column, n_bins=4, zero_bin_label=-1, null_bin_label=-2):
    """
    Perform quantile binning on non-zero, non-null values using numeric labels.
    Assign separate labels for zero and null values.
    
    Parameters:
    - df: pandas DataFrame
    - column: column name to bin
    - n_bins: number of bins (excluding zero/null bins)
    - zero_bin_label: label for zero values
    - null_bin_label: label for null (NaN) values
    
    Returns:
    - pandas Series with bin labels as integers
    """
    data = df[column].copy()
    
    # Masks
    null_mask = data.isna()
    zero_mask = (data == 0) & (~null_mask)
    valid_mask = (~null_mask) & (~zero_mask)

    # Apply qcut on valid (non-zero, non-null) data
    valid_data = data[valid_mask]
    binned_valid = pd.qcut(valid_data, q=n_bins, labels=range(n_bins), duplicates='drop')

    # Create full bin series
    bins = pd.Series(index=data.index, dtype='float')  # Use float to allow for -1, -2, NaNs etc.
    bins[null_mask] = null_bin_label
    bins[zero_mask] = zero_bin_label
    bins[valid_mask] = binned_valid.astype(int)

    return bins.astype(int)

# Example usage
df = pd.DataFrame({
    'value': [0, 0, np.nan, 1, 2, 5, 8, 10, None, 12, 15, 18, 20]
})

df['binned'] = quantile_binning_with_nulls_and_zeros(df, 'value', n_bins=3)
print(df)
