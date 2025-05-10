## 1. **High-Level Blueprint**

1. **Data Ingestion & Validation**
   - Load CSV files.
   - Validate input formats and column names.
   - Handle missing or null fields.

2. **Preprocessing & Cleaning**
   - Normalize text fields (remove stop words, handle punctuation, etc.).
   - Rename columns for consistency.
   - Export a cleaned dataset for downstream tasks.

3. **Embedding Generation**
   - Load Cohere's english light model or similar embedding model.
   - Convert each participant's responses into vector embeddings.
   - Store the embeddings in a local vector database (ChromaDB).

4. **Matching & Scoring Logic**
   - Similarity-based matching (e.g., “What do you want to learn?”).
   - Dissimilarity-based matching for diversity (e.g., “What’s the last thing you worked on?”).
   - Cross-matching (e.g., “Learning” ↔ “Talk about forever”).
   - Generate pairwise or group-based match scores.

5. **House Assignments**
   - Use clustering (K-Means, Spectral Clustering, etc.) to split participants into three houses.
   - Ensure diversity in skillsets and experiences.

6. **Summaries (Optional)**
   - Summarize participant data (e.g., GPT-based text summarization).
   - Integrate these summaries back into the matching pipeline as needed.

7. **Deploying the Frontend**
   - Use Vercel to host a minimal frontend that displays match results.
   - Provide a user interface to filter and view participant matches.

8. **Testing Strategy**
   - **Unit Tests**: Validate CSV ingestion, preprocessing, and embedding generation.
   - **Integration Tests**: Ensure end-to-end data flow from CSV to match results.
   - **Match Accuracy Tests**: Verify that the system correctly identifies similar and dissimilar participants.

---

## 2. **Breaking Down into Iterative Chunks**

1. **Setup & Environment**
   - Set up the project directory and environment (Python, dependencies, etc.).
   - Initialize a testing framework (e.g., Pytest).

2. **Data Ingestion & Validation**
   - Write a module to load CSV files.
   - Validate columns and handle missing data.

3. **Preprocessing & Cleanup**
   - Build a cleaning module to handle text normalization.
   - Test it with sample data.

4. **Embedding Generation**
   - Implement a function to load Cohere's model.
   - Generate embeddings for each row in the cleaned dataset.
   - Store embeddings in ChromaDB.

5. **Matching & Scoring**
   - Implement a similarity function (cosine similarity).
   - Implement a dissimilarity logic (1 - cosine similarity).
   - Implement cross-matching logic.
   - Test with small sets of mock data.

6. **House Assignment**
   - Write a module that clusters participants into three houses.
   - Validate cluster diversity.

7. **Summaries (Optional Feature)**
   - Integrate summarization logic (e.g., GPT-based).
   - Rebuild or augment embeddings if needed.

8. **Deployment**
   - Set up a minimal frontend with Vercel.
   - Connect the back-end data or local JSON results to the UI.

9. **Testing & Validation**
   - Ensure each step is covered by tests.
   - Final integration tests.

---

## 3. **Refining Each Chunk into Smaller Steps**

Below, each of the eight chunks is expanded into more granular tasks.

### 3.1 **Setup & Environment**
1. Create a new Git repository.
2. Create and activate a Python virtual environment.
3. Install necessary dependencies (e.g., `pip install chromadb sentence-transformers pytest sklearn pandas`).
4. Initialize a basic file structure (e.g., `src/`, `tests/`, `scripts/`).
5. Create a dummy test to verify that Pytest runs successfully.

### 3.2 **Data Ingestion & Validation**
1. Create a `data_ingestion.py` module.
2. Write a function `load_csv(filepath)` that returns a DataFrame.
3. Write a function `validate_columns(df, required_columns)` that raises an error if columns are missing.
4. Test the module with a small sample CSV.

### 3.3 **Preprocessing & Cleanup**
1. Create a `preprocessing.py` module.
2. Write a function `clean_text(text)` to strip punctuation, handle casing, etc.
3. Write a function `clean_dataframe(df)` that applies `clean_text` to relevant columns and replaces NaN with "NULL".
4. Save the cleaned result to a new CSV (e.g., `cleaned_data.csv`).
5. Test using synthetic or sample data.

### 3.4 **Embedding Generation**
1. Create an `embedding.py` module.
2. Initialize a Sentence-BERT model (e.g., `sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')`).
3. Write a function `generate_embeddings(df, columns_to_embed)` that returns a list of embeddings.
4. Integrate with ChromaDB:
   - Create or connect to a ChromaDB collection.
   - Insert embeddings and associated metadata (e.g., participant name).
