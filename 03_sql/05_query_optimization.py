"""Query Optimization with EXPLAIN and Broadcast"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Optimization").getOrCreate()

data = [("Alice", "Sales", 5000), ("Bob", "Eng", 6000)]
df = spark.createDataFrame(data, ["name", "dept", "salary"])
df.createOrReplaceTempView("emp")

print("\n=== EXPLAIN Query ===")
spark.sql("EXPLAIN SELECT name FROM emp WHERE salary > 5000").show()

print("\n=== EXPLAIN FORMATTED ===")
spark.sql("EXPLAIN FORMATTED SELECT * FROM emp WHERE dept = 'Sales'").show()

print("\n=== Broadcast Join ===")
df2 = spark.createDataFrame([("Sales", "NYC")], ["dept", "loc"])
df2.createOrReplaceTempView("locs")
spark.sql("SELECT /*+ BROADCAST(locs) */ e.name FROM emp e JOIN locs l ON e.dept = l.dept").show()
