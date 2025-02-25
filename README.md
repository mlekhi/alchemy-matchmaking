# Matchmaking Project Proposal

## **Overview**
This project is a tool for intelligently matching participants based on their responses to key questions. Using embeddings and clustering techniques, the system enables structured matchmaking while ensuring diverse and meaningful pairings. The solution includes a graph-based visualization of connections and a searchable match interface.

## **Goals**
- Automate participant matching using AI-powered embeddings.
- Enable structured event-based matchmaking through CSV input.
- Support real-time search and visualization of participant relationships.
- Provide a lightweight, deployable solution for event organizers.

## **Matching Algorithm**

### **1. Preprocessing Responses**
- Convert text responses for "learning," "past work," "talk about forever," and "hype song" into **vector embeddings** using **SBERT**.
- Use **TF-IDF** as a fallback if embeddings are too sparse.
- Store these embeddings in a **vector database** (e.g., **FAISS** for fast similarity lookups).

### **2. Compute Cross-Matching Scores**
#### **Cross-Match #1: "What do you want to learn?" ⬄ "What can you talk about forever?"**
✅ **Goal:** Pair users who are passionate about a topic with those who want to learn it.
#### **Algorithm:**
1. **Retrieve embeddings for all users** in both categories.
2. **Compute cosine similarity** between "learning" and "talk forever" embeddings.
3. **Sort users by highest similarity** and create **one-to-one or group matches**.
4. **Cap how many users in a house have the same knowledge-sharing topic** to maintain diversity.

#### **Cross-Match #2: "What do you want to learn?" ⬄ "What’s the last thing you worked on?"**
✅ **Goal:** Create **mentorship pairings** between learners and experienced users **while ensuring diversity in past experiences**.
#### **Algorithm:**
1. **Retrieve embeddings for all users** in both categories.
2. **Compute cosine similarity** between "learning" and "past work" responses.
3. **Apply a mentorship weight**: If similarity is **high**, increase match score.
4. **Use dissimilarity for house placements:**
   - **Enforce diversity in work history** → **Avoid matching users with highly similar past projects**.
   - **Apply penalties** if too many users have the same work experience in a house.

#### **Cross-Match #3: "What’s your hype song?"**
✅ **Goal:** Balance **music-based cultural fit** with some diversity.
#### **Algorithm:**
1. **Convert songs to embeddings** using **pre-trained music models (e.g., Spotify API, OpenAI embeddings)**.
2. **Compute similarity in genres, artists, and song embeddings**.
3. **Use a hybrid similarity score:**
   - **High music similarity** → Strengthen **1:1 matches**.
   - **Low music similarity** → Encourage **house diversity** while still allowing compatibility.

### **3. Final Matching & House Assignments**
✅ **Goal:** Ensure balance in **learning, experience, music preferences, and discussion variety**.
#### **Algorithm:**
1. **Calculate all match scores** based on learning/work/talk/music topics.
2. **Sort by priority:**
   - **Mentorship pairs (learning ⬄ work experience with dissimilar past work)**.
   - **Knowledge-sharing pairs (learning ⬄ talk forever)**.
   - **Music-based compatibility (soft influence on matching)**.
3. **Run clustering algorithm** (**K-Means or Spectral Clustering**) to assign houses.
4. **Apply diversity penalties:**
   - Prevent houses from having **too many people with identical past experiences**.
   - **Encourage learning alignment** within houses.
5. **Finalize house groups & pairings** for chat and networking.

---

## **Project Setup**

### **1. Prepare the Data**
1. Download participant data from `lu.ma` or your preferred source.
2. Ensure the CSV is formatted as follows:

   | Names | Responses |
   |--------|--------------------------------|
   | Freeman Jiang | I wish to explore the world |
   | Rajan Agarwal | I want to build AGI |
   | Hudhayfa Nazoordeen | I want to grow more vegetables hydroponically |

3. Save the file as `data.csv` in the root directory.
4. Set `COLUMN_INDEX` in `generate_embeddings.py` to the correct response column index (e.g., `1` in this case).

### **2. Install Dependencies**
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Generate Embeddings and Match Data**
```sh
python generate_embeddings.py  # Convert responses into vector embeddings
python build_graph.py  # Construct graph based on similarity thresholds
python attendees.py  # Generate attendee cache for search
```
You should now have a `graphData.json` file containing participant connections.

### **4. (Optional) Summarize Responses**
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

---

## **Developing the Graph Interface**
1. Navigate to the `graph/` directory:
```sh
cd graph
npm i
npm run dev
```
2. Run Tailwind in a separate terminal:
```sh
npm run tailwind
```
3. Open `graph/index.html` in a browser to preview.
4. To serve:
```sh
npm start
```

---

## **Developing the Matchmaking Interface**
1. Navigate to the `match/` directory:
```sh
cd match
npm i
npm run dev
```
2. Open `localhost:3000` in a browser to view results.
3. To serve:
```sh
npm start
```

---

## **Deployment Guide**
- Use **Vercel CLI** to deploy `match` and `graph` separately.
- Keep sensitive CSV data private.
- Follow [Vercel CLI Docs](https://vercel.com/docs/cli) for step-by-step deployment instructions.

---

## **To-Do List**
### **Backend & Processing**
- [ ] Ensure CSV data formatting compliance.
- [ ] Implement embeddings for participant responses.
- [ ] Build the similarity graph.
- [ ] Add optional AI-powered summarization.

### **Frontend UI**
- [ ] Develop graph-based participant visualization.
- [ ] Implement matchmaking search functionality.
- [ ] Display house assignments for grouped matchmaking.
- [ ] Enable interactive filters for exploring connections.

### **Optimization & Deployment**
- [ ] Optimize similarity thresholds for ideal matching.
- [ ] Improve UI responsiveness.
- [ ] Deploy to Vercel.
