# Practical 03 – Big Data Scenario Checklist

Goal: Build a reusable checklist to quickly decide whether a problem is a **Big Data** problem and what characteristics matter most [web:10][web:7].

## 1. Checklist questions

Use this checklist whenever you see a new data problem:

1. **Volume**
   - Approximate total data size (raw + processed)?
   - Expected growth per day/week/month?
   - Can a single machine store all required data comfortably?

2. **Velocity**
   - How frequently does new data arrive?
   - Do we need batch, near real-time, or real-time responses? [web:11]
   - What is the maximum acceptable processing delay?

3. **Variety**
   - What formats exist (tables, JSON, logs, images, text)? [web:7][web:15]
   - Do schemas change over time?
   - How many independent data sources are involved?

4. **Veracity**
   - How noisy, incomplete, or inconsistent is the data?
   - Are there duplicates or conflicting records? [web:15]
   - How critical is correctness for downstream decisions?

5. **Value**
   - What business or analytical decisions will this data influence? [web:11]
   - Are we collecting data that we do not plan to use?
   - How will success be measured?

## 2. Decision guide

After answering the checklist, classify the problem:

- **Not Big Data**:
  - Fits on one machine.
  - Simple batch jobs complete within SLAs.
  - Limited variety, low velocity.

- **Borderline Big Data**:
  - Hitting limits on storage/performance occasionally.
  - Considering sharding or partial distribution.

- **Clear Big Data**:
  - Very high Volume/Velocity/Variety.
  - Strong Veracity and Value requirements.
  - Single-node solutions are not feasible.

## 3. Example usage

Work through at least two examples:

- One internal to your own projects (e.g., movie recommendation datasets).
- One from an external domain (e.g., IoT, finance, healthcare).

For each example:

- Fill out the checklist.
- Write 3–5 sentences justifying whether it is a Big Data problem.
- Note whether Hadoop/Spark would be justified or overkill based on your reasoning [web:6][web:8].

Keep this file as a template you can copy into other project repos when scoping new data problems.
