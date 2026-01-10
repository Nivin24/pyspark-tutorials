# Caching and Persistence Tutorial
from pyspark.sql import SparkSession
from pyspark.storage import StorageLevel

spark = SparkSession.builder.appName("Caching").getOrCreate()
df = spark.range(1000000).select("id")

# Example 1: Cache in memory
df.cache()
df.count()
print("Data cached in memory")

# Example 2: Persist with specific level
df.persist(StorageLevel.MEMORY_AND_DISK)
print("Data persisted with MEMORY_AND_DISK")

# Example 3: Unpersist to remove from cache
df.unpersist()
print("Data removed from cache")

# Example 4: Clear all caches
spark.catalog.clearCache()
print("All caches cleared")
