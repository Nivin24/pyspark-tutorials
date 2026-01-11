# Introduction to Apache Hive

## 1. What is Hive?

Hive is a data warehousing and SQL-like query system built on top of Hadoop, designed to make it easier to analyze large datasets stored in HDFS using familiar SQL concepts [web:32]. It is well suited for batch analytics and ETL over Big Data.

Key ideas:

- Define tables and schemas on top of files in HDFS.
- Use **HiveQL (HQL)**, a SQL-like language, to query and transform data.
- Under the hood, Hive executes queries using engines like MapReduce, Tez, or Spark [web:32].

## 2. Hive architecture (high level)

Core components:

- **Metastore**:
  - Stores metadata about databases, tables, partitions, schemas, and locations.

- **Driver and Compiler**:
  - Parse and optimize HiveQL queries.
  - Generate execution plans (e.g., MapReduce jobs).

- **Execution engine**:
  - Submits and manages the actual jobs on the cluster (MapReduce/Tez/Spark).

- **CLI / Beeline / JDBC**:
  - Interfaces through which users submit queries.

## 3. Tables, partitions, and data layout

Hive organizes data into:

- **Databases**: Logical grouping of tables.
- **Tables**: Structured views over files.
- **Partitions**: Directory-based partitioning by key (e.g., date, country) for efficient query pruning [web:32].

Common patterns:

- External vs managed tables.
- Using partitions and buckets for performance at large scale.

## 4. Typical use cases

- Batch ETL jobs over logs and transactional data.
- Aggregated reporting and dashboards (when latency can be in minutes).
- Precomputing features for downstream systems.

In Week 35, you will focus on understanding where Hive fits and writing a few simple conceptual queries in the practicals, without going into full SQL or optimization details [web:32].
