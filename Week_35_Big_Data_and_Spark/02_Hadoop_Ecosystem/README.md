# 02 – Hadoop Ecosystem

This module introduces the Apache Hadoop ecosystem as one of the first widely adopted platforms for storing and processing Big Data using clusters of commodity machines [web:8][web:12].

## Learning objectives

By the end of this folder, you should be able to:

- Explain the core components of Hadoop: HDFS, MapReduce, and YARN [web:8][web:12].
- Describe how HDFS stores large datasets reliably across multiple nodes [web:21][web:24].
- Understand the MapReduce programming model and its role in batch processing [web:20][web:31].
- Explain YARN’s role as a resource manager for distributed applications [web:12][web:25].
- Describe key tools in the Hadoop ecosystem: Hive, Pig, Sqoop, Flume, HBase, etc. [web:26][web:32].
- Write basic conceptual workflows using Hive and Pig (no deep code focus in this week).

## File structure

- `01_hadoop_introduction.md` – Why Hadoop was created and its high-level architecture.
- `02_hdfs_architecture.md` – HDFS design, NameNode/DataNode, blocks, replication.
- `03_mapreduce_fundamentals.md` – MapReduce programming model and execution.
- `04_yarn_architecture.md` – YARN as a generic resource manager.
- `05_hadoop_ecosystem_tools.md` – Overview of important ecosystem components.
- `06_hive_introduction.md` – Data warehousing and SQL-on-Hadoop via Hive.
- `07_pig_introduction.md` – Data flow scripting with Pig Latin.
- `practicals/` – HDFS commands, a wordcount walkthrough, and simple Hive/Pig tasks.

## How this connects to other Week 35 modules

- Builds directly on **01_Big_Data_Fundamentals** by giving a concrete platform that addresses Volume, Velocity, and Variety via distributed storage and processing [web:10][web:7].
- Prepares conceptual ground for **03_Apache_Spark_Introduction**, where Spark is presented as a more flexible and faster processing engine that can run on top of Hadoop storage [web:6][web:28].
