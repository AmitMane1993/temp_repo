import pandas as pd
import numpy as np

# Sample DataFrame (replace with your actual data)
df = pd.DataFrame({
    'total_phn_adds_gross': [np.nan, 5, 0, 15, np.nan],
    'fwa_adds_gross': [1, -3, np.nan, 2, 0],
    'mobile_to_fios_refferals_cnt': [np.nan, np.nan, np.nan, 5, 2],
    'price_plan_step_up_cnt': [0, 10, 20, 30, 0],
    'connected_device_adds_gross': [0, 0, 0, 5, 10],
    'total_upgrades_gross': [np.nan, np.nan, 25, 32, np.nan],
    'total_perks_adds': [0, 5, 10, 0, 85],
})

# Step 1: Normalize each column (Min-Max scaling excluding nulls)
def normalize_column(col):
    valid = col.dropna()
    min_val, max_val = valid.min(), valid.max()
    return (col - min_val) / (max_val - min_val)

normalized_df = df.copy()
for col in df.columns:
    normalized_df[col] = normalize_column(df[col])

# Step 2: Compute mean of available (non-null) normalized values row-wise
df['kpi_score'] = normalized_df.mean(axis=1, skipna=True)

# Show result
print(df[['kpi_score']])

weights = {
    'total_phn_adds_gross': 1,
    'fwa_adds_gross': 1,
    'mobile_to_fios_refferals_cnt': 1,
    'price_plan_step_up_cnt': 1,
    'connected_device_adds_gross': 1,
    'total_upgrades_gross': 1,
    'total_perks_adds': 1,
}

# Multiply each normalized value by weight, sum, then divide by sum of weights (ignoring nulls)
weighted_sum = np.zeros(len(df))
weight_sum = np.zeros(len(df))

for col, weight in weights.items():
    valid = normalized_df[col].notnull()
    weighted_sum += normalized_df[col].fillna(0) * weight
    weight_sum += valid.astype(int) * weight

df['weighted_kpi_score'] = weighted_sum / weight_sum

