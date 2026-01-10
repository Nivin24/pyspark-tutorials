"""
Spark Session Setup and Configuration
=====================================
This tutorial covers:
- Creating a Spark Session
- Configuring Spark properties
- Using different cluster managers
- Managing Spark Context
"""

from pyspark.sql import SparkSession

# Basic Spark Session creation
spark = SparkSession.builder.appName("SessionSetup").getOrCreate()

# Spark Session with advanced configuration
spark2 = SparkSession.builder \
    .appName("AdvancedConfiguration") \
    .config("spark.executor.memory", "2g") \
    .config("spark.executor.cores", "2") \
    .config("spark.driver.memory", "1g") \
    .getOrCreate()

# Access configuration
print("Spark Configuration:")
for key, value in spark.sparkContext.getConf().getAll():
    print(f"{key}: {value}")

# Get Spark version
print(f"\nSpark Version: {spark.version}")

# Stop the session
spark.stop()
spark2.stop()
