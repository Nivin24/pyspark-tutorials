# Spark Structured Streaming - Monitoring and Debugging
# Understanding streaming query metrics and monitoring

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, sum, count
import time

spark = SparkSession.builder.appName("MonitoringDebugging").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("Monitoring and Debugging Tutorial")
print("="*60)

# Create a streaming DataFrame
df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 10) \
    .load()

# Create a simple transformation
agg_df = df.select(
    (col("value") % 5).alias("category"),
    col("value").alias("amount")
).groupBy("category").agg(
    count("*").alias("count"),
    sum("amount").alias("total")
)

# Example 1: Starting a query and monitoring
print("\nExample 1: Starting and Monitoring a Query")
print("-"*60)

query = agg_df.writeStream \
    .format("console") \
    .outputMode("update") \
    .option("truncate", False) \
    .option("numRows", 5) \
    .start()

print(f"Query ID: {query.id}")
print(f"Query Name: {query.name}")
print(f"Is Active: {query.isActive}")

time.sleep(1)

# Example 2: Accessing query status
print("\nExample 2: Accessing Query Status")
print("-"*60)

status = query.status
print(f"Current Timestamp: {status.timestamp}")
print(f"Message: {status.message}")
print(f"Is Data Available: {status.isDataAvailable}")

# Example 3: Recent Progress
print("\nExample 3: Recent Progress Information")
print("-"*60)

if query.recentProgress:
    recent = query.recentProgress[-1]
    print(f"Batch ID: {recent.batchId}")
    print(f"Input Rows: {recent.numInputRows}")
    print(f"Output Rows: {recent.numOutputRows}")
    if recent.durationMs:
        print(f"Batch Duration: {recent.durationMs.get('total', 0)} ms")
else:
    print("No recent progress yet")

# Example 4: Error Handling
print("\nExample 4: Error Handling and Debugging")
print("-"*60)

try:
    print("Query Status: Running")
    print("Check logs for detailed error information")
    print("Monitor input rate and processing rate")
except Exception as e:
    print(f"Error occurred: {str(e)}")

query.stop()

print("\n" + "="*60)
print("Monitoring and Debugging Tutorial Completed")
print("="*60)
