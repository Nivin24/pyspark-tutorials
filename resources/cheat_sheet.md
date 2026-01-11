# PySpark Quick Reference Cheat Sheet

## Session Management

### Create Spark Session
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AppName") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

sc = spark.sparkContext  # Get context
```

### Configuration
```python
# Set configurations
spark.conf.set("spark.sql.shuffle.partitions", "100")

# Get configuration
partitions = spark.conf.get("spark.sql.shuffle.partitions")

# Adaptive query execution
spark.conf.set("spark.sql.adaptive.enabled", "true")
```

### Stop Session
```python
spark.stop()
```

---

## Creating DataFrames

### From Python Collections
```python
data = [(1, "Alice", 25), (2, "Bob", 30)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)
```

### From Pandas DataFrame
```python
import pandas as pd
pdf = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
df = spark.createDataFrame(pdf)
```

### Reading Data
```python
# CSV
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# JSON
df = spark.read.json("path/to/file.json")

# Parquet
df = spark.read.parquet("path/to/file.parquet")

# Text
df = spark.read.text("path/to/file.txt")

# Option chaining
df = spark.read \
    .option("header", "true") \
    .option("delimiter", ",") \
    .csv("file.csv")
```

---

## DataFrame Basics

### Display & Information
```python
df.show()              # Show first 20 rows
df.show(5)            # Show 5 rows
df.show(truncate=False)  # Full column width
df.printSchema()      # Show schema
df.dtypes             # Data types list
df.columns            # Column names
df.count()            # Row count
df.rdd.getNumPartitions()  # Partition count
```

### Shape Operations
```python
len(df.columns)       # Number of columns
df.count()            # Number of rows
df.describe().show()  # Statistics
```

---

## Selection & Filtering

### Column Selection
```python
df.select("name")                    # Single column
df.select("name", "age")             # Multiple columns
df.select(df.name, df.age)           # Using column objects
df.select(["name", "age"])           # List of columns
df.select("*")                       # All columns
df[["name", "age"]]                  # Alternative syntax
```

### Filtering
```python
df.filter(df.age > 30)                      # Simple filter
df.filter((df.age > 30) & (df.salary > 50000))  # AND
df.filter((df.age > 30) | (df.salary > 50000))  # OR
df.filter(~(df.age > 30))                   # NOT
df.filter(df.name == "Alice")               # Equality
df.filter(df.name.isin(["Alice", "Bob"]))   # IN
df.filter(df.name.like("A%"))               # LIKE
df.where(df.age > 30)                       # Alias for filter
```

### Distinct & Drop Duplicates
```python
df.distinct()                # Remove all duplicates
df.dropDuplicates()          # Same as distinct
df.dropDuplicates(["name"])  # Duplicates in name column
```

---

## Transformations

### Adding/Modifying Columns
```python
# Add new column
df.withColumn("salary_doubled", df.salary * 2)

# Rename column
df.withColumnRenamed("age", "person_age")

# Drop column
df.drop("age")
df.drop("age", "salary")  # Multiple columns

# Type casting
df.withColumn("age", df.age.cast("int"))
```

### String Operations
```python
from pyspark.sql.functions import col, upper, lower, trim, length

df.withColumn("name_upper", upper(col("name")))
df.withColumn("name_lower", lower(col("name")))
df.withColumn("name_clean", trim(col("name")))
df.withColumn("name_length", length(col("name")))
```

### Conditional Logic
```python
from pyspark.sql.functions import when

df.withColumn(
    "age_group",
    when(col("age") < 30, "Young")
    .when(col("age") < 60, "Middle")
    .otherwise("Senior")
)
```

---

## Aggregations

### Basic Aggregations
```python
from pyspark.sql.functions import count, sum, avg, min, max, stddev

df.agg(count("*"))           # Count rows
df.agg(sum("salary"))        # Sum column
df.agg(avg("salary"))        # Average
df.agg(min("salary"))        # Minimum
df.agg(max("salary"))        # Maximum
df.agg(stddev("salary"))     # Standard deviation

