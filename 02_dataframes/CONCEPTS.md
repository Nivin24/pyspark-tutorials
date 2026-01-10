# PySpark DataFrame Concepts

## Table of Contents
1. DataFrame Fundamentals
2. DataFrame Creation Methods
3. DataFrame Operations
4. Filtering and Selection
5. Aggregations
6. Joins
7. GroupBy and Window Functions
8. Performance Optimization
9. Best Practices

## 1. DataFrame Fundamentals

### What is a DataFrame?
A DataFrame is an immutable distributed collection of data organized into named columns. It is the most common data structure in Apache Spark and provides a SQL-like interface for data manipulation.

### Key Characteristics:
- **Immutable**: Once created, DataFrames cannot be changed
- **Distributed**: Data is partitioned across multiple nodes
- **Lazy Evaluation**: Operations are not executed until an action is called
- **Schema**: Each DataFrame has a schema defining column names, types, and nullability

### DataFrame vs RDD
- RDDs: Lower-level, more flexible but slower
- DataFrames: Higher-level, optimized, SQL-like interface

## 2. DataFrame Creation Methods

### Method 1: From Python Lists
```python
data = [(1, "Alice"), (2, "Bob")]
df = spark.createDataFrame(data, ["id", "name"])
```

### Method 2: From Pandas DataFrame
```python
import pandas as pd
pdf = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
df = spark.createDataFrame(pdf)
```

### Method 3: From External Sources
```python
df = spark.read.csv("path/to/file.csv", header=True)
df = spark.read.parquet("path/to/file.parquet")
df = spark.read.json("path/to/file.json")
```

### Method 4: With Explicit Schema
```python
from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([StructField("name", StringType())])
df = spark.createDataFrame(data, schema)
```

## 3. DataFrame Operations

### Common Operations
- **select()**: Choose specific columns
- **drop()**: Remove columns
- **withColumn()**: Add or modify columns
- **withColumnRenamed()**: Rename columns
- **orderBy()**: Sort data
- **limit()**: Restrict number of rows

### Transformations
Transformations create a new DataFrame from an existing one:
- All transformation operations are LAZY
- They are not executed until an action is called

### Actions
Actions trigger computation and return results:
- show(): Display rows
- collect(): Return all rows to driver
- count(): Count rows
- write(): Save to external source

## 4. Filtering and Selection

### Filter Conditions
- Use column expressions: `df.filter(df.age > 25)`
- Use SQL strings: `df.filter("age > 25")`
- Use multiple conditions: `df.filter((df.age > 25) & (df.salary > 50000))`

### Logical Operators
- AND: `&`
- OR: `|`
- NOT: `~`

### String Operations
- contains(): Check if string contains substring
- startswith(): Check if starts with
- endswith(): Check if ends with
- like(): Pattern matching

## 5. Aggregations

### Aggregate Functions
- count(): Number of non-null values
- sum(): Total of numeric values
- avg(): Average of numeric values
- min()/max(): Minimum/Maximum values
- stddev(): Standard deviation
- variance(): Variance

### GroupBy
Partition data into groups and apply aggregations:
```python
df.groupBy("department").agg({"salary": "sum"})
df.groupBy("dept", "job").count()
```

## 6. Joins

### Join Types
- **Inner Join**: Only matching records from both DataFrames
- **Left Outer Join**: All records from left, matching from right
- **Right Outer Join**: All records from right, matching from left
- **Full Outer Join**: All records from both DataFrames
- **Left Semi Join**: Records from left with matches in right (right columns not included)
- **Left Anti Join**: Records from left with NO matches in right
- **Cross Join**: Cartesian product of both DataFrames

### Join Syntax
```python
df1.join(df2, df1.id == df2.id, "inner")
```

## 7. GroupBy and Window Functions

### Window Functions
Allow computation across a set of rows related to current row:
- **Ranking**: row_number(), rank(), dense_rank()
- **Analytic**: lead(), lag(), first(), last()
- **Aggregate**: sum(), avg(), count() (as window functions)

### Window Specification
```python
from pyspark.sql import Window
window = Window.partitionBy("dept").orderBy("salary")
```

## 8. Performance Optimization

### Caching
Cache frequently used DataFrames in memory:
```python
df.cache()  # or df.persist()
df.show()  # First action materializes cache
```

### Partitioning
Distribute data for parallel processing:
- Partition by columns with few distinct values
- Increases parallelism

### Broadcasting
Send small DataFrames to all nodes:
```python
from pyspark.sql.functions import broadcast
df.join(broadcast(small_df), "key")
```

## 9. Best Practices

1. **Use Column Objects**: `df.salary` instead of strings when possible
2. **Select Only Needed Columns**: Reduce data movement
3. **Filter Early**: Push filters down the execution plan
4. **Avoid Collect()**: Can cause out-of-memory errors
5. **Use SQL**: For complex queries, SQL is often clearer
6. **Understand Lazy Evaluation**: Plan your code accordingly
7. **Monitor Performance**: Use Spark UI to identify bottlenecks
8. **Partition Wisely**: Balance parallelism with overhead
