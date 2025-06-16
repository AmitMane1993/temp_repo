import pandas as pd
import numpy as np

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

# Define a mapping for each state (adjust weights as needed)
# Lower value for null (no opportunity)
# Medium value for zero (opportunity, no conversion)
# Higher value for non-zero (opportunity, conversion)
state_weights = {
    'null': -1,  # Can be a negative value to represent a 'missed' opportunity
    'zero': 0.5, # Small positive value for opportunity but no conversion
    'non_zero': 2 # Higher positive value for successful conversion
}

df['weighted_combined_score'] = 0.0

features_info = {
    'total_phn_adds_gross': {'null_pct': 84, 'zero_pct': 2},
    'fwa_adds_gross': {'null_pct': 84, 'zero_pct': 8},
    'mobile_to_fios_refferals_cnt': {'null_pct': 91, 'zero_pct': 0},
    'price_plan_step_up_cnt': {'null_pct': 0, 'zero_pct': 6},
    'connected_device_adds_gross': {'null_pct': 0, 'zero_pct': 88},
    'total_upgrades_gross': {'null_pct': 84, 'zero_pct': 0},
    'total_perks_adds': {'null_pct': 0, 'zero_pct': 84}
}

for feature, info in features_info.items():
    # Apply weights based on state
    df[f'{feature}_score'] = df[feature].apply(lambda x:
                                               state_weights['null'] if pd.isna(x) else
                                               state_weights['zero'] if x == 0 else
                                               state_weights['non_zero'])
    df['weighted_combined_score'] += df[f'{feature}_score']

print("\nDataFrame with 'weighted_combined_score':")
print(df[['total_phn_adds_gross', 'fwa_adds_gross', 'weighted_combined_score']])
