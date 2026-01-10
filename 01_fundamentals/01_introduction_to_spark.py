"""
Introduction to Apache Spark
=============================
This tutorial covers:
- What is Spark?
- Spark ecosystem components
- Spark architecture (Driver, Executors, Cluster Manager)
- Key concepts: RDDs, DataFrames, Datasets
"""

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession \
    .builder \
    .appName("IntroductionToSpark") \
    .getOrCreate()

# Get Spark Context
sc = spark.sparkContext

print("=" * 50)
print("Spark Version:", spark.version)
print("Python Version:", sc.pythonVer)
print("=" * 50)

# Basic RDD creation
rdd = sc.parallelize([1, 2, 3, 4, 5])
print(f"RDD Sample: {rdd.collect()}")

# Basic DataFrame creation
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
print("\nDataFrame Sample:")
df.show()

# Stop the Spark Session
spark.stop()
