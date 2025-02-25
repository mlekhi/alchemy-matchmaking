# Matchmaking System: Developer Specification

## **1. Overview**
This matchmaking system processes participant responses from a CSV, computes embeddings, and matches individuals based on similarity and dissimilarity across key questions. The system runs entirely **without a backend**, using local scripts and **ChromaDB** for efficient vector search. It supports **individual question-based matching**, **cross-matching** for mentorship and knowledge-sharing, and **final house sorting into three houses.**

## **2. Functional Requirements**
- **Data Ingestion**: Load CSV containing participant responses.
- **Preprocessing**: Extract and clean relevant response columns.
- **Embedding Generation**: Convert text responses into vector embeddings.
- **Storage**: Persist embeddings using **ChromaDB**.
- **Matching Logic**:
  - **Individual Question Matching** (e.g., similarity for learning, dissimilarity for past work).
  - **Cross-Matching** (e.g., learning ↔ talk about forever, learning ↔ past work).
- **House Assignments**: Group participants into **three distinct houses** ensuring diverse skillsets and interests.
- **Deployment**: Frontend deployment using **Vercel CLI**.

## **3. System Workflow**

### **3.1 Generate Embeddings and Match Data**
```sh
python preprocess_alchemy_csv.py  # Cleaning the specific Alchemy Luma responses. Skip this step or customize it for your individual event!
python generate_embeddings.py  # Convert responses into vector embeddings
python build_graph.py  # Construct graph based on similarity thresholds
python attendees.py  # Generate attendee cache for search
```
After running these scripts, you will have a `graphData.json` file containing participant connections.

### **3.2 (Optional) Summarize Responses**
```sh
python summarize_graph_data.py  # Generate AI-based summaries
```
If using summarized data, update `graph/index.js`:
```js
// Uncomment this line to use summarized data
// const json = require("../summarizedGraphData.json");
```
Then, re-run:
```sh
python attendees.py  # Rebuild attendee cache with summaries
```

## **4. Data Handling**
### **4.1 Input Data Format**
| Name | Learning Interest | Past Work | Talk Forever | Hype Song |
|------|------------------|-----------|-------------|-----------|
| Ahmed Sinjab | Learning how to make a project using a database | The last thing that I worked on that I am proud of is... | *NULL* | My own way |
| Atnasia Ibsa | How to play the piano | A creativity manifesto... | *NULL* | *NULL* |
| Ali | Flying | A charades iPhone game... | *NULL* | Kylo Ren theme |

### **4.2 Preprocessing Steps**
1. **Extract only necessary columns** (name, responses).
2. **Rename columns** for easier processing.
3. **Handle missing values** (replace `NaN` with `"NULL"`).
4. **Save cleaned CSV (`cleaned_data.csv`)**.

### **4.3 Storage in ChromaDB**
- **Collection:** `matchmaking`
- **Metadata:** `{"name": <name>, "response": <text>}`
- **Embeddings:** Stored as 768-d vector (SBERT)

### **4.4 Retrieval Strategy**
- **Similarity Search**: Use cosine similarity for “learning” and “talk about forever.”
- **Dissimilarity Search**: Invert similarity for “past work.”

## **5. Matching Logic**
### **5.1 Individual Question Matching**
- **What do you want to learn?** → Find high-similarity matches.
- **What’s the last thing you worked on?** → Find high-dissimilarity matches.
- **What can you talk about forever?** → Find high-similarity matches.
- **What’s your hype song?** → Find high-similarity matches (soft weighting).

### **5.2 Cross-Matching**
- **Learning ↔ Talk about forever** → High similarity = mentorship pair.
- **Learning ↔ Past Work** → High similarity = mentorship, **low similarity = house diversity.**

### **5.3 House Assignment (Final Step)**
- Use **K-Means or Spectral Clustering** to **sort all participants into three houses.**
- **Ensure diversity** in past work experiences within each house.
- **Align some learning interests** to foster collaboration.

## **6. Deployment Guide**
- Use **Vercel CLI** to deploy `match` and `graph` separately.
- Keep sensitive CSV data private.

## **7. Error Handling Strategy**
- **CSV Validation**: Ensure correct format before processing.
- **ChromaDB Failure Handling**: Retry with exponential backoff.
- **Embedding Generation Errors**: Log and skip faulty records.
- **Matching Failures**: Fallback to default random assignments.

## **8. Testing Plan**
### **8.1 Unit Tests**
- Validate **embedding output consistency**.
- Ensure **ChromaDB stores and retrieves data correctly**.

### **8.2 Integration Tests**
- Check **end-to-end processing from CSV → Match output**.
- Validate **frontend integration with JSON outputs**.

### **8.3 Match Accuracy Testing**
- Test with **predefined datasets** to measure match quality.
- Ensure **dissimilarity in past work-based grouping**.
- Validate **house diversity rules**.