# Spark Structured Streaming - Sources and Sinks
# Understanding different data sources and output sinks

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType
import json
from datetime import datetime

spark = SparkSession.builder.appName("StreamingSourcesSinks").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("Streaming Sources and Sinks Tutorial")
print("="*60)

# Example 1: Rate Source
print("\nExample 1: Rate Source (Built-in Test Source)")
print("-"*60)
df_rate = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 2) \
    .option("rampUpTime", "1s") \
    .load()

print("Rate source schema:")
df_rate.printSchema()

# Example 2: Memory Sink (for testing)
print("\nExample 2: Memory Sink")
print("-"*60)
query_memory = df_rate.select(
    col("timestamp"),
    col("value")
).writeStream \
    .format("memory") \
    .queryName("streaming_memory") \
    .outputMode("append") \
    .start()

print(f"Query name: {query_memory.queryName}")
print(f"Query ID: {query_memory.id}")

# Example 3: Console Sink
print("\nExample 3: Console Sink")
print("-"*60)
query_console = df_rate.select(
    col("timestamp").cast("string").alias("event_time"),
    (col("value") * 10).alias("scaled_value")
).writeStream \
    .format("console") \
    .outputMode("append") \
    .option("truncate", False) \
    .option("numRows", 5) \
    .start()

import time
time.sleep(1)
query_console.stop()

# Example 4: Foreach Sink (custom processing)
print("\nExample 4: Foreach Sink (Custom Processing)")
print("-"*60)

def foreach_batch_function(df, epoch_id):
    print(f"\nBatch {epoch_id}:")
    df.show(n=3, truncate=False)

query_foreach = df_rate.select(
    col("timestamp"),
    col("value")
).writeStream \
    .foreachBatch(foreach_batch_function) \
    .outputMode("append") \
    .start()

time.sleep(1)
query_foreach.stop()

# Cleanup memory table if exists
try:
    spark.sql("DROP TABLE streaming_memory")
except:
    pass

print("\n" + "="*60)
print("Sources and Sinks Tutorial Completed")
print("="*60)
