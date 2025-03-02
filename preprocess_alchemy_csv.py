import pandas as pd

# Constants
INPUT_CSV = "data.csv"
OUTPUT_CSV = "cleaned_data.csv"

# Load CSV
df = pd.read_csv(INPUT_CSV)

# Select relevant columns with cleaned names
selected_columns = {
    "name": "Name",
    "what is something you’ve always wanted to learn about but haven’t started yet? (detail is highly encouraged!)": "Learning Interest",
    "what's the last thing you worked on that you're proud of? (detail is highly encouraged!)": "Past Work",
    "what's something you could talk about forever? (detail is highly encouraged!)": "Talk Forever",
    "what's your hype song?": "Hype Song"
}
df_cleaned = df[list(selected_columns.keys())].rename(columns=selected_columns)

# Handle missing values (replace NaN with empty string or "NULL")
df_cleaned = df_cleaned.fillna("NULL")

# Save cleaned CSV
df_cleaned.to_csv(OUTPUT_CSV, index=False)

print(f"Cleaned CSV saved as {OUTPUT_CSV}")