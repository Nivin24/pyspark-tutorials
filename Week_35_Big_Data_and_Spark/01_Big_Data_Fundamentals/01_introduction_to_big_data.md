# Introduction to Big Data

## 1. What is Big Data?

Big Data refers to data that is so large, fast, or complex that traditional data processing tools (single-node databases, spreadsheets, simple scripts) cannot store, process, or analyze it efficiently [web:10]. It is not only about size but also about the speed of generation and the variety of formats involved [web:4][web:14].

Key points:

- Too **large** to fit on a single machine’s storage or memory.
- Generated too **quickly** to be handled with simple batch jobs.
- Too **diverse** in format to fit neatly into relational tables.

## 2. Evolution of data processing

### 2.1 Traditional (pre–Big Data) stack

- Relational databases (RDBMS) with SQL.
- Single-server deployments, vertical scaling (add more CPU/RAM).
- Suitable for GB-level structured data and transactional workloads.

### 2.2 Why this model broke

- Explosion of web, mobile, IoT, logs, clickstreams, and sensor data.
- Data volumes grew to TBs and PBs, and read/write rates increased beyond what a single node could handle [web:10].
- Unstructured and semi-structured data (JSON, logs, images) became common.

## 3. Big Data era technologies (high level)

To cope with these challenges, new systems were introduced:

- **Hadoop ecosystem** for distributed storage and batch processing on clusters of commodity machines [web:8][web:12].
- **Apache Spark** for fast, in-memory, general-purpose data processing on top of distributed storage [web:6][web:9].

You will study Hadoop in the next folder and Spark in the following ones, but for now, just understand that they are answers to the limitations of traditional systems.

## 4. When does a problem become a “Big Data” problem?

Ask questions like:

- Can one machine store the raw data and intermediate results comfortably?
- Can one machine process the data within the required time (SLA)?
- Is the data coming too fast or in too many different formats?
- Do we need horizontal scaling, fault tolerance, and parallelism?

If the answer is “no” for single-node solutions, or you hit clear limits on storage/performance, you are in Big Data territory [web:10].

## 5. How this file should guide you

After reading:

- You should be able to explain Big Data in your own words without mentioning specific tools.
- You should clearly articulate why we need distributed storage and processing.
- You should be ready to study the 5Vs in detail in `02_characteristics_5Vs.md`.
