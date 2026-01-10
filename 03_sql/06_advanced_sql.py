"""Advanced SQL - UNION, INTERSECT, EXCEPT"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Advanced").getOrCreate()

data1 = [("Alice", "Sales"), ("Bob", "Eng")]
data2 = [("Bob", "Eng"), ("Charlie", "HR")]
df1 = spark.createDataFrame(data1, ["name", "dept"])
df2 = spark.createDataFrame(data2, ["name", "dept"])

df1.createOrReplaceTempView("emp1")
df2.createOrReplaceTempView("emp2")

print("\n=== UNION ===")
spark.sql("SELECT * FROM emp1 UNION SELECT * FROM emp2").show()

print("\n=== UNION ALL ===")
spark.sql("SELECT * FROM emp1 UNION ALL SELECT * FROM emp2").show()

print("\n=== INTERSECT ===")
spark.sql("SELECT * FROM emp1 INTERSECT SELECT * FROM emp2").show()

print("\n=== EXCEPT ===")
spark.sql("SELECT * FROM emp1 EXCEPT SELECT * FROM emp2").show()
