# Practical 01 – Data Volume Exploration

Goal: Build intuition for what “big” means on your local machine versus a distributed system [web:10].

## 1. Setup

- Use Python (Jupyter or PySpark shell).
- Have a simple CSV (e.g., 1–10 million rows) or generate synthetic data.

Example (Python, local):

- Generate a DataFrame with N rows.
- Measure:
  - File size on disk.
  - Time to read.
  - Peak memory usage (approximate via OS tools).

## 2. Tasks

1. Start with a small dataset (e.g., 100k rows).
2. Gradually increase to 1M, 5M, 10M rows.
3. For each size, record:
   - File size (MB/GB).
   - Read time.
   - Simple aggregation time (e.g., group by a column).

## 3. Observations

Fill this table after running experiments:

| Rows       | File Size | Read Time | Aggregation Time | Notes                  |
|-----------:|-----------|-----------|------------------|------------------------|
| 100,000    |           |           |                  |                        |
| 1,000,000  |           |           |                  |                        |
| 5,000,000  |           |           |                  |                        |
| 10,000,000 |           |           |                  |                        |

Questions:

- At what point does your machine start to feel slow?
- At what point do you hit RAM or time limits?

## 4. Link to theory

- Connect your observations to the **Volume** and **“When does it become Big Data?”** sections in `01_introduction_to_big_data.md` and `02_characteristics_5Vs.md` [web:10][web:11].
- Write a short paragraph summarizing when you would consider using distributed tools (Hadoop/Spark) based on these experiments.
