# Spark Structured Streaming - Stateful Operations
# Maintaining and updating state across micro-batches

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, max as max_func
from pyspark.sql.types import StructType, StructField, StringType, LongType

spark = SparkSession.builder.appName("StatefulStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("Stateful Operations Tutorial")
print("="*60)

# Create a rate source
df = spark.readStream.format("rate").option("rowsPerSecond", 10).load()

# Example 1: Aggregation (implicitly stateful)
print("\nExample 1: Aggregation (Stateful - maintains running totals)")
print("-"*60)

df_with_key = df.select(
    (col("value") % 3).cast("string").alias("key"),
    col("value").alias("amount")
)

agg_query = df_with_key.groupBy("key").agg(
    count("*").alias("total_count"),
    sum("amount").alias("sum_amount")
)

print("Aggregation query schema:")
agg_query.printSchema()
print("State being maintained: Count and sum per key")

# Example 2: Streaming aggregation with output
print("\nExample 2: Console Output - Update Mode")
print("-"*60)
query_update = agg_query.writeStream \
    .format("console") \
    .outputMode("update") \
    .option("truncate", False) \
    .start()

import time
time.sleep(2)
query_update.stop()

# Example 3: Stateless vs Stateful
print("\nExample 3: Understanding Stateless Operations")
print("-"*60)
stateless = df.select(
    col("value"),
    (col("value") * 2).alias("doubled"),
    (col("value") % 2).alias("remainder")
)
print("Stateless operations: select, filter, map transformations")
print("No state maintained across batches")

# Example 4: State cleanup with TTL
print("\nExample 4: State Management Best Practices")
print("-"*60)
print("State Retention Considerations:")
print("1. Use TTL (Time-To-Live) for state cleanup")
print("2. Monitor state size")
print("3. Use appropriate aggregation keys")
print("4. Consider memory limitations")
print("5. Enable checkpointing for state persistence")

print("\n" + "="*60)
print("Stateful Operations Tutorial Completed")
print("="*60)
