# Spark Structured Streaming - Basics Tutorial
# Learning basic concepts of Spark Structured Streaming

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

# Create Spark session
spark = SparkSession.builder \
    .appName("StreamingBasics") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("=" * 60)
print("Example 1: Basic Streaming from Rate Source")
print("=" * 60)

# Example 1: Create a simple streaming DataFrame from the rate source
df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 5) \
    .load()

print("\nStreaming DataFrame schema:")
df.printSchema()
print(f"\nIs streaming: {df.isStreaming}")

# Example 2: Basic transformation - select and rename columns
print("\n" + "=" * 60)
print("Example 2: Basic Transformations")
print("=" * 60)

result = df.select(
    col("timestamp").alias("event_time"),
    col("value").alias("record_id")
)

print("\nTransformed schema:")
result.printSchema()

# Example 3: Filtering
print("\n" + "=" * 60)
print("Example 3: Filtering")
print("=" * 60)

filtered = df.filter(col("value") % 2 == 0)
print("\nFilter applied: value % 2 == 0")

# Example 4: Writing to console
print("\n" + "=" * 60)
print("Example 4: Streaming to Console")
print("=" * 60)

query = filtered.writeStream \
    .format("console") \
    .option("truncate", "False") \
    .option("numRows", 10) \
    .start()

print(f"\nQuery ID: {query.id}")
print(f"Query name: {query.name}")
print(f"Is active: {query.isActive}")

time.sleep(2)
query.stop()

print("\n" + "=" * 60)
print("Streaming Basics Tutorial Completed")
print("=" * 60)
