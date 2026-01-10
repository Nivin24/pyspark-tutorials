# PySpark Fundamentals - Theoretical Concepts

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Core Architecture](#core-architecture)
3. [Key Concepts](#key-concepts)
4. [RDD vs DataFrame](#rdd-vs-dataframe)
5. [Execution Model](#execution-model)
6. [Optimization Concepts](#optimization-concepts)

---

## Prerequisites

Before learning PySpark fundamentals, you should have:

### Software
- **Python 3.7 or higher** - Basic Python knowledge
- **Java 8 or 11** - Spark runs on JVM
- **Scala basics** - Optional but helpful to understand Spark documentation

### Knowledge
- **Python fundamentals** - Variables, functions, loops, data structures
- **SQL basics** - SELECT, WHERE, JOIN, GROUP BY
- **Distributed computing concepts** - Basic understanding of parallel processing
- **Command line/Terminal** - Ability to run commands

### Mathematical Background
- **Linear algebra basics** - Vectors, matrices (for ML later)
- **Statistics fundamentals** - Mean, median, standard deviation

---

## Core Architecture

### What is Apache Spark?

Apache Spark is a **unified computing engine** designed for:
- **Speed**: In-memory processing, 10-100x faster than MapReduce
- **Ease of use**: High-level APIs in Python, Scala, Java, R
- **Generality**: Works with diverse workloads (batch, streaming, ML, graph)
- **Fault tolerance**: Automatic recovery from node failures

### Spark Ecosystem

```
┌─────────────────────────────────────────────────┐
│           Spark Applications (APIs)             │
├─────────────────────────────────────────────────┤
│  Spark SQL  │  Spark ML  │  MLlib  │ GraphX   │
├─────────────────────────────────────────────────┤
│         Spark Core (RDDs, Datasets)             │
├─────────────────────────────────────────────────┤
│    Cluster Manager (Standalone, YARN, K8s)     │
├─────────────────────────────────────────────────┤
│   Storage (HDFS, S3, GCS, Local File System)    │
└─────────────────────────────────────────────────┘
```

### Spark Cluster Architecture

#### Components:

1. **Driver Program**
   - Runs the main() function
   - Creates SparkContext/SparkSession
   - Executes user code
   - Single entry point for Spark application
   - Responsible for orchestration

2. **Cluster Manager**
   - Allocates resources across machines
   - Types: Standalone, YARN, Kubernetes, Mesos
   - Manages executor processes

3. **Executor Nodes**
   - Run tasks assigned by driver
   - Each node can have multiple executors
   - In-memory storage for cached data
   - Execute code and return results to driver

4. **Worker Nodes**
   - Physical machines that run executors
   - Store partitioned data
   - Process data in parallel

#### Data Flow:
```
Driver → Cluster Manager → Executors → Storage
↑_________________________________↓
        Results & State
```

---

## Key Concepts

### 1. Spark Context vs Spark Session

#### SparkContext
- **Old API** (Spark 1.x)
- Entry point for RDD operations
- Manages cluster connection
- Single context per application
```python
from pyspark import SparkContext
sc = SparkContext("local", "AppName")
```

#### SparkSession
- **Modern API** (Spark 2.0+)
- Entry point for DataFrame and SQL operations
- Encapsulates SparkContext
- Unified interface
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("AppName").getOrCreate()
```

### 2. RDDs (Resilient Distributed Datasets)

#### Definition
RDD is an **immutable, distributed collection** of objects that can be processed in parallel.

#### Properties
- **Resilient (Fault-Tolerant)**: Recover from node failures using lineage
- **Distributed**: Data split across multiple nodes
- **Immutable**: Cannot be changed after creation
- **Lazy Evaluation**: Transformations not computed until action is called

#### RDD Lineage (DAG)
- Directed Acyclic Graph of transformations
- Enables fault tolerance without replication
- Allows Spark to recompute lost data

### 3. DataFrames

#### Definition
DataFrame is a **distributed collection of data organized in columns** (like SQL tables or Pandas DataFrames).

#### Advantages over RDDs
- **Structured data**: Named columns with types
- **SQL queries**: Can use SQL syntax
- **Optimization**: Catalyst optimizer for query plans
- **Memory efficiency**: Columnar storage format (Parquet)
- **APIs**: Multiple languages (Python, Scala, R, Java)

#### Schema
- Defines structure: column names, types, nullable flags
- Can be inferred or explicitly defined
- Enables optimization and validation

### 4. Partitions

#### What are Partitions?
- Data is split into **logical chunks** across cluster
- Each partition processed in parallel on one executor
- Key to parallelism in Spark

#### Partition Size
- Default: 200 partitions or 128MB per partition (HDFS block size)
- Too few: Underutilized resources
- Too many: High overhead from task scheduling
- Optimal: 1-4 partitions per executor core

#### Partitioning Benefits
- **Parallelism**: Process multiple partitions simultaneously
- **Locality**: Process data where it's stored (data locality)
- **Fault tolerance**: Replace failed partition from lineage

### 5. Lazy Evaluation

#### Definition
Transformations are **not executed immediately** when called. Execution happens only when an **action** is invoked.

#### Benefits
- **Optimization**: Spark optimizes entire pipeline before execution
- **Efficiency**: Avoid unnecessary computation
- **Pipeline fusion**: Combine multiple transformations

#### Example
```python
df = spark.read.csv("file.csv")  # No execution
df2 = df.filter(df.age > 25)     # Still no execution
result = df2.show()              # NOW execution happens!
```

---

## RDD vs DataFrame

| Feature | RDD | DataFrame |
|---------|-----|----------|
| **Structure** | Unstructured | Structured (columns) |
| **API Level** | Low-level | High-level |
| **Optimization** | No | Yes (Catalyst) |
| **SQL Support** | No | Yes |
| **Memory** | Slower | Faster (Tungsten) |
| **Type Safety** | Weak | Strong (schema) |
| **Use Case** | Unstructured data | Structured data |
| **Performance** | Slower | Faster |

### When to use RDD?
- Unstructured text data
- Need low-level transformations
- Working with non-key-value data
- Custom partitioning logic

### When to use DataFrame?
- Structured/semi-structured data
- SQL operations needed
- High performance required
- Integration with other tools
- Most modern use cases

---

## Execution Model

### Transformation vs Action

#### Transformations
- Return new RDD/DataFrame
- Lazy: not executed immediately
- Examples: map, filter, select, join, groupBy
- Create lineage (DAG)

```python
df2 = df.filter(df.age > 25)  # Transformation
df3 = df2.select("name", "age")  # Another transformation
```

#### Actions
- Return results to driver or write to storage
- Trigger actual computation
- Examples: show, count, collect, save, take, first

```python
df3.show()  # Action - triggers execution
count = df3.count()  # Action - triggers execution
```

### Job, Stage, and Task

#### Job
- Corresponds to action
- Full computation from data source to result
- Example: `df.show()` triggers one job

#### Stage
- Group of tasks within a job
- Separated by shuffle boundaries
- Sequential within a job
- Example: 2 stages if join operation present

#### Task
- Unit of work on a single partition
- Sent to executor nodes
- Example: Apply filter to one partition

#### Relationship
```
Action (Job)
  ↓
Stage 1 (No shuffle)
  ├─ Task 1 (on Partition 1)
  ├─ Task 2 (on Partition 2)
  └─ Task N (on Partition N)
  ↓
Stage 2 (After shuffle)
  ├─ Task 1 (on Partition 1)
  ├─ Task 2 (on Partition 2)
  └─ Task N (on Partition N)
```

### Shuffle Operation

#### Definition
**Redistribution of data** across partitions when operation requires grouping or joining.

#### When Shuffle Happens
- groupBy, reduceByKey
- join, cogroup
- repartition, sortByKey

#### Shuffle Cost
- Most expensive operation
- Network I/O and disk I/O
- Multiple stages in job
- Minimize shuffles for performance

---

## Optimization Concepts

### Catalyst Optimizer

Optimizes DataFrame queries automatically:

1. **Logical Optimization**
   - Push filters early (predicate pushdown)
   - Combine operations
   - Remove redundant operations

2. **Physical Optimization**
   - Choose best join strategy
   - Select index structures
   - Determine partition strategy

3. **Cost-Based Optimization**
   - Analyze table statistics
   - Choose lowest-cost execution plan

### Tungsten Execution

- **Vectorization**: Process batches of rows
- **Code generation**: Generate optimized Java code
- **Memory management**: Custom off-heap memory management
- **CPU efficiency**: Better cache locality
- **Result**: 2-10x faster than RDD operations

### Caching & Persistence

#### Cache
- Store intermediate results in memory
- Reuse across multiple actions
- Avoid recomputation of expensive operations

```python
df.cache()  # or df.persist()
df.show()  # First action computes and caches
df.count()  # Uses cached data
```

#### Storage Levels
- **MEMORY_ONLY**: RAM only (fast, may evict)
- **MEMORY_AND_DISK**: RAM first, then disk
- **DISK_ONLY**: Disk only (slow)
- **MEMORY_ONLY_2**: Replicated in memory

#### When to Cache
- RDD used multiple times
- Expensive operation result
- DataFrame used in multiple actions
- Iterative algorithms (ML)

### Broadcast Variables

- Send large read-only data to executors
- Avoid sending in every task
- Efficient when used in joins or lookups

```python
broadcast_var = spark.broadcast(large_dict)
# Use broadcast_var.value in transformations
```

### Accumulators

- Variables sent to executors for counters
- Only driver can read values
- Updated in parallel across tasks
- Used for debugging or counting events

```python
accum = spark.accumulator(0)
df.rdd.foreach(lambda x: accum.add(1))
print(accum.value)  # Total count
```

---

## Best Practices

### Performance
1. ✅ Use DataFrames over RDDs when possible
2. ✅ Cache intermediate results used multiple times
3. ✅ Minimize shuffle operations
4. ✅ Push filters as early as possible
5. ✅ Use appropriate partition count
6. ✅ Broadcast small lookup tables

### Code Quality
1. ✅ Use SparkSession for new applications
2. ✅ Always define schema explicitly
3. ✅ Use column expressions instead of strings
4. ✅ Handle null values explicitly
5. ✅ Test with sample data before full run

### Resource Management
1. ✅ Set appropriate executor memory
2. ✅ Adjust number of executors based on data
3. ✅ Monitor job execution in Spark UI
4. ✅ Use proper serialization (Kryo)
5. ✅ Clean up resources (stop sessions)

---

## Key Takeaways

- Spark is a distributed computing engine optimized for speed
- Lazy evaluation enables optimization
- Partitions enable parallelism across clusters
- DataFrames provide structure and optimization
- Understanding DAG helps troubleshoot performance
- Caching and partitioning are critical for optimization
- Shuffle is expensive, minimize when possible

---

## Next Steps

After understanding these concepts:
1. Study the tutorial files (01, 02, 03, 04)
2. Run code examples and modify them
3. Understand Spark UI to see execution
4. Move to advanced topics (SQL, MLlib)
5. Build real-world applications

---

**Last Updated**: January 2026
