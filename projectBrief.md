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
- Convert text responses for **each individual question** ("learning," "past work," "talk about forever," and "hype song") into **vector embeddings** using **SBERT**.
- Use **TF-IDF** as a fallback if embeddings are too sparse.
- Store these embeddings in a **vector database** (e.g., **FAISS**) for fast similarity lookups.

### **2. Individual Question Matching (Standalone Matching)**
Each response is evaluated independently to determine **direct similarity or dissimilarity matching** within its category.

#### **Matching by Individual Question:**
✅ **Goal:** Allow similarity-based or dissimilarity-based grouping based on each response while ensuring diversity where needed.
#### **Technical Mechanism:**
- **“What do you want to learn?”** → Match users with **high similarity** by computing cosine similarity on embeddings.
- **“What’s the last thing you worked on?”** → Match users with **high dissimilarity** by computing cosine similarity on embeddings and inverting the score (`1 - similarity`).
- **“What’s something you could talk about forever?”** → Match users with **high similarity** for knowledge-sharing.
- **“What’s your hype song?”** → Match users with **high similarity** on music embeddings, but allow variation in house placements for cultural diversity.

### **3. Cross-Matching Responses (Multi-Question Matching)**
In addition to individual matching, two specific questions are cross-matched to enhance mentorship and knowledge-sharing dynamics.

#### **Cross-Match #1: "What do you want to learn?" ⬄ "What can you talk about forever?"**
✅ **Goal:** Pair users who are passionate about a topic with those who want to learn it.
#### **Technical Mechanism:**
1. **Retrieve embeddings for all users** in both categories.
2. **Compute cosine similarity** between "learning" and "talk forever" embeddings.
3. **Sort users by highest similarity** and create **one-to-one or group matches**.
4. **Cap how many users in a house have the same knowledge-sharing topic** to maintain diversity.

#### **Cross-Match #2: "What do you want to learn?" ⬄ "What’s the last thing you worked on?"**
✅ **Goal:** Create **mentorship pairings** between learners and experienced users **while ensuring diversity in past experiences**.
#### **Technical Mechanism:**
1. **Retrieve embeddings for all users** in both categories.
2. **Compute cosine similarity** between "learning" and "past work" responses.
3. **Apply a mentorship weight**: If similarity is **high**, increase match score.
4. **Use dissimilarity for house placements:**
   - **Enforce diversity in work history** → **Avoid matching users with highly similar past projects**.
   - **Apply penalties** if too many users have the same work experience in a house.

### **4. Final Matching & House Assignments**
✅ **Goal:** Ensure balance in **learning, experience, music preferences, and discussion variety**.
#### **Technical Mechanism:**
1. **Calculate all match scores** based on individual question similarity and cross-match scores.
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