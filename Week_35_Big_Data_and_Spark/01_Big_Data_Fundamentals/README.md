# 01 – Big Data Fundamentals

This module builds the conceptual foundation for Week 35 by explaining what **Big** data actually means, why traditional systems fail, and how distributed systems like Hadoop and Spark emerged to solve those problems.

## Learning objectives

By the end of this folder, you should be able to:

- Define Big Data in terms of data volume, velocity, and variety.
- Explain the extended 5Vs (Volume, Velocity, Variety, Veracity, Value).
- Map real-world industry use cases to Big Data characteristics.
- Describe key challenges in storing and processing Big Data.
- Understand at a high level why distributed computing and clusters are needed.

## File structure

- `01_introduction_to_big_data.md` – What is Big Data and why it matters.
- `02_characteristics_5Vs.md` – Deep dive into the 5Vs with examples.
- `03_use_cases_and_applications.md` – Domain-wise scenarios.
- `04_challenges_in_big_data.md` – Storage, processing, and quality issues.
- `05_distributed_computing_basics.md` – Why we need clusters and how they help.
- `practicals/` – Small, focused exercises to build intuition.

## How this connects to the rest of Week 35

- The concepts here motivate **Hadoop (02 folder)** as an early Big Data solution using HDFS, MapReduce, and YARN for storage and processing [web:8][web:12].
- The limitations of MapReduce and batch-only processing naturally lead to **Apache Spark (03+ folders)** for fast, in-memory analytics and richer APIs [web:6][web:9].
