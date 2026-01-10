# Spark Structured Streaming - Windowed Operations
# Understanding tumbling, sliding, and session windows

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, count, sum, avg
from pyspark.sql.types import StructType, StructField, TimestampType, DoubleType
import json
from datetime import datetime, timedelta

spark = SparkSession.builder.appName("StreamingWindows").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("Windowed Operations Tutorial")
print("="*60)

# Create a rate source with timestamp
df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 5) \
    .load()

# Example 1: Tumbling Window (Fixed-size, non-overlapping)
print("\nExample 1: Tumbling Window (10-second windows)")
print("-"*60)
windowed_tumbling = df.groupBy(
    window(col("timestamp"), "10 seconds")
).agg(
    count("*").alias("record_count"),
    avg("value").alias("avg_value")
).select(
    col("window").getField("start").alias("window_start"),
    col("window").getField("end").alias("window_end"),
    col("record_count"),
    col("avg_value")
)

print("Tumbling window schema:")
windowed_tumbling.printSchema()

# Example 2: Sliding Window (Overlapping windows)
print("\nExample 2: Sliding Window (10-sec window, 5-sec slide)")
print("-"*60)
windowed_sliding = df.groupBy(
    window(col("timestamp"), "10 seconds", "5 seconds")
).agg(
    count("*").alias("count"),
    sum("value").alias("total"),
    avg("value").alias("average")
)

print("Sliding window aggregation created")
print("Window size: 10 seconds, Slide: 5 seconds")

# Example 3: Window with Watermark
print("\nExample 3: Window with Watermark (Late Data Handling)")
print("-"*60)
watermarked = df.withWatermark("timestamp", "5 seconds") \
    .groupBy(
        window(col("timestamp"), "10 seconds")
    ).agg(
        count("*").alias("event_count"),
        avg("value").alias("avg_val")
    )

print("Watermark configuration:")
print("- Watermark delay: 5 seconds")
print("- Window duration: 10 seconds")
print("- Events arriving after watermark will be dropped in Append mode")

# Example 4: Console output
print("\nExample 4: Console Output of Windowed Data")
print("-"*60)
query = windowed_tumbling.writeStream \
    .format("console") \
    .outputMode("update") \
    .option("truncate", False) \
    .option("numRows", 10) \
    .start()

import time
time.sleep(2)
query.stop()

print("\n" + "="*60)
print("Windowed Operations Tutorial Completed")
print("="*60)
