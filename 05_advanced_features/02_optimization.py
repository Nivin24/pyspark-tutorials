# Query Optimization and Explain Plans
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Optimization").getOrCreate()
df = spark.range(100)

# Example 1: Check execution plan
print("=" * 50)
print("Execution Plan (Optimized):")
df.filter(df.id > 50).select("id").explain()

# Example 2: Extended plan
print("\nExtended Plan with Details:")
df.filter(df.id > 50).select("id").explain(extended=True)

print("Optimization tutorial completed")
