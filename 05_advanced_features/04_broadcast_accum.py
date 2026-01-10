# Broadcast Variables and Accumulators
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BroadcastAccum").getOrCreate()

# Broadcast variable
lookup_dict = {1: "A", 2: "B", 3: "C"}
broadcast_lookup = spark.broadcast(lookup_dict)

df = spark.range(1, 4).select("id")
df.show()

print("\nBroadcast value:", broadcast_lookup.value)

# Accumulator
acc = spark.sparkContext.accumulator(0)
sc = spark.sparkContext
sc.parallelize([1, 2, 3]).foreach(lambda x: acc.add(x))

print("\nAccumulator total:", acc.value)
