# Introduction to Apache Hadoop

## 1. Why Hadoop?

Hadoop was created to store and process massive web-scale datasets on clusters of inexpensive commodity hardware, inspired by Google’s GFS and MapReduce papers [web:8][web:31]. Instead of relying on a single powerful machine, Hadoop distributes both data and computation across many nodes to handle Big Data workloads.

Key goals:

- **Scalability**: Add more nodes to handle more data and computation.
- **Fault tolerance**: Keep working even if some nodes fail.
- **Cost efficiency**: Use commodity hardware instead of specialized high-end servers [web:8][web:12].

## 2. Core components (high level)

The Hadoop framework is built around three core components:

- **HDFS (Hadoop Distributed File System)** – Distributed, fault-tolerant file system for storing large datasets [web:21][web:24].
- **MapReduce** – Distributed batch processing framework that divides work into map and reduce tasks [web:20][web:31].
- **YARN (Yet Another Resource Negotiator)** – Resource management and job scheduling layer for Hadoop [web:12][web:25].

These components together provide storage, processing, and cluster resource management capabilities.

## 3. Master–slave architecture

A typical Hadoop cluster follows a **master–slave** (now often called leader–worker) architecture:

- Master nodes run services such as **NameNode** (HDFS), **ResourceManager** (YARN), and job history servers [web:8][web:21].
- Worker nodes run **DataNode** (HDFS) and **NodeManager** (YARN) daemons, storing data blocks and executing tasks [web:8][web:16].

This separation allows centralized coordination while leveraging many workers for parallelism.

## 4. Hadoop’s role in the Big Data stack

Hadoop provides:

- A place to store raw and processed data **once** (HDFS).
- A way to run batch analytics over this data (MapReduce and other engines) [web:20][web:28].
- A common resource management layer (YARN) that multiple engines (MapReduce, Spark, etc.) can share [web:12][web:25].

Later sections and modules will show how Spark can coexist with and extend beyond MapReduce while still leveraging the Hadoop ecosystem.
