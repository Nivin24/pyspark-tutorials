# Spark Structured Streaming - Advanced Features
# Exploring advanced streaming patterns and features

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, window, from_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import json

spark = SparkSession.builder.appName("AdvancedStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

print("="*60)
print("Advanced Streaming Features Tutorial")
print("="*60)

# Example 1: Stream-to-Batch Join
print("\nExample 1: Stream-to-Static Table Join")
print("-"*60)

df = spark.readStream.format("rate").option("rowsPerSecond", 5).load()

# Create a static reference table
static_data = spark.range(0, 100, 1).selectExpr(
    "id as product_id",
    "cast(id * 10 as double) as price"
)

# Join stream with static table
joined = df.select(
    col("value").cast("long").alias("product_id"),
    col("timestamp")
).join(
    static_data,
    "product_id",
    "left"
)

print("Stream-to-Static join schema:")
joined.printSchema()

# Example 2: Stream-to-Stream Join (requires watermark)
print("\nExample 2: Stream-to-Stream Join Concepts")
print("-"*60)
print("Requirements for stream-stream joins:")
print("1. Both streams must have watermarks")
print("2. Time bounds must be specified")
print("3. Join condition must have time constraints")
print("Example:")
print("  stream1.join(stream2,")
print("    [stream1.key == stream2.key,")
print("     stream1.ts >= stream2.ts - interval(\"10 minutes\"),")
print("     stream1.ts <= stream2.ts + interval(\"5 minutes\")]")
print("  )")

# Example 3: Custom State Management
print("\nExample 3: Advanced State Patterns")
print("-"*60)
print("State management patterns:")
print("1. Aggregations - Built-in state handling")
print("2. flatMapGroupsWithState - Custom state function")
print("3. mapGroupsWithState - Deterministic state updates")
print("4. State TTL - Automatic state cleanup")

# Example 4: Output modes comparison
print("\nExample 4: Output Modes Comparison")
print("-"*60)
print("\nAppend Mode:")
print("- Only new rows written")
print("- Suitable for: Non-aggregated data, append-only operations")
print("- State: Not required")
print("\nUpdate Mode:")
print("- Only modified rows written")
print("- Suitable for: Aggregations, updated results")
print("- State: Required for aggregations")
print("\nComplete Mode:")
print("- Entire result table written")
print("- Suitable for: Interactive queries, small results")
print("- State: Full state maintained")

# Example 5: Performance tuning
print("\nExample 5: Performance Optimization Tips")
print("-"*60)
print("1. Trigger Configuration:")
print("   - processingTime: Batch interval tuning")
print("   - continuous: Low-latency processing")
print("   - once: Single batch execution")
print("\n2. Memory Management:")
print("   - State cleanup with TTL")
print("   - Proper partitioning")
print("   - Batch size optimization")
print("\n3. Checkpointing:")
print("   - Use fast storage (local SSD)")
print("   - Enable compression")
print("   - Monitor checkpoint size")

print("\n" + "="*60)
print("Advanced Features Tutorial Completed")
print("="*60)
