Awesome! Here's how you can automate Chi-Square test and Cramér’s V for all the groups like the ones shown in your heatmaps.


---

Step-by-Step Python Code

Assuming your dataframe is named df and has these columns:

'Group' — the team/efficiency group (e.g., "2025 CS CX Eff 4/1")

'Positive_FWA_Activations'

'gross_adds_fwa_cnt'


1. Function to Compute Chi-Square and Cramér's V

import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np

def cramers_v(confusion_matrix):
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    r, k = confusion_matrix.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1)))

def analyze_group_relationship(df, group_col, cat1, cat2):
    results = []
    for group_name, group_data in df.groupby(group_col):
        table = pd.crosstab(group_data[cat1], group_data[cat2])
        chi2, p, dof, expected = chi2_contingency(table)
        v = cramers_v(table)
        results.append({
            "Group": group_name,
            "Chi2": round(chi2, 3),
            "p-value": round(p, 5),
            "Cramer's V": round(v, 3),
            "Interpretation": interpret_strength(v)
        })
    return pd.DataFrame(results)

def interpret_strength(v):
    if v < 0.1:
        return "Weak"
    elif v < 0.3:
        return "Moderate"
    elif v < 0.5:
        return "Strong"
    else:
        return "Very Strong"

2. Run the Analysis

results_df = analyze_group_relationship(
    df,
    group_col='Group',
    cat1='Positive_FWA_Activations',
    cat2='gross_adds_fwa_cnt'
)

print(results_df)
