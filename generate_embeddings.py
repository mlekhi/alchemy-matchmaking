import cohere
import csv
import numpy as np
import chromadb
import os
from dotenv import load_dotenv

# to generate embeddings, 1) initialize cohere client (and chroma), 2) read answers from csv,
# 3) compute cosine similarity for each individual answer

load_dotenv()
COHERE_API_KEY= os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

chroma_client = chromadb.PersistentClient(path="./chroma_db")  
collection = chroma_client.get_or_create_collection(name="attendee_answer_embeddings")

CSV_FILE = "cleaned_data.csv"

# reading csv
attendees = {}
questions = []
with open(CSV_FILE, newline='') as attendees_csv:
    data = csv.reader(attendees_csv, delimiter=',', quotechar='"')
    header = next(data)  
    questions = header[1:] 
    
    for row in data:
        name = row[0]  # name
        # print(name)
        answers = row[1:]  # question responses
        attendees[name] = answers  # storing by name

# print(attendees)
# print(questions)

person_embeddings = {} 
for name, answers in attendees.items():
    # filtering out unanswered
    valid_answers = [a for a in answers if a.strip() and a.strip().upper() != "NULL"]
    valid_questions = [q for q, a in zip(questions, answers) if a.strip() and a.strip().upper() != "NULL"]

    if not valid_answers: 
        continue

    # print(f"VALID ANSWERS: {valid_answers}")
    response = co.embed(texts=valid_answers, model="embed-english-light-v3.0", input_type="search_document")
    embeddings = response.embeddings  # one embedding per question
    
    person_embeddings[name] = {q: emb for q, emb in zip(valid_questions, embeddings)}  # ✅ Store correctly

    # chroma db save
    for q, emb, ans in zip(valid_questions, embeddings, valid_answers):
        collection.add(
            ids=[f"{name}_{q}"],  # ID == name{underscore}question
            embeddings=[emb],
            metadatas=[{"name": name, "question": q, "answer": ans}]
        )

# print(person_embeddings)
print("EMBEDDINGS STORED!")
