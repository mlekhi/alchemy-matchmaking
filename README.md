# Matchmaking @ Alchemy!

## **Project Setup**

### **1. Prepare the Data**
1. Download participant data from `lu.ma` or your preferred source.
2. Ensure the CSV is formatted as follows:

   | Names | Responses |
   |--------|--------------------------------|
   | Maya Lekhi | I wish to explore the world |
   | Robin Hylands | I want to build AGI |

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

## **Deployment Guide**
- Use **Vercel CLI** to deploy `match` and `graph` separately.
- Keep sensitive CSV data private.