# Partitioning and Shuffling Tutorial
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Partitioning").getOrCreate()
df = spark.range(100).select("id")

print("Original partitions:", df.rdd.getNumPartitions())

# Repartition - causes shuffle
df_repartitioned = df.repartition(4)
print("After repartition(4):", df_repartitioned.rdd.getNumPartitions())

# Coalesce - minimal shuffle
df_coalesced = df_repartitioned.coalesce(2)
print("After coalesce(2):", df_coalesced.rdd.getNumPartitions())

# Show partition distribution
df.withColumn("partition", df.id).show(10)
