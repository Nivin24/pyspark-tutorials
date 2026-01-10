"""
RDD (Resilient Distributed Dataset) Basics
==========================================
This tutorial covers:
- Creating RDDs
- RDD transformations
- RDD actions
- Persistence and caching
"""

from pyspark import SparkContext

# Create Spark Context
sc = SparkContext("local", "RDD Basics")

# Create RDD from a collection
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

print("Original RDD:", rdd.collect())

# Transformation: map
rdd_mapped = rdd.map(lambda x: x * 2)
print("After map (x*2):", rdd_mapped.collect())

# Transformation: filter
rdd_filtered = rdd.filter(lambda x: x > 2)
print("After filter (x>2):", rdd_filtered.collect())

# Action: count
print(f"Count: {rdd.count()}")

# Action: first
print(f"First element: {rdd.first()}")

# Action: take
print(f"First 3 elements: {rdd.take(3)}")

# Caching
rdd_cached = rdd.cache()
rdd_cached.count()  # This triggers evaluation and caches
print(f"Cached RDD: {rdd_cached.collect()}")

sc.stop()
