# Introduction to Apache Pig

## 1. What is Pig?

Apache Pig is a platform for analyzing large datasets using a high-level scripting language called **Pig Latin** [web:26][web:32]. Instead of writing Java MapReduce jobs directly, developers express data flows using Pig Latin, which Pig then compiles into execution plans (commonly MapReduce jobs).

Key features:

- Data flow style (sequence of transformations).
- Handles structured, semi-structured, and unstructured data.
- Automatically optimizes execution plans [web:26][web:32].

## 2. Pig Latin basics (conceptual)

Typical operations in a Pig script:

- `LOAD` – Load data from HDFS or other sources.
- `FILTER` – Filter rows based on conditions.
- `FOREACH ... GENERATE` – Project and transform fields.
- `GROUP` – Group data by keys.
- `JOIN` – Join multiple relations.
- `ORDER` – Sort data.
- `STORE` – Write results back to HDFS.

These operations are chained to create a logical flow, which Pig converts into parallel jobs on the cluster.

## 3. When to use Pig vs Hive

Conceptual comparison:

- **Hive**:
  - SQL-like, declarative.
  - Good for analytics/reporting where you think in queries [web:32].

- **Pig**:
  - Data flow scripting, more procedural.
  - Good for complex ETL pipelines where multi-step flows are natural [web:26][web:32].

Today, many of these roles are also covered by Spark (Spark SQL, DataFrame API), but understanding Pig helps appreciate how higher-level abstractions evolved on top of MapReduce.

## 4. Use in Week 35

For this week:

- Focus on:
  - Knowing what Pig is and where it fits in the Hadoop ecosystem.
  - Being able to read simple conceptual Pig flows (LOAD → FILTER → GROUP → STORE).
- You will not go deep into syntax; instead you will connect Pig’s role to later Spark DataFrame pipelines and SQL transformations [web:26][web:6].
