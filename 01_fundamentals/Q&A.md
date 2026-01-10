# PySpark Fundamentals - Questions & Answers (50+)

## Beginner Level Questions

### 1. What is Apache Spark?
**A:** Apache Spark is a unified, open-source computing engine designed for large-scale data processing. It provides high-level APIs in Python, Scala, Java, and R, and supports batch processing, streaming, machine learning, and graph processing.

### 2. What are the advantages of Spark over Hadoop MapReduce?
**A:** 
- **Speed**: 10-100x faster due to in-memory processing
- **Ease of use**: Higher-level APIs (SQL, DataFrames, MLlib)
- **Generality**: Supports batch, streaming, SQL, ML in one engine
- **Fault tolerance**: Built-in recovery mechanisms

### 3. What is the difference between Spark and Hadoop?
**A:** Spark is a processing framework, while Hadoop is an ecosystem. Hadoop uses MapReduce for processing (slower, disk-based). Spark uses in-memory processing (faster). Spark can run on top of Hadoop.

### 4. What is a Spark Session?
**A:** SparkSession is the entry point for using Spark with DataFrames and SQL. It encapsulates SparkContext and provides a unified interface for all Spark functionality in modern versions (Spark 2.0+).

### 5. How do you create a Spark Session in PySpark?
**A:**
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .getOrCreate()
```

### 6. What is RDD (Resilient Distributed Dataset)?
**A:** RDD is an immutable, distributed collection of objects that can be processed in parallel. It's the fundamental data structure of Spark with properties like resilience, distribution, and lazy evaluation.

### 7. What does "Resilient" mean in RDD?
**A:** Resilient means fault-tolerant. RDDs can recover from node failures using lineage (the sequence of transformations used to build the RDD).

### 8. What is a DataFrame in Spark?
**A:** DataFrame is a distributed collection of data organized into named columns, similar to a table in SQL or a DataFrame in Pandas. It provides more optimization than RDDs through Catalyst optimizer.

### 9. What is the difference between RDD and DataFrame?
**A:**
| Feature | RDD | DataFrame |
|---------|-----|----------|
| Structure | Unstructured | Structured |
| Optimization | No | Yes (Catalyst) |
| SQL Support | No | Yes |
| Performance | Slower | Faster |
| Type Safety | Weak | Strong |

### 10. When should you use RDD over DataFrame?
**A:** Use RDD when:
- Working with unstructured data (text, images)
- Need low-level transformations
- Custom partitioning is needed
- Non-key-value data handling required

### 11. What is lazy evaluation in Spark?
**A:** Spark doesn't execute transformations immediately when they're called. Execution only happens when an action is invoked. This allows Spark to optimize the entire pipeline before execution.

### 12. Give examples of Spark transformations.
**A:** map, filter, select, join, groupBy, flatMap, reduceByKey, sortByKey, union, distinct, take, collect

### 13. Give examples of Spark actions.
**A:** show(), count(), collect(), first(), take(n), saveAsTextFile(), coalesce(), write, foreach

### 14. What happens when you call show() on a DataFrame?
**A:** show() is an action that triggers the execution of all previous transformations and displays the first 20 rows of the DataFrame in a formatted table.

### 15. What is a Spark Partition?
**A:** A partition is a logical division of data across a cluster. Each partition is processed in parallel on one executor. Partitions enable distributed computing and parallelism.

### 16. What is the default partition count in Spark?
**A:** The default is 200 partitions or determined by the HDFS block size (128MB or 256MB). It can be configured during session creation.

### 17. How do you change the number of partitions?
**A:**
```python
df_repartitioned = df.repartition(10)
df_coalesced = df.coalesce(5)  # Reduce partitions
```

### 18. What is the difference between repartition and coalesce?
**A:** 
- repartition(n): Redistributes data across n partitions (shuffles data)
- coalesce(n): Combines partitions without shuffling (only reduce)

### 19. What is a shuffle in Spark?
**A:** Shuffle is the redistribution of data across partitions. It happens during operations like join, groupBy, reduceByKey. It's expensive due to network I/O and disk I/O.

### 20. What operations trigger a shuffle?
**A:** join, groupBy, reduceByKey, distinct, repartition, sortByKey, coalesce (increase partitions), intersection, union

## Intermediate Level Questions

### 21. What is Catalyst Optimizer?
**A:** Catalyst is Spark's query optimizer for DataFrames. It automatically optimizes execution plans by applying logical and physical transformations like predicate pushdown, filter early application, and join reordering.

### 22. What is Tungsten Execution?
**A:** Tungsten is Spark's execution engine optimization that includes:
- Vectorization: Process batches of rows
- Code generation: Generate optimized Java code
- Memory management: Custom off-heap memory
- CPU efficiency: Better cache locality

### 23. What is caching in Spark?
**A:** Caching stores intermediate results in memory for reuse. It avoids recomputation of expensive operations when the same RDD/DataFrame is used in multiple actions.

### 24. How do you cache an RDD/DataFrame?
**A:**
```python
df.cache()  # or df.persist()
df.show()  # First action: computes and caches
df.count()  # Uses cached data, no recomputation
```

### 25. What are the storage levels in Spark?
**A:**
- MEMORY_ONLY: RAM only
- MEMORY_AND_DISK: RAM first, then disk
- DISK_ONLY: Disk only
- MEMORY_ONLY_2: Replicated 2x in memory
- MEMORY_AND_DISK_2: MEMORY_AND_DISK replicated 2x

### 26. When should you use cache()?
**A:** Cache when:
- RDD/DataFrame is used multiple times
- Operation is expensive (join, aggregation)
- Iterative algorithms (ML training)
- Avoid recomputation across actions

### 27. What is a Spark Job?
**A:** A job is a complete computation triggered by an action. It's represented as a DAG (Directed Acyclic Graph) of stages and tasks.

### 28. What is a Spark Stage?
**A:** A stage is a group of tasks within a job separated by shuffle boundaries. Stages are executed sequentially, and tasks within a stage run in parallel.

### 29. What is a Spark Task?
**A:** A task is the smallest unit of work that runs on a single partition. It's sent to an executor and processes data from one partition.

### 30. What is a DAG (Directed Acyclic Graph)?
**A:** DAG is the logical execution plan created by Spark, showing the sequence of transformations. It enables fault tolerance as Spark can recompute lost data from the lineage.

### 31. What is broadcast variable?
**A:** A broadcast variable sends large read-only data to all executors efficiently, avoiding sending it with every task.

### 32. How do you create a broadcast variable?
**A:**
```python
large_dict = {...}
broadcast_var = spark.broadcast(large_dict)
# Use: broadcast_var.value
```

### 33. What is an accumulator?
**A:** An accumulator is a variable that can only be written to by tasks but read by the driver. Used for counters and debugging.

### 34. How do you create an accumulator?
**A:**
```python
accum = spark.accumulator(0)
df.rdd.foreach(lambda x: accum.add(1))
print(accum.value)  # Read in driver
```

### 35. What is a schema in Spark DataFrame?
**A:** A schema defines the structure of a DataFrame: column names, data types, and nullable flags. It can be inferred or explicitly defined.

### 36. How do you define a schema explicitly?
**A:**
```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])
df = spark.createDataFrame(data, schema)
```

### 37. What is predicate pushdown?
**A:** An optimization where filters are pushed down in the execution plan to be applied as early as possible, reducing data processed in later stages.

### 38. What are narrow and wide transformations?
**A:**
- Narrow: Each output partition depends on one input partition (no shuffle) - map, filter
- Wide: Each output partition depends on multiple input partitions (shuffle) - join, groupBy

### 39. What is data locality?
**A:** Data locality is processing data where it's stored to minimize network I/O. Spark tries to schedule tasks on the executor where data resides.

### 40. What is the Spark Execution Plan?
**A:** The execution plan is how Spark will execute a query. It includes stages, tasks, and how data flows through the pipeline.

## Advanced Level Questions

### 41. What is the difference between persist() and cache()?
**A:** cache() is a shorthand for persist() with MEMORY_ONLY. persist(StorageLevel) allows you to specify the storage level.

### 42. What is the purpose of unpersist()?
**A:** unpersist() removes cached data from memory and executors. Use when you're done with a DataFrame to free up memory.

### 43. What is dynamic partition pruning?
**A:** An optimization that reduces the amount of data read when filtering on partition columns by eliminating unnecessary partitions.

### 44. What is adaptive query execution (AQE)?
**A:** AQE is a feature that optimizes query execution during runtime by:
- Coalescing shuffle partitions
- Converting sort-merge joins to broadcast joins
- Skipping shuffles for skew joins

### 45. What is columnar storage?
**A:** Data organized by columns instead of rows. Beneficial for analytical queries as only required columns are read, saving I/O.

### 46. What is the Spark Web UI?
**A:** Web interface (usually at localhost:4040) showing:
- Jobs and stages
- Task execution details
- Storage (cached data)
- Environment variables
- Executor logs

### 47. How do you monitor Spark application performance?
**A:** Using:
- Spark Web UI
- Metrics (counters, gauges)
- Logging
- Profiling tools
- Cluster manager UI (YARN, Kubernetes)

### 48. What is the purpose of explain()?$
**A:** explain() shows the logical and physical execution plans. Helps understand optimization and identify performance issues.

### 49. What is window function in Spark?
**A:** Functions that operate on a window of rows instead of a single row. Examples: ROW_NUMBER(), RANK(), LAG(), LEAD(), SUM() OVER

### 50. What is the difference between DataFrame and Dataset API?
**A:** 
- DataFrame: Untyped (dynamic typing)
- Dataset: Strongly typed (compile-time type checking)
- Dataset available in Scala/Java, not in Python

### 51. What are the common join types in Spark?
**A:** inner, left, right, outer (full), left_semi, left_anti, cross

### 52. What is a self-join?
**A:** Joining a DataFrame with itself. Useful for hierarchical data or finding relationships within the same table.

### 53. What is bucketing in Spark?
**A:** Bucketing pre-partitions data by a column into a fixed number of buckets during write. Improves performance for frequent join and groupBy on the same column.

### 54. What is skew in data?
**A:** Uneven distribution where some partitions have much more data than others, causing stragglers and performance degradation.

### 55. How do you handle data skew?
**A:** 
- Repartition/reshuffle data
- Use skew-aware join algorithms
- Apply salting techniques
- Use separate buckets for high-frequency values

## Expert Level Questions

### 56. What is the difference between action and lazy transformation?
**A:** Actions execute immediately and return results. Transformations are lazy - they build a DAG but don't execute until an action is called.

### 57. What is the Spark memory model?
**A:** 
- Reserved memory: ~300MB
- Execution memory: For shuffles, joins, sorts
- Storage memory: For caching
- User memory: For user code

### 58. What are the best practices for optimal Spark performance?
**A:**
1. Use DataFrames over RDDs
2. Minimize shuffles
3. Cache strategically
4. Right-size partitions
5. Use appropriate executors
6. Broadcast small tables
7. Monitor via Spark UI
8. Tune memory allocations

### 59. How do you handle null values in Spark?
**A:**
```python
df.na.drop()  # Remove rows with nulls
df.na.fill(value)  # Replace nulls
df.na.replace(mapping)  # Replace with mapping
df.fillna(value)
df.dropna()
```

### 60. What is Spark Streaming?
**A:** Framework for processing streaming data using micro-batches. Enables near real-time processing of data streams with Spark's optimizations and fault tolerance.

---

## Summary

These questions cover the essential concepts needed to master PySpark fundamentals. Study them along with the tutorial files and CONCEPTS.md to gain deep understanding.

**Key Takeaway:** Understanding these concepts will help you:
- Write efficient Spark code
- Debug performance issues
- Design scalable data pipelines
- Optimize resource utilization
- Master advanced Spark topics

---

**Last Updated**: January 2026
**Difficulty**: Beginner to Expert
**Total Questions**: 60+