# Multiple aggregations
df.agg(
    count("*").alias("count"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("max_salary")
)
```

### GroupBy
```python
df.groupBy("department").agg(
    count("*").alias("count"),
    avg("salary").alias("avg_salary")
)

df.groupBy("department", "role").count()
df.groupBy("department").agg(sum("salary"))
```

### Window Functions
```python
from pyspark.sql.functions import row_number, rank, dense_rank
from pyspark.sql.window import Window

window = Window.partitionBy("department").orderBy("salary")
df.withColumn("row_num", row_number().over(window))
df.withColumn("rank", rank().over(window))
df.withColumn("dense_rank", dense_rank().over(window))
```

---

## Joins

### Join Types
```python
df1.join(df2, df1.id == df2.id)           # Inner join (default)
df1.join(df2, df1.id == df2.id, "left")   # Left join
df1.join(df2, df1.id == df2.id, "right")  # Right join
df1.join(df2, df1.id == df2.id, "outer")  # Full outer join
df1.join(df2, df1.id == df2.id, "cross")  # Cross join
```

### Join on Multiple Columns
```python
df1.join(
    df2,
    (df1.id == df2.id) & (df1.date == df2.date),
    "inner"
)
```

### Broadcast Join (for small tables)
```python
from pyspark.sql.functions import broadcast

df1.join(broadcast(df2), df1.id == df2.id)
```

---

## Sorting & Ordering

```python
df.sort("age")                           # Ascending
df.sort(col("age").desc())               # Descending
df.orderBy("age", "name")                # Multiple columns
df.orderBy(col("age").desc(), col("name"))  # Mixed order
df.sort("age").limit(10)                 # Top 10
```

---

## Writing Data

### Basic Write
```python
df.write.csv("output/path", header=True)         # CSV
df.write.json("output/path")                     # JSON
df.write.parquet("output/path")                  # Parquet
df.write.mode("overwrite").csv("output/path")    # Overwrite
df.write.mode("append").csv("output/path")       # Append
```

### Write Modes
```python
# error: Throw error if path exists
# append: Append new data
# overwrite: Overwrite existing path
# ignore: Ignore if path exists

df.write.mode("overwrite").csv("path")
```

---

## Common Functions

```python
from pyspark.sql.functions import *

# Math
abs(col)              # Absolute value
round(col, 2)         # Round to 2 decimals
sqrt(col)             # Square root
exp(col), log(col)    # Exponential and log

# String
concat(col1, col2)    # Concatenate strings
substring(col, 1, 5)  # Substring
replace(col, "a", "b")  # Replace

# Date/Time
current_timestamp()   # Current timestamp
dayofmonth(col)      # Day of month
month(col)           # Month
year(col)            # Year
dateadd(col, 1)      # Add days

# Null handling
isnull(col)          # Check null
coalesce(col1, col2) # Return first non-null
fillna(value)        # Fill null values
```

---

## Performance Tips

### Caching
```python
df.cache()           # Cache in memory
df.persist()         # Persist (same as cache)
df.unpersist()       # Remove from cache
```

### Partitioning
```python
df.repartition(100)           # Change partition count
df.coalesce(10)               # Reduce partitions
df.partitionBy("year").write.parquet("path")  # Partition on write
```

### Broadcast
```python
from pyspark.sql.functions import broadcast
df.join(broadcast(small_df), "key")  # Use for small tables
```

---

## Spark SQL

```python
df.createOrReplaceTempView("table_name")      # Temporary view
df.createOrReplaceGlobalTempView("table")    # Global view

# Run SQL queries
result = spark.sql("""
    SELECT name, age FROM table_name
    WHERE age > 30
    ORDER BY age DESC
""")
```

---

## RDD Operations

```python
rdd = df.rdd                    # Convert to RDD
rdd.map(lambda x: x * 2)       # Map transformation
rdd.filter(lambda x: x > 10)   # Filter
rdd.collect()                  # Collect to driver
rdd.count()                    # Count elements
rdd.first()                    # First element
rdd.take(10)                   # First 10 elements
```

---

## Debugging & Testing

```python
# Print schema
df.printSchema()

# Explain query plan
df.explain()
df.explain(extended=True)  # Extended plan

# Sample data
df.sample(0.1).show()      # 10% sample

# Test on subset
df.limit(100).show()       # First 100 rows

# Count null values
from pyspark.sql.functions import sum as spark_sum, when
df.select([spark_sum(when(isnull(c), 1)).alias(c) for c in df.columns]).show()
```

---

## Quick Reference Summary

| Task | Command |
|------|----------|
| Create session | `SparkSession.builder.appName(\"app\").getOrCreate()` |
| Read CSV | `spark.read.csv(\"file.csv\", header=True)` |
| Show data | `df.show()` |
| Filter | `df.filter(df.age > 30)` |
| Select | `df.select(\"name\", \"age\")` |
| GroupBy | `df.groupBy(\"dept\").agg(count(\"*\"))` |
| Join | `df1.join(df2, df1.id == df2.id)` |
| Write | `df.write.csv(\"output/\")` |
| Cache | `df.cache()` |
| SQL | `spark.sql(\"SELECT * FROM table\")` |
