# 🏆 Rising Stars GNN Mini-Competition: Inductive Node Classification

Welcome to the **Rising Stars GNN Mini-Competition** 🚀

This repository hosts a hands-on challenge on **inductive node classification** using **Graph Neural Networks (GNNs)**. Your task is to train a model on a given graph and **generalize to completely unseen nodes**.

This competition is designed to be **safe and reproducible**. You will not submit code; instead, you will submit **predictions only**, which are automatically evaluated and ranked on a public leaderboard using GitHub Actions.

---

## 🎯 Challenge Overview

You are given a citation network with node features and labels for training nodes only.  
Your goal is to **predict the research topic of unseen nodes** using an **inductive GNN model**.

### 🔍 What Makes This Inductive?

* Test nodes are **not present during training**
* Their IDs and labels are **never seen**
* The model must rely **only on learned parameters**, not memorized node embeddings

> **Train once, generalize to new nodes.**

---

## 📂 Dataset Description

We use the **Cora citation network**, a standard benchmark in graph learning.

### Graph Components

* **Nodes:** Scientific papers
* **Edges:** Citation relationships
* **Node features:** Bag-of-words vectors
* **Labels:** Research topics

### 📁 Repository File Structure

```text
.
├── data/
│   └── public/
│       ├── edge_list.csv          # Edges between training nodes
│       ├── train.csv              # Training nodes (IDs, features, labels)
│       ├── test_edges.csv         # Edges involving test nodes (inference only)
│       ├── test_nodes.csv         # Unseen test nodes (IDs, features only)
│       └── sample_submission.csv  # Example format for your predictions
├── submissions/
│   └── inbox/                     # Where you will open PRs to submit
├── leaderboard/                   # Live ranking data
└── docs/                          # Source code for the interactive leaderboard website

---

## 3. Submission Format

Participants submit a **single CSV file**:

**predictions.csv**
```
id,y_pred
n0001,0.92
n0002,0.13
...
```

Rules:
- `id` must match exactly the IDs in `test_nodes.csv`
- One row per test node
- `y_pred` must be a float in [0,1]
- No missing or duplicate IDs

A sample is provided in:
```
data/public/sample_submission.csv
```

---

## 4. How to Submit

1. Fork this repository
2. Create a new folder:
```
submissions/inbox/<team_name>/<run_id>/
```
3. Add:
   - `predictions.csv`
   - `metadata.json`

Example `metadata.json`:
```json
{
  "team": "example_team",
  "model": "llm-only",
  "llm_name": "gpt-x",
  "notes": "Temporal GNN with class weighting"
}
```

4. Open a Pull Request to `main`

The PR will be **automatically scored** and the result posted as a comment.

---

## 5. Leaderboard

After a PR is merged, the submission is added to:
- `leaderboard/leaderboard.csv`
- `leaderboard/leaderboard.md`

Rankings are sorted by **descending score**.

---

## 6. Rules

- No external or private data
- No manual labeling of test data
- No modification of evaluation scripts
- Unlimited offline training is allowed
- Only predictions are submitted

Violations may result in disqualification.

---

## 7. Human vs LLM Studies

To use this competition for research:
- Fix a time budget (e.g., 2 hours)
- Fix a submission budget (e.g., 5 runs)
- Record metadata fields (`model`, `llm_name`)
- Compare:
  - validity rate
  - best score within K submissions
  - score vs submission index

---

## 8. Citation

If you use this template in academic work, please cite the repository.

---

## 9. License

MIT License.

## Interactive Leaderboard (GitHub Pages)

This template includes an interactive leaderboard page inspired by modern benchmark sites.

**Enable GitHub Pages** (Settings → Pages) and set the source to the `main` branch `/docs` folder.
Then open `https://<your-org>.github.io/<repo>/leaderboard.html`.
