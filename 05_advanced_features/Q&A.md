# Advanced Spark - Q&A (35 Questions)

## Beginner Level (Q1-Q10)

Q1: What is a UDF?
A: User-Defined Function allowing custom transformations not in Spark API.

Q2: Types of UDFs?
A: Python UDFs (slow), SQL UDFs (optimized), Pandas UDFs (vectorized, 3-100x faster).

Q3: Why Pandas UDFs faster?
A: Use Apache Arrow for efficient data transfer and batch processing instead of row-by-row.

Q4: What is Catalyst Optimizer?
A: Spark's built-in query optimizer analyzing logical/physical plans and applying optimizations.

Q5: What is predicate pushdown?
A: Moving filter conditions close to data source to reduce data processed.

Q6: What is caching?
A: Storing DataFrame/RDD in memory for quick reuse without recomputation.

Q7: When cache data?
A: When accessed multiple times or after expensive computations (joins, aggregations).

Q8: Broadcast variables for?
A: Efficiently sharing large read-only objects across nodes without per-task serialization.

Q9: What is accumulator?
A: Shared mutable variable for safe aggregation of values across tasks.

Q10: What is partitioning?
A: How data is distributed across nodes in a cluster for parallel processing.

## Intermediate Level (Q11-Q25)

Q11: repartition() vs coalesce()?
A: repartition() changes count with shuffle; coalesce() reduces with minimal movement.

Q12: What is shuffle?
A: Re-distributing data across nodes based on keys (groupBy, join operations).

Q13: Cache storage levels?
A: MEMORY_ONLY, MEMORY_AND_DISK, DISK_ONLY, plus replicated versions (_2).

Q14: What unpersist() does?
A: Removes data from cache/storage and frees memory.

Q15: How check execution plan?
A: Call df.explain() or df.explain(extended=True) for detailed plans.

Q16: What is join reordering?
A: Catalyst reorders joins to broadcast small tables first.

Q17: Avoid UDFs in WHERE?
A: UDFs prevent predicate pushdown; condition evaluated after UDF.

Q18: What is bucketing?
A: Pre-partitioning data by column to optimize joins without shuffling.

Q19: What is data skew?
A: Some partitions having much more data, causing unbalanced execution.

Q20: Configure executor memory?
A: Set spark.executor.memory and spark.driver.memory configurations.

Q21: Pandas UDF types?
A: Series->Series (element-wise), Iterator->Iterator (batched), GroupedAgg->Series.

Q22: What projection pushdown?
A: Selecting needed columns early to reduce memory and I/O.

Q23: Cached data doesn't fit?
A: MEMORY_AND_DISK spills to disk; MEMORY_ONLY recomputes.

Q24: Accumulators vs variables?
A: Accumulators distributed and safe for concurrent updates; regular variables aren't.

Q25: Optimal partition size?
A: Typically 100-200MB per partition for balanced performance.

## Advanced Level (Q26-Q35)

Q26: Hash vs range partitioning?
A: Hash uses hash(key) (uneven), range uses key ranges (predictable).

Q27: Executor memory regions?
A: Execution (tasks), Storage (cache), User (data), Reserved (system).

Q28: Delta Lake improvements?
A: ACID transactions, better metadata, schema evolution capabilities.

Q29: What is salting?
A: Adding random salt to keys to redistribute skewed data across partitions.

Q30: Why cache sparingly?
A: Caching consumes memory; only cache data reused multiple times.

Q31: What constant folding?
A: Pre-computing constant expressions at compile time vs runtime.

Q32: Broadcast in join?
A: broadcast(small_df) hints Spark to broadcast instead of shuffling.

Q33: Adaptive query execution?
A: Spark dynamically adjusts plans based on runtime statistics.

Q34: Narrow vs wide transforms?
A: Narrow (map, filter) don't shuffle; wide (groupBy, join) do shuffle.

Q35: RDD persistence vs caching?
A: Similar concept; DataFrames offer more optimization opportunities.
