import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Sample DataFrame (replace with your actual data)
data = {
    'total_phn_adds_gross': [-1, 10, np.nan, 0, 5, np.nan, 20],
    'fwa_adds_gross': [-5, np.nan, 2, 0, np.nan, 1, 3],
    'mobile_to_fios_refferals_cnt': [1, 5, np.nan, np.nan, 2, np.nan, 7],
    'price_plan_step_up_cnt': [0, 10, 50, 0, 115, 20, 0],
    'connected_device_adds_gross': [-1, 0, 0, 0, 10, 0, 0],
    'total_upgrades_gross': [19, np.nan, 30, np.nan, 37, np.nan, 25],
    'total_perks_adds': [0, 0, 85, 0, 10, 0, 0]
}
df = pd.DataFrame(data)

df['ordinal_combined_score'] = 0.0

features = [
    'total_phn_adds_gross',
    'fwa_adds_gross',
    'mobile_to_fios_refferals_cnt',
    'price_plan_step_up_cnt',
    'connected_device_adds_gross',
    'total_upgrades_gross',
    'total_perks_adds'
]

for feature in features:
    # Initialize the transformed feature column
    df[f'{feature}_transformed'] = 0.0

    # Handle nulls
    df.loc[df[feature].isna(), f'{feature}_transformed'] = -1

    # Handle zeros (opportunity, no conversion)
    df.loc[(df[feature].notna()) & (df[feature] == 0), f'{feature}_transformed'] = 0

    # Handle non-zeros (opportunity, conversion)
    # Scale non-zero values to a range, e.g., 0 to 1, then add to the score.
    # Be careful with features that have negative values, you might want to adjust the base.
    non_zero_values = df.loc[(df[feature].notna()) & (df[feature] != 0), feature]
    if not non_zero_values.empty:
        # Normalize non-zero values to a specific range (e.g., 0 to 1)
        # Add a small constant to ensure all non-zero values are positive before scaling if negative values are present
        min_val = non_zero_values.min()
        if min_val < 0:
            scaler = MinMaxScaler(feature_range=(0.01, 1)) # Start above 0
            df.loc[(df[feature].notna()) & (df[feature] != 0), f'{feature}_transformed'] = \
                scaler.fit_transform(non_zero_values.values.reshape(-1, 1)).flatten()
        else:
            scaler = MinMaxScaler(feature_range=(0.1, 1)) # Start above 0
            df.loc[(df[feature].notna()) & (df[feature] != 0), f'{feature}_transformed'] = \
                scaler.fit_transform(non_zero_values.values.reshape(-1, 1)).flatten()


    df['ordinal_combined_score'] += df[f'{feature}_transformed']

print("\nDataFrame with 'ordinal_combined_score':")
print(df[['total_phn_adds_gross', 'fwa_adds_gross', 'ordinal_combined_score']])
