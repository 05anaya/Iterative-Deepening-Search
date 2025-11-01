# Iterative Deepening Search (IDS)

This project implements the **Iterative Deepening Search (IDS)** algorithm in Python.  
IDS combines the **space efficiency of Depth-First Search (DFS)** with the **completeness of Breadth-First Search (BFS)** by progressively deepening the search limit until the goal node is found.

---

## 🔍 How It Works

The algorithm repeatedly performs **Depth-Limited Search (DLS)** with increasing depth limits.  
At each depth, it explores the search tree up to that limit before increasing the depth by one.

**Pseudocode Overview:**
1. Start with depth = 0  
2. Run depth-limited search from the start node  
3. If the goal is found → return the path  
4. Else, increase depth and repeat until the maximum depth is reached  
