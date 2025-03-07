import openai
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_CSV = "csvs/cleaned_data.csv"
OUTPUT_CSV = "csvs/cleaned_data_music.csv"

df = pd.read_csv(INPUT_CSV)
print(f"Loaded CSV with {len(df)} rows.")

# get 3 words describing the vibe of a song
def describe_song_vibe(song_name):
    if pd.isna(song_name) or song_name.strip() == "":
        print(f"Skipping empty song entry: {song_name}")
        return None

    print(f"Processing song: {song_name}")

    prompt = f"""
    Describe the overall vibe of the song "{song_name}" in exactly three words, separated by commas.
    Example format: "Energetic, Uplifting, Fun"
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a music analyst that summarizes song vibes in three words."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        response_text = response.choices[0].message.content.strip()
        print(f"Raw response: {response_text}")

        # response validation
        vibe_words = [word.strip() for word in response_text.split(",") if word.strip()]
        if len(vibe_words) == 3:
            result = ", ".join(vibe_words)
            print(f"Extracted Vibe: {result}")
            return result
        else:
            print(f"Unexpected response format for '{song_name}', skipping.")
            return None

    except Exception as e:
        print(f"Error processing '{song_name}': {str(e)}")
        return None

df["Hype Song Vibe"] = df["Hype Song"].astype(str).apply(describe_song_vibe)

df.to_csv(OUTPUT_CSV, index=False)

print(f"Updated CSV saved as {OUTPUT_CSV}")
