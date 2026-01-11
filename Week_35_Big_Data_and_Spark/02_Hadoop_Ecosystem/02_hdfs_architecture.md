# HDFS Architecture

## 1. Purpose of HDFS

Hadoop Distributed File System (HDFS) is designed to store very large files reliably on a cluster and provide high-throughput access to application data [web:21][web:28]. It assumes commodity hardware and is optimized for streaming reads of large datasets rather than low-latency random access.

Key design ideas:

- Store large files as blocks distributed across many nodes.
- Replicate blocks for fault tolerance.
- Prefer moving computation to data rather than data to computation [web:8][web:24].

## 2. NameNode and DataNodes

HDFS follows a master–worker pattern:

- **NameNode**:
  - Maintains the file system namespace (directory tree, file metadata).
  - Stores metadata about which blocks belong to which file and where blocks are located [web:24][web:30].
  - Receives heartbeats and block reports from DataNodes.

- **DataNodes**:
  - Store actual data blocks on local disks.
  - Serve read/write requests for blocks.
  - Perform block creation, deletion, and replication as instructed by NameNode [web:24][web:30].

If a DataNode fails, HDFS uses replication to restore block availability on healthy nodes [web:24][web:27].

## 3. Blocks and replication

HDFS splits files into fixed-size blocks (e.g., 128 MB) and distributes them across DataNodes [web:21][web:30]. Each block is replicated (e.g., replication factor 3) for fault tolerance:

- If one node fails, data can still be read from other replicas.
- NameNode continuously monitors block replication and triggers re-replication if needed [web:24][web:27].

This design allows HDFS to store petabytes of data reliably on clusters of commodity machines.

## 4. Data flow: read and write

High-level flows:

- **Write**:
  - Client contacts NameNode to create a file.
  - NameNode allocates blocks and chooses DataNodes.
  - Client streams data to a pipeline of DataNodes that store block replicas [web:24].

- **Read**:
  - Client contacts NameNode to get block locations.
  - Client reads directly from DataNodes that hold the needed blocks.

HDFS is optimized for streaming reads/writes of large files, not small random reads.

## 5. Limitations and trade-offs

Trade-offs:

- Not ideal for many tiny files (metadata pressure on NameNode).
- High latency for small random reads or writes.
- Designed primarily for **write-once, read-many** access patterns [web:21].

Despite these trade-offs, HDFS remains a foundational storage layer in many Big Data stacks and is commonly used as an underlying store for engines like MapReduce and Spark.
