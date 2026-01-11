# YARN Architecture

## 1. Purpose of YARN

YARN (Yet Another Resource Negotiator) is Hadoop’s generic resource management and job scheduling layer [web:12][web:25]. It was introduced in Hadoop 2.x to decouple resource management from the MapReduce engine and allow multiple processing frameworks to share the same cluster.

Key goals:

- Manage CPU and memory resources across applications.
- Schedule and monitor distributed applications.
- Support diverse processing models (batch, streaming, interactive) on top of HDFS [web:12][web:21].

## 2. Main components

YARN includes three main components:

- **ResourceManager (RM)**:
  - Global authority for resource allocation.
  - Decides which applications (jobs) get resources and when [web:25].

- **NodeManager (NM)**:
  - Runs on each worker node.
  - Reports resources and health to RM.
  - Manages containers (processes) running on that node [web:12][web:21].

- **ApplicationMaster (AM)**:
  - One per application/job.
  - Negotiates resources from RM.
  - Coordinates tasks for its application on NodeManagers [web:22][web:25].

## 3. Typical YARN application flow

High-level execution steps [web:22][web:25]:

1. Client submits an application (e.g., MapReduce job, Spark job) to the **ResourceManager**.
2. RM starts an **ApplicationMaster** in a container on some NodeManager.
3. AM registers with RM and requests containers for tasks.
4. RM allocates containers on various NodeManagers.
5. AM launches tasks in those containers and monitors their progress.
6. On completion, AM reports final status to RM and shuts down.

This pattern is common across YARN-compatible frameworks.

## 4. Benefits of YARN

Benefits:

- **Multi-tenancy**: Multiple frameworks (MapReduce, Spark, Tez, etc.) can run on the same cluster [web:12][web:28].
- **Better utilization**: Flexible scheduling and resource sharing improve cluster utilization.
- **Scalability**: Designed to scale with large clusters and many concurrent applications [web:16][web:21].

Understanding YARN clarifies how Hadoop evolved from “just MapReduce” to a more general Big Data platform.

## 5. YARN and Spark

Spark can run:

- In **YARN cluster mode**, where the driver runs inside the cluster managed by YARN.
- In **YARN client mode**, where the driver runs outside but executors run as YARN containers.

This means your Hadoop knowledge will directly help when you configure and run Spark jobs on Hadoop clusters [web:6][web:21].
