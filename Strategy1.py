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

# Create the new feature
df['combined_engagement_score'] = 0

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
    # 1. Add score if opportunity existed (not null)
    df['combined_engagement_score'] += df[feature].notna().astype(int)

    # 2. Add extra score if conversion happened (non-zero and not null)
    df['combined_engagement_score'] += ((df[feature].notna()) & (df[feature] != 0)).astype(int)

    # Optional: Add a small penalty/score for opportunity but no conversion (zero and not null)
    # df['combined_engagement_score'] += ((df[feature].notna()) & (df[feature] == 0)).astype(int) * 0.5 # Example, adjust weight

print("DataFrame with 'combined_engagement_score':")
print(df)
