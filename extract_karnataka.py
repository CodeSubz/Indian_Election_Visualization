import pandas as pd

# Read the main CSV
df = pd.read_csv('data/electiondata.csv')

# Filter for Karnataka
karnataka_df = df[df['state'] == 'Karnataka']

# Write to new CSV with header
karnataka_df.to_csv('data/secpageda_karnataka_full.csv', index=False)

print(f"Extracted {len(karnataka_df)} rows for Karnataka.")