5. Test by retrieving a vector from the DB and asserting its shape.

### 3.5 **Matching & Scoring**
1. Create a `matching.py` module.
2. Write `compute_similarity(embedding1, embedding2)` using cosine similarity.
3. Write `compute_dissimilarity(embedding1, embedding2)` as `1 - similarity`.
4. For each participant, generate top-N most similar or dissimilar matches.
5. Write unit tests with mock embeddings to verify correct similarity/dissimilarity values.

### 3.6 **House Assignment**
1. Create a `house_assignment.py` module.
2. Implement a clustering method (e.g., K-Means) with `n_clusters=3`.
3. Assign each participant to a cluster (house).
4. Validate that each house is non-empty.
5. Optionally, check diversity by verifying a range of embeddings or past work columns.

### 3.7 **Summaries (Optional Feature)**
1. Create a `summaries.py` module.
2. Implement a function `summarize_responses(df)` that calls a GPT-based model for short summaries.
3. Integrate summaries back into the dataset (or in a new column).
4. If using summaries for matching, generate new embeddings and repeat the store/insert steps.
5. Test on small data to confirm it completes without errors.

### 3.8 **Deployment**
1. Build a minimal React or static JavaScript frontend in a `frontend/` directory.
2. Write code in `frontend/` to load match results (from a local JSON or an API endpoint).
3. Deploy to Vercel using `vercel deploy`.
4. Test the deployment to confirm that the site displays the data.

---

## 4. **Reviewing & Right-Sizing the Steps**

- Each of these smaller tasks can be developed and tested in isolation.
- They build on each other: ingestion → cleaning → embeddings → matching → etc.
- None of the tasks is too large to handle. Testing is introduced immediately (Pytest from the start).
- We have optional expansions (summaries) that do not block core functionality.

This should provide a smooth, test-driven path from raw CSV data to a fully functional matchmaking system.

---

## 5. **Series of Prompts for Code-Generation LLM**

Below, each prompt section is shown in **code blocks** (using triple backticks and specifying `text` as the language). These prompts are structured for incremental development. You can feed each prompt in sequence to your code-generation LLM.

### 5.1 **Prompt 1: Project Setup & Environment**

```
text
You are an AI pair programmer. We are starting a new project for a matchmaking system. Please:

1. Initialize a new Python project with the following structure:
   - src/
   - tests/
   - scripts/
2. Create a Python virtual environment and install the following packages:
   - chromadb
   - sentence-transformers
   - pytest
   - sklearn
   - pandas
3. Provide a dummy test in tests/test_basic.py that simply checks that 1 + 1 == 2.
4. Include a short README.md describing the project setup.

Use best practices for setting up a Python project. Output the relevant files in your response, including the dummy test and a basic README.
```

### 5.2 **Prompt 2: Data Ingestion & Validation**

```
text
We have set up the environment. Next steps:

1. Create a module at src/data_ingestion.py containing two functions:
   - load_csv(filepath: str) -> pd.DataFrame
   - validate_columns(df: pd.DataFrame, required_columns: List[str]) -> None

2. Write a Pytest file at tests/test_data_ingestion.py with:
   - A test that checks loading of a small CSV (mock or embedded CSV content).
   - A test that verifies validate_columns raises an error if columns are missing.
   - A test that verifies validate_columns does not raise an error when columns are present.

3. Provide inline comments explaining each step. 
4. Return the content of src/data_ingestion.py and tests/test_data_ingestion.py in your response.
```

### 5.3 **Prompt 3: Preprocessing & Cleanup**

```
text
We have the ingestion and validation done. Now we need to clean and normalize text:

1. Create a module at src/preprocessing.py with functions:
   - clean_text(text: str) -> str
   - clean_dataframe(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame
     * This function applies clean_text to all rows in the specified columns, replaces NaN with "NULL", and returns the cleaned DataFrame.

2. Write Pytest file tests/test_preprocessing.py to:
   - Verify clean_text removes punctuation and normalizes case.
   - Verify clean_dataframe handles NaN and applies clean_text properly.

3. Return the code for src/preprocessing.py and tests/test_preprocessing.py in your response.
```

### 5.4 **Prompt 4: Embedding Generation**

