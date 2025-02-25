# TODO Checklist

A comprehensive checklist for building the matchmaking system, from setup to deployment. Check off each item as you complete it.

---

## 1. **Setup & Environment**

- [ ] **Repository Initialization**
  - [ ] Create a new Git repository.
  - [ ] Set up Python virtual environment.
  - [ ] Install dependencies (chromadb, sentence-transformers, pytest, sklearn, pandas, etc.).
  - [ ] Initialize a basic file structure:  
    - `src/`  
    - `tests/`  
    - `scripts/`  
- [ ] **Basic Testing Setup**
  - [ ] Create a dummy test in `tests/test_basic.py` (verifies `1 + 1 == 2`).
  - [ ] Confirm that tests run successfully via `pytest`.

---

## 2. **Data Ingestion & Validation**

- [ ] **Create `data_ingestion.py`**
  - [ ] Function `load_csv(filepath: str) -> pd.DataFrame`.
  - [ ] Function `validate_columns(df: pd.DataFrame, required_columns: List[str]) -> None`.
- [ ] **Testing (`test_data_ingestion.py`)**
  - [ ] Test loading a small, mock CSV.
  - [ ] Test validation with missing columns (should raise error).
  - [ ] Test validation with all columns present (should pass).

---

## 3. **Preprocessing & Cleanup**

- [ ] **Create `preprocessing.py`**
  - [ ] `clean_text(text: str) -> str`.
  - [ ] `clean_dataframe(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame`.
    - [ ] Applies `clean_text` to each relevant column.
    - [ ] Replaces NaN with `"NULL"`.
    - [ ] Returns cleaned DataFrame.
- [ ] **Testing (`test_preprocessing.py`)**
  - [ ] Verify `clean_text` normalization (punctuation, case, etc.).
  - [ ] Verify `clean_dataframe` handles NaN and applies cleaning as expected.

---

## 4. **Embedding Generation**

- [ ] **Create `embedding.py`**
  - [ ] Function `load_embedding_model()`  
    - Loads the Sentence-BERT model, e.g. `'all-MiniLM-L6-v2'`.
  - [ ] Function `generate_embeddings(df: pd.DataFrame, columns_to_embed: List[str]) -> List[List[float]]`.
    - [ ] Concatenate relevant columns for each row.
    - [ ] Generate embeddings with the model.
  - [ ] Function `store_embeddings_in_chromadb(embeddings: List[List[float]], metadata: List[Dict[str, str]])`.
    - [ ] Create or connect to a ChromaDB collection named `"matchmaking"`.
    - [ ] Insert each embedding with corresponding metadata (name, etc.).
- [ ] **Testing (`test_embedding.py`)**
  - [ ] Use a small DataFrame with mock data.
  - [ ] Verify `generate_embeddings` returns correct number of embeddings.
  - [ ] Test `store_embeddings_in_chromadb` by inserting and verifying retrieval (mock or local instance).

---

## 5. **Matching & Scoring**

- [ ] **Create `matching.py`**
  - [ ] `compute_similarity(vec1: List[float], vec2: List[float]) -> float` (cosine similarity).
  - [ ] `compute_dissimilarity(vec1: List[float], vec2: List[float]) -> float` (1 - similarity).
  - [ ] `match_participants(embeddings: Dict[str, List[float]]) -> Dict[str, List[Tuple[str, float]]]`.
    - [ ] For each participant, find top-N most similar and most dissimilar participants.
    - [ ] Return a structure mapping participant → list of `(other_participant, score)`.
- [ ] **Testing (`test_matching.py`)**
  - [ ] Mock a small dictionary of known embeddings.
  - [ ] Verify `compute_similarity` and `compute_dissimilarity` are correct with known vectors.
  - [ ] Check `match_participants` returns logical matches in ascending/descending order.

---

## 6. **House Assignment**

- [ ] **Create `house_assignment.py`**
  - [ ] `assign_houses(embeddings: Dict[str, List[float]], n_clusters=3) -> Dict[str, int]`.
    - [ ] Use K-Means (or chosen clustering) from `sklearn`.
    - [ ] Map each participant to a cluster label (0, 1, or 2).
- [ ] **Testing (`test_house_assignment.py`)**
  - [ ] Mock embeddings for 3–6 participants.
  - [ ] Ensure each participant is assigned a house index.
  - [ ] Verify no house is empty (if possible).
  - [ ] Check basic diversity or distribution if relevant.

---

## 7. **Summaries (Optional Feature)**

- [ ] **Create `summaries.py`**
  - [ ] `summarize_responses(df: pd.DataFrame, text_columns: List[str]) -> pd.DataFrame`
    - [ ] Calls GPT or another LLM to create short summaries per participant.
    - [ ] Stores results in a new column (e.g. `summary`).
- [ ] **Integration with Embeddings**
  - [ ] Optionally re-embed summaries or store them separately.
- [ ] **Testing (`test_summaries.py`)**
  - [ ] Mock or stub the LLM calls (return a fixed string).
  - [ ] Check that new or modified columns exist and hold summarized content.

---

## 8. **Deployment & Frontend**

- [ ] **Minimal Frontend**
  - [ ] Create a `frontend/` directory with `index.html`, `script.js`, or a small React setup.
  - [ ] Display participants and their top matches or house assignments.
  - [ ] Provide basic UI to filter or sort matches.
- [ ] **Vercel Deployment**
  - [ ] Configure `vercel.json` if needed.
  - [ ] Run `vercel deploy` and confirm the site is live.

---

## 9. **Testing & Validation**

- [ ] **End-to-End Test (`test_end_to_end.py`)**
  - [ ] Use a sample CSV with a handful of entries.
  - [ ] Run data ingestion, validation, preprocessing, embedding generation, matching, and house assignment in sequence.
  - [ ] Verify the output (JSON or CSV) has the expected participants and assigned houses.
- [ ] **Match Accuracy / Quality Checks**
  - [ ] If possible, manually inspect the top matches for a few sample participants to ensure correctness.
  - [ ] Confirm dissimilar matches behave as expected (especially for “past work” vs. “learning” logic).

---

## 10. **Final Clean-Up & Documentation**

- [ ] **Code Review & Refactoring**
  - [ ] Ensure naming conventions are consistent.
  - [ ] Remove dead code or unused imports.
- [ ] **Documentation**
  - [ ] Update `README.md` with usage instructions:
    - [ ] How to install dependencies.
    - [ ] How to run each step (preprocessing, embeddings, etc.).
    - [ ] How to run tests.
  - [ ] Add docstrings to all core functions.
- [ ] **Optional Enhancements**
  - [ ] Parameterize similarity thresholds or cross-matching weight factors.
  - [ ] Add more descriptive metrics for cluster diversity or match quality.
