import pandas as pd
from visualization import (
    plot_category_comparison,
    plot_yearly_trend,
    plot_top_papers
)

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("gate_cutoff.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Original Shape:", df.shape)

# ==========================
# Data Cleaning
# ==========================

# Remove unwanted column
if 'Unnamed: 0' in df.columns:
    df.drop('Unnamed: 0', axis=1, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df = df.ffill()

# Convert columns to numeric if needed
for col in ['GEN', 'OBC', 'SC/ST', 'Year']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Remove remaining null values
df.dropna(inplace=True)

# ==========================
# Outlier Removal (IQR)
# ==========================

for col in ['GEN', 'OBC', 'SC/ST']:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

print("Cleaned Shape:", df.shape)

# ==========================
# Save Cleaned Dataset
# ==========================

df.to_csv("cleaned_gate_cutoff.csv", index=False)

# ==========================
# Dataset Statistics
# ==========================

print("\nDataset Summary:\n")
print(df.describe())

# ==========================
# Visualizations
# ==========================

plot_category_comparison(df)
plot_yearly_trend(df)
plot_top_papers(df)

print("\nProject Completed Successfully!")