import pandas as pd

# Convert date columns to datetime if not already
df['start_dt'] = pd.to_datetime(df['start_dt'])
df['end_dt'] = pd.to_datetime(df['end_dt'])

# Create a 'month' column
df['month'] = df['start_dt'].dt.to_period('M')

# Define the months you're interested in
existing_months = ['2023-11', '2023-12', '2024-01', '2024-02']
missing_months = ['2024-03', '2024-04']
all_alert_cols = [col for col in df.columns if col.startswith('alert_cnt')]

# Filter only data from existing months
df_existing = df[df['month'].astype(str).isin(existing_months)]

# Compute mean for each emp_eid across existing months
df_mean = df_existing.groupby('emp_eid')[all_alert_cols].mean().reset_index()

# Create missing month rows for each emp_eid
imputed_rows = []
for month in missing_months:
    for _, row in df_mean.iterrows():
        entry = row.copy()
        entry['emp_eid'] = row['emp_eid']
        entry['start_dt'] = pd.to_datetime(f'{month}-01')
        entry['end_dt'] = pd.to_datetime(f'{month}-28')  # assuming end of month
        entry['month'] = pd.Period(month)
        imputed_rows.append(entry)

# Convert list of rows to DataFrame
df_imputed = pd.DataFrame(imputed_rows)

# Combine original and imputed data
df_final = pd.concat([df, df_imputed], ignore_index=True).sort_values(['emp_eid', 'start_dt'])

# Optional: Drop 'month' column if not needed
df_final.drop(columns='month', inplace=True)

# Final imputed dataframe
print(df_final)
