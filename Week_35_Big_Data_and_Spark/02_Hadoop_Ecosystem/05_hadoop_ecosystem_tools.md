# Hadoop Ecosystem Tools Overview

Beyond HDFS, MapReduce, and YARN, the Hadoop ecosystem includes many tools for ingesting, querying, and managing data [web:26][web:32]. This file provides a high-level map of key components relevant for Week 35.

## 1. Hive – SQL on Hadoop

- Data warehouse infrastructure built on top of Hadoop.
- Uses **HiveQL (HQL)**, a SQL-like language, to define tables and run queries.
- Translates queries into execution plans (often MapReduce or other engines) [web:32].
- Good for:
  - Batch analytics.
  - ETL on large datasets.
  - Users comfortable with SQL.

## 2. Pig – Data flow scripting

- Provides **Pig Latin**, a high-level data flow language.
- Scripts describe a series of operations like load, filter, group, join, and store.
- Pig translates scripts into MapReduce jobs or other execution plans [web:26][web:32].
- Good for:
  - Complex ETL flows.
  - Programmers who prefer data flow over declarative SQL.

## 3. Sqoop – RDBMS ↔ Hadoop data transfer

- Tool for bulk data transfer between relational databases and Hadoop (HDFS, HBase, Hive) [web:28][web:32].
- Uses parallel Map tasks to import/export data efficiently.
- Common use cases:
  - Periodic imports of transactional data into HDFS/Hive.
  - Exporting processed results back to relational systems.

## 4. Flume – Log and event ingestion

- Distributed service for collecting, aggregating, and moving large volumes of log and event data into HDFS or other stores [web:23][web:32].
- Uses agents with **source–channel–sink** architecture.
- Good for:
  - Streaming log ingestion from many servers or applications.

## 5. HBase – NoSQL on Hadoop (brief)

- Distributed, column-oriented NoSQL database on top of HDFS.
- Provides low-latency random reads/writes over large tables.
- Often used when both Big Data scale and random access patterns are needed [web:32].

## 6. How to use this map in Week 35

For this week:

- You only need **conceptual understanding** of these tools:
  - Hive and Pig as higher-level abstractions above MapReduce.
  - Sqoop and Flume as ingestion/egress tools [web:26][web:32].
- Later, you can map similar ideas to Spark (Spark SQL vs Hive, Spark Streaming vs Flume-like pipelines, etc.).

The next two files focus specifically on Hive and Pig, as they are the most commonly referenced in Big Data syllabi.
