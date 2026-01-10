# PySpark DataFrame Q&A

## Beginner Level

### Q1: What is a PySpark DataFrame?
**A:** A DataFrame is an immutable distributed collection of data organized into named columns. It provides a SQL-like interface.

### Q2: How do you create a DataFrame from a Python list?
**A:** Using `spark.createDataFrame(data, columns)` where data is a list of tuples.

### Q3: What is the difference between show() and collect()?
**A:** show() displays the first 20 rows, collect() brings all rows to driver memory.

### Q4: How do you select specific columns?
**A:** Using select(): `df.select("name", "salary")`

### Q5: What does filter() do?
**A:** filter() applies a condition and returns rows that match the condition.

### Q6: How do you rename a column?
**A:** Using withColumnRenamed(): `df.withColumnRenamed("old_name", "new_name")`

### Q7: What is lazy evaluation in Spark?
**A:** Operations are not executed immediately until an action is called.

### Q8: How do you add a new column?
**A:** Using withColumn(): `df.withColumn("new_col", df.salary * 1.1)`

### Q9: What is a transformation vs an action?
**A:** Transformations are lazy, actions trigger computation and return results.

### Q10: How do you sort a DataFrame?
**A:** Using orderBy(): `df.orderBy(df.salary.desc())`

## Intermediate Level

### Q11: What are different ways to filter data?
**A:** Using filter/where with column expressions, SQL strings, or logical operators.

### Q12: What is a join and its types?
**A:** Combines data from two DataFrames. Types: inner, left_outer, right_outer, outer, left_semi, left_anti, cross.

### Q13: What is groupBy?
**A:** Partitions data by columns and applies aggregations.

### Q14: What are window functions?
**A:** Compute values across rows related to the current row for ranking and lead/lag.

### Q15: How do you handle NULL values?
**A:** Using isNull(), isNotNull(), and na functions.

### Q16: What is schema inference?
**A:** Automatically detecting column names and types when creating a DataFrame.

### Q17: How do you join two DataFrames?
**A:** Using join(): `df1.join(df2, df1.id == df2.id, "inner")`

### Q18: What aggregation functions are available?
**A:** count(), sum(), avg(), min(), max(), stddev(), variance().

### Q19: How do you apply aggregations without groupBy?
**A:** Using agg() directly: `df.agg({"salary": "sum"})`

### Q20: What is the purpose of cache()?
**A:** Caches frequently used DataFrames in memory to avoid recomputation.

## Advanced Level

### Q21: How do you optimize a slow Spark job?
**A:** Increase partitions, use broadcast, push filters down, select needed columns, cache results.

### Q22: What is data skew?
**A:** Uneven distribution of data. Handle using salting technique on join keys.

### Q23: What is the Catalyst optimizer?
**A:** Spark's query optimizer converting logical plans to optimized physical plans.

### Q24: How do you write a DataFrame to different formats?
**A:** Using write.format(): `df.write.format("parquet").save("path")`

### Q25: What is partitioning in Spark?
**A:** Dividing data across nodes for parallel processing.

### Q26: How do you use broadcasting in joins?
**A:** Using broadcast(): `df.join(broadcast(small_df), "key")`

### Q27: What is dynamic partitioning?
**A:** Automatically determining partition count based on data size.

### Q28: How to handle extremely large DataFrames?
**A:** Use persist(), broadcast small tables, increase memory, use Parquet.

### Q29: persist() vs cache()?
**A:** cache() uses memory only. persist() allows specifying storage level.

### Q30: Window operations with ordering?
**A:** Use Window.partitionBy().orderBy() with rank/row_number functions.

## Advanced Concepts

### Q31: What is shuffle in Spark?
**A:** Moving data across partitions - expensive operation.

### Q32: How to estimate job duration?
**A:** Monitor Spark UI, check data size, partitions, and transformations.

### Q33: What are UDFs and drawbacks?
**A:** Custom functions but bypass optimization and may be slower.

### Q34: Columnar formats like Parquet?
**A:** Read: `spark.read.parquet("path")`. Write: `df.write.parquet("path")`

### Q35: Columnar storage advantages?
**A:** Better compression, faster queries on specific columns.

### Q36: Partition during write?
**A:** Using partitionBy(): `df.write.partitionBy("year").parquet("path")`

### Q37: Role of driver?
**A:** Runs main program, creates DataFrames, coordinates task execution.

### Q38: Handle skewed joins?
**A:** Use salting to add random values to join keys.

### Q39: What is bucketing?
**A:** Pre-partitioning for efficient joins on specific columns.

### Q40: Avoid out-of-memory errors?
**A:** Avoid collect(), use iterators, increase memory, partition wisely.

### Q41: Common performance bottlenecks?
**A:** Shuffle, broadcasting large tables, collect(), unoptimized joins.

### Q42: Debug Spark jobs?
**A:** Use Spark UI, check logs, use narrow transformations.

### Q43: What is execution plan?
**A:** explain() shows logical and physical plans from optimizer.

### Q44: Handle late-arriving data?
**A:** Use watermarks with structured streaming.

### Q45: DataFrame vs Dataset?
**A:** Dataset is type-safe (Scala/Java), DataFrame untyped (Python).

### Q46: Manage memory in Spark?
**A:** Use spark.executor.memory, spark.driver.memory config.

### Q47: Impact of partition count?
**A:** Too few: slow. Too many: overhead. Balance needed.

### Q48: Handle nested JSON structures?
**A:** Use explode() to flatten arrays, col() for nested fields.

### Q49: reduceByKey vs groupBy?
**A:** reduceByKey is RDD, groupBy is DataFrame (preferred).

### Q50: Adaptive query execution?
**A:** Set spark.sql.adaptive.enabled=true for runtime optimization.
