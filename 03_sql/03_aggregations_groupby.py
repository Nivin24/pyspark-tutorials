"""SQL Aggregations and GROUP BY

Covers: COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Aggregations").getOrCreate()

# Sales data
sales_data = [("Sales", 10000), ("Engineering", 5000), ("Sales", 12000), ("Engineering", 8000)]
df = spark.createDataFrame(sales_data, ["dept", "amount"])
df.createOrReplaceTempView("sales")

print("\n=== COUNT ===")
spark.sql("SELECT COUNT(*) as total FROM sales").show()

print("\n=== SUM ===")
spark.sql("SELECT SUM(amount) as total_amount FROM sales").show()

print("\n=== GROUP BY ===")
spark.sql("""
  SELECT dept, COUNT(*) as count, SUM(amount) as total
  FROM sales GROUP BY dept
""").show()

print("\n=== HAVING ===")
spark.sql("""
  SELECT dept, SUM(amount) as total
  FROM sales GROUP BY dept
  HAVING SUM(amount) > 10000
""").show()
