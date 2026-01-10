# Advanced Spark Features - Core Concepts

## 1. User-Defined Functions (UDFs)

### What are UDFs?
UDFs allow you to define custom functions that are not available in the standard Spark API. They enable complex data transformations tailored to your specific use case.

### Types of UDFs

**Python UDFs**
- Traditional Python functions wrapped for Spark
- Serialized to bytecode and sent to workers
- Performance overhead due to Python/JVM serialization
- Example: `def add_one(x): return x + 1`

**SQL UDFs**
- Defined using SQL expressions
- Compiled to same optimizations as built-in functions
- Better performance than Python UDFs
- Example: `CREATE TEMP FUNCTION add_one AS 'return x + 1'`

**Pandas UDFs (Vectorized)**
- Process batches of data using Pandas DataFrames
- Use Apache Arrow for efficient data transfer
- 3-100x faster than row-at-a-time Python UDFs
- Recommended for most use cases
- Types: Series to Series, Iterator of Series, Series to Series (grouped)

### UDF Decorator Syntax
```python
@udf("IntegerType")
def my_udf(x):
    return x * 2

@pandas_udf("IntegerType")
def my_pandas_udf(s):
    return s * 2
```

### Performance Considerations
- Python UDFs: Expensive serialization, avoid when possible
- Pandas UDFs: Recommended for Python custom logic
- SQL UDFs: Use built-in functions when available
- Avoid UDFs in WHERE clauses (use Python expressions instead)

## 2. Query Optimization

### Catalyst Optimizer
Spark's built-in query optimizer that:
- Analyzes logical and physical execution plans
- Applies optimization rules
- Selects optimal execution strategy
- Works with DataFrames and SQL

### Explain Plans
```python
df.explain()  # Shows execution plan
df.explain(extended=True)  # Shows detailed plan
```

Plan stages:
1. **Parsed Logical Plan**: Original query structure
2. **Analyzed Logical Plan**: With type information
3. **Optimized Logical Plan**: After rule application
4. **Physical Plan**: How it will execute

### Key Optimizations

**Predicate Pushdown**
- Moves filter conditions as close to data source as possible
- Reduces data processed
- Automatically applied by Catalyst

**Projection Pushdown**
- Only selects needed columns
- Reduces memory and I/O

**Join Reordering**
- Reorders joins for optimal execution
- Broadcasts small tables first

**Constant Folding**
- Pre-computes constant expressions
- Reduces runtime computation

## 3. Caching and Persistence

### Cache Levels

**MEMORY_ONLY**
- Stores entire RDD in memory
- If doesn't fit, recomputes missing partitions
- Fastest access

**MEMORY_AND_DISK**
- Stores in memory first
- Spills to disk if memory full
- Balanced performance/reliability

**DISK_ONLY**
- Only stores on disk
- Slowest but most reliable

**MEMORY_ONLY_2, MEMORY_AND_DISK_2**
- Replicates across 2 nodes
- For fault tolerance

### When to Cache
- Data accessed multiple times
- Expensive computations (joins, aggregations)
- Intermediate results in complex pipelines
- Do NOT cache if used only once

### Cache Management
```python
df.cache()  # Mark for caching
df.persist(StorageLevel.MEMORY_AND_DISK)
df.unpersist()  # Remove from cache
spark.catalog.clearCache()  # Clear all
```

## 4. Broadcast Variables

### Purpose
Efficiently share large read-only objects across nodes without serializing for each task.

### Usage
```python
broadcast_var = spark.broadcast(large_dict)
# Access: broadcast_var.value
```

### Benefits
- Reduces network traffic
- Reduces serialization overhead
- Enables efficient joins with lookup tables

### Use Cases
- Reference tables for joins
- Configuration data
- Lookup dictionaries
- Model coefficients

## 5. Accumulators

### Purpose
Shared mutable variable for safe aggregation across tasks.

### Types
- **NumericAccumulator**: For numbers
- **CollectionAccumulator**: For collections
- **Custom Accumulator**: Implement AccumulatorV2

### Usage
```python
acc = spark.sparkContext.accumulator(0)
rdd.foreach(lambda x: acc.add(x))
print(acc.value)
```

### Important Rules
- Only accessible in actions, not transformations
- Guaranteed to be incremented only once per task
- Not for distributed reads, only aggregation

## 6. Data Partitioning

### Partition Strategy
Determines how data is distributed across nodes.

**Hash Partitioning**
- Distributes by hash of key
- Default for groupBy, join
- May create skewed partitions

**Range Partitioning**
- Divides into ranges
- Better for sorted data
- Predictable distribution

**Bucket Partitioning**
- Pre-partitions by column
- Optimizes joins
- Defined at table creation

### Repartition vs Coalesce
- **repartition()**: Changes partition count, causes shuffle
- **coalesce()**: Reduces partitions, minimal shuffle
- Use coalesce() to reduce partitions, repartition() to increase

### Optimal Partition Size
- Target: 100MB - 200MB per partition
- Too small: Overhead, slow
- Too large: Memory issues, unbalanced

## 7. Shuffle Operations

### What is a Shuffle?
Re-distributes data across nodes based on key.

### Expensive Operations (cause shuffle)
- groupBy(), reduceByKey()
- join(), repartition()
- union()

### Shuffle Optimization
- Use broadcast join for small tables
- Pre-partition data when possible
- Use bucketing for repetitive joins
- Avoid unnecessary shuffles

## 8. Memory Management

### Memory Regions
- **Execution Memory**: Tasks, shuffles, joins
- **Storage Memory**: Caching, broadcast
- **User Memory**: User data structures
- **Reserved Memory**: System operations

### Configuration
```python
spark.conf.set("spark.executor.memory", "4g")
spark.conf.set("spark.driver.memory", "2g")
spark.conf.set("spark.memory.fraction", 0.6)
```

## 9. Skew Handling

### Data Skew
When some partitions have much more data than others.

### Effects
- Unbalanced execution
- Slow tasks
- OOM errors

### Solutions
- Repartition on different column
- Use salting technique
- Adaptive query execution
- Broadcast join instead

## 10. Delta Lake Integration

### Benefits
- ACID transactions
- Time travel/versioning
- Schema evolution
- Better optimization
- Unified batch and streaming

### Usage
```python
df.write.format("delta").mode("overwrite").save("/path")
df = spark.read.format("delta").load("/path")
```

## Key Takeaways

1. Use Pandas UDFs for custom Python logic
2. Always check explain() plans
3. Cache only frequently-accessed data
4. Broadcast small tables
5. Optimize partitioning early
6. Monitor and manage memory
7. Use Delta Lake for reliability
8. Minimize shuffle operations
9. Profile before optimizing
10. Test with production-scale data