```
text
Now let's handle embeddings with Sentence-BERT and ChromaDB:

1. Create src/embedding.py with:
   - A function load_embedding_model() -> Any that loads 'sentence-transformers/all-MiniLM-L6-v2'.
   - A function generate_embeddings(df: pd.DataFrame, columns_to_embed: List[str]) -> List[List[float]] that iterates over rows, concatenates relevant columns, and returns embeddings.

2. Integrate with ChromaDB:
   - In the same module, create function store_embeddings_in_chromadb(embeddings: List[List[float]], metadata: List[Dict[str, str]]), which:
     * Initializes or connects to a ChromaDB collection named "matchmaking".
     * Inserts each embedding with corresponding metadata (like participant name).

3. Create tests/test_embedding.py to:
   - Mock a small DataFrame.
   - Check that generate_embeddings returns the correct number of embeddings.
   - Use store_embeddings_in_chromadb in a test to confirm insertion. 
   - (If needed, mock ChromaDB or use a local test instance.)

4. Return relevant code for src/embedding.py and tests/test_embedding.py.
```

### 5.5 **Prompt 5: Matching & Scoring**

```
text
Next, we implement matching logic:

1. Create src/matching.py with:
   - compute_similarity(vec1: List[float], vec2: List[float]) -> float using cosine similarity.
   - compute_dissimilarity(vec1: List[float], vec2: List[float]) -> float, which is 1 - similarity.
   - match_participants(embeddings: Dict[str, List[float]]) -> Dict[str, List[Tuple[str, float]]], which:
     * For each participant, finds top-N most similar participants and top-N most dissimilar participants.
     * Return a dictionary mapping each participant’s name to lists of (other_participant, score).

2. Create tests/test_matching.py to:
   - Mock a small dictionary of embeddings (2-3 participants).
   - Verify compute_similarity and compute_dissimilarity are correct for known vectors.
   - Verify match_participants returns the correct top matches.

3. Return code for src/matching.py and tests/test_matching.py.
```

### 5.6 **Prompt 6: House Assignment**

```
text
Now we need to group people into three houses:

1. Create src/house_assignment.py with:
   - assign_houses(embeddings: Dict[str, List[float]], n_clusters=3) -> Dict[str, int]
     * Use a clustering algorithm (K-Means from sklearn) to cluster participants.
     * Return a dictionary mapping each participant to a house index (0, 1, or 2).

2. Create tests/test_house_assignment.py with:
   - A small set of embeddings (3–6 mock participants).
   - Test that assign_houses returns a house index for each participant.
   - Ensure it doesn’t crash when n_clusters=3 and data is small.

3. Return the code for src/house_assignment.py and tests/test_house_assignment.py.
```

### 5.7 **Prompt 7: Summaries (Optional Feature)**

```
text
Optional summarization feature:

1. Create src/summaries.py with:
   - summarize_responses(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame
     * This function can be a mock or call an LLM to produce short summaries of participant responses.

2. In tests/test_summaries.py:
   - Mock or stub the LLM call so it always returns "fake summary".
   - Verify the function adds a "summary" column or modifies columns accordingly.

3. If you want to re-embed the summaries, illustrate how to integrate with your existing embedding pipeline in an example usage snippet.

4. Return src/summaries.py and tests/test_summaries.py.
```

### 5.8 **Prompt 8: Deployment & Frontend Integration**

```
text
Finally, we deploy a simple frontend with Vercel:

1. Create a frontend directory with:
   - index.html, script.js (or a React app if desired).
   - A minimal interface to display participants and their top matches or house assignments.

2. Show how to build and run the frontend locally, then how to use "vercel deploy".

3. Provide a final integration test in tests/test_end_to_end.py that:
   - Loads a sample CSV.
   - Runs the end-to-end pipeline (ingestion, preprocessing, embedding, matching, house assignment).
   - Outputs a JSON or CSV with the final assignments.

4. Return the final code structure, including the minimal frontend.

Please include instructions for running the end-to-end test and mention any best practices or final notes.
```

---

### **How to Use These Prompts**

1. **Feed Prompt 1** to your code-generation LLM. Take the generated code, put it in your repository.  
2. Run tests.  
3. **Feed Prompt 2**, incorporate changes, and so on.  
4. Continue this process until Prompt 8 is completed.  

By following this iterative, test-driven approach, you ensure each piece is well-tested and integrates seamlessly with the previous steps. This reduces refactoring later and helps maintain a clean, maintainable codebase.