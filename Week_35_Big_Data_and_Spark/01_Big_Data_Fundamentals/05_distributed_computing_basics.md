# Distributed Computing Basics for Big Data

This file explains the minimum distributed computing concepts you need before diving into Hadoop and Spark [web:8][web:12].

## 1. Why single-machine approaches break

Limitations:

- **Storage**: A single machine has finite disk and memory.
- **Compute**: CPU and I/O can become bottlenecks as data grows.
- **Reliability**: Single point of failure; hardware issues bring the whole system down [web:10].

For Big Data workloads, vertical scaling (adding more resources to one machine) becomes too expensive or technically insufficient.

## 2. Horizontal scaling and clusters

Key idea:

- Instead of one very powerful machine, use **many commodity machines** (nodes) connected in a cluster.
- Distribute both data and computation across these nodes.

Benefits:

- Scale-out by adding more nodes.
- Improved aggregate storage and compute.
- Potential for fault tolerance via replication.

## 3. Data partitioning and locality

Concepts:

- Datasets are split into **partitions** or blocks and stored across nodes.
- Computations are scheduled “close” to where data resides to reduce network I/O (data locality) [web:8][web:16].

This is a core idea in systems like HDFS and MapReduce, and later Spark.

## 4. Fault tolerance

In a cluster:

- Nodes can fail at any time.
- Distributed systems must detect failures and recover without losing data [web:12].

Typical techniques:

- Replicating data across multiple nodes (HDFS).
- Recomputing lost work from lineage or intermediate state (Spark’s RDDs) [web:9].

## 5. Coordination and resource management

Challenges:

- Many jobs compete for CPU, memory, and I/O across the cluster.
- Need a central (or logically central) component to schedule and allocate resources.

Solutions:

- Resource managers like YARN that assign containers and track node health [web:12].
- Cluster managers used by Spark (Standalone, YARN, Kubernetes).

## 6. Where Hadoop and Spark fit

- **HDFS**: Distributed file system handling storage and replication.
- **MapReduce**: Distributed batch processing framework on top of HDFS.
- **YARN**: Resource manager for the Hadoop ecosystem [web:8][web:12].
- **Spark**: General-purpose distributed computing engine that can run on top of HDFS and other storage systems, providing richer APIs and in-memory processing [web:6][web:9].

The **next Week 35 folder (02)** will formalize these ideas in the context of the Hadoop ecosystem, and the **03+ folders** will build on them for Spark.
