import pandas as pd

INPUT_CSV = "data.csv"
OUTPUT_CSV = "csvs/cleaned_data.csv"

df = pd.read_csv(INPUT_CSV)

selected_columns = {
    "name": "Name",
    "email": "Email",
    "what is something you’ve always wanted to learn about but haven’t started yet? (detail is highly encouraged!)": "Learning Interest",
    "what's the last thing you worked on that you're proud of? (detail is highly encouraged!)": "Past Work",
    "what's something you could talk about forever? (detail is highly encouraged!)": "Talk Forever",
    "what's your hype song?": "Hype Song"
}
df_cleaned = df[list(selected_columns.keys())].rename(columns=selected_columns)

df_cleaned = df_cleaned.drop_duplicates(subset=["Name"], keep="first")

df_cleaned = df_cleaned.replace(["NULL", "null", "None", "none"], "").fillna("")

non_matching_columns = ["Learning Interest", "Past Work", "Talk Forever", "Hype Song"]
df_cleaned = df_cleaned[~(df_cleaned[non_matching_columns] == "").all(axis=1)]

# save cleaned CSV
df_cleaned.to_csv(OUTPUT_CSV, index=False)