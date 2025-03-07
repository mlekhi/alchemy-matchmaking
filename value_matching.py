import openai
import pandas as pd
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found. Set OPENAI_API_KEY in your .env file.")

INPUT_CSV = "csvs/cleaned_data_music.csv"
OUTPUT_CSV = "csvs/cleaned_data_music_values.csv"

df = pd.read_csv(INPUT_CSV)

def classify_text(response):
    if pd.isna(response) or response.strip() == "":
        return {"formal": None, "emotional": None}

    prompt = f"""
    Analyze the following text response and provide certainty scores (0-1) for:
    - Formal (1 = very formal, 0 = very informal)
    - Emotional (1 = highly expressive, 0 = neutral or logical)

    Response: "{response}"

    Return the result in **valid JSON format**, with the keys "formal" and "emotional" containing numerical values.

    Example format:
    {{
        "formal": 0.5,
        "emotional": 0.8
    }}
    """

    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a strict JSON generator. Always output valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        response_text = response.choices[0].message.content.strip()
        print(f"🔍 Raw API Response: {response_text}")

        # ensure valid JSON
        try:
            result = json.loads(response_text)
            return {"formal": result.get("formal"), "emotional": result.get("emotional")}
        except json.JSONDecodeError:
            print(f"❌ JSON parsing error for response: {response_text}")
            return {"formal": None, "emotional": None, "error": "Invalid JSON response"}

    except Exception as e:
        print(f"❌ API Error: {str(e)}")
        return {"formal": None, "emotional": None}

formal_scores, emotional_scores = [], []

for _, row in df.iterrows():
    all_responses = " ".join(str(row[col]) for col in ["Learning Interest", "Past Work", "Talk Forever", "Hype Song"] if pd.notna(row[col]))

    if all_responses.strip():
        scores = classify_text(all_responses)
        formal_scores.append(scores.get("formal"))
        emotional_scores.append(scores.get("emotional"))
    else:
        formal_scores.append(None)
        emotional_scores.append(None)

# Add new columns to the original DataFrame
df["formal"] = formal_scores
df["emotional"] = emotional_scores

# Save to CSV
df.to_csv(OUTPUT_CSV, index=False)
