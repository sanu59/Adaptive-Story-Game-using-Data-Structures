# Adaptive Story Game using Data Structures

This repository contains an interactive story game implemented in Python, where the narrative is modeled as a graph of story states. Each choice the player makes moves them to a different node in the story, and a scoring system evaluates how good their overall path was compared to the best possible path.

The project was developed as part of a **Data Structures and Algorithms (DSA)** course to show how core DS concepts (graphs, stacks, recursion/DFS) can power an adaptive story engine.

---

## 📚 Overview

- You play through a branching story by clicking on choices in a **Tkinter GUI**.
- The story is represented as a **graph**:
  - Nodes = story states.
  - Edges = choices that lead to the next state.
- Each node can contribute to a **score**.
- At the end, the game can:
  - Show your final score.
  - Conceptually compare your path to a maximum-score path through the story graph.

There are two main implementations in this project:

1. **`Code.py`** – A simpler version with the story graph hard-coded directly in Python.  
2. **`gui.py`** – A more advanced version that loads story data from a JSON file, includes scoring and path analysis, and supports background images.

---

## 🧠 Core Data Structure Ideas

- **Graph (Dictionary of Dictionaries)**  
  The story is stored as a dictionary where each key is a node ID (like `"start"`, `"choice1"`, etc.).  
  Each node contains:
  - `text` → the narrative paragraph.
  - `choices` → mapping from button text to the next node ID.
  - `score` → points gained when entering that node.

- **Stack (Choice History)**  
  A Python list is used as a stack to keep track of the sequence of visited nodes, allowing the game to maintain a history of choices.

- **Depth-First Search (DFS)**  
  DFS (via recursion) is used to:
  - Explore all possible paths from the starting node to endings.
  - Compute which path yields the **maximum total score**.

- **Accumulated Scoring**  
  A running score variable is updated whenever the player moves to a new node.  
  At the end of the game, the player’s score is compared with the score of an optimal path.

---

## 🛠 Tech Stack

- **Language:** Python 3  
- **GUI Library:** Tkinter  
- **Data Format:** JSON (for external story data in the advanced version)  
- **Concepts:** Graphs, Stacks, Recursion / DFS, GUI programming

---

## 📁 Project Structure

```text
Adaptive-Story-Game-using-Data-Structures/
├── Code.py            # Basic prototype: hard-coded story graph
├── gui.py             # Advanced GUI: JSON-based story + scoring + DFS
├── scratch_11.json    # Story data (draft/example JSON file)
└── README.md          # Project documentation
