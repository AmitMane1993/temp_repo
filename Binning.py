import pandas as pd
import numpy as np

def quantile_binning_with_zeros(df, column, n_bins=4, zero_bin_label='zero_bin'):
    """
    Perform quantile binning on non-zero values while assigning a separate bin to zero values.
    
    Parameters:
    - df: pandas DataFrame
    - column: column name to bin
    - n_bins: number of bins (excluding the zero bin)
    - zero_bin_label: label to assign to zero bin
    
    Returns:
    - pandas Series with bin labels
    """
    # Copy to avoid changing original
    data = df[column].copy()
    
    # Mask for zeros
    zero_mask = data == 0
    
    # Non-zero data
    non_zero_data = data[~zero_mask]
    
    # Apply qcut on non-zero values
    binned_non_zero = pd.qcut(non_zero_data, q=n_bins, duplicates='drop')
    
    # Create full bin series
    bins = pd.Series(index=data.index, dtype='object')
    bins[zero_mask] = zero_bin_label
    bins[~zero_mask] = binned_non_zero.astype(str)
    
    return bins

# Example usage
df = pd.DataFrame({
    'value': [0, 0, 0, 1, 2, 5, 8, 10, 12, 15, 18, 20]
})

df['binned'] = quantile_binning_with_zeros(df, 'value', n_bins=3)
print(df)
