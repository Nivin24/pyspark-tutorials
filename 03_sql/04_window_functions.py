"""Window Functions - ROW_NUMBER, RANK, LEAD, LAG, Running Totals"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Window").getOrCreate()

data = [("Alice", "Sales", 5000), ("Bob", "Sales", 6000), ("Charlie", "Eng", 7000)]
df = spark.createDataFrame(data, ["name", "dept", "salary"])
df.createOrReplaceTempView("emp")

print("\n=== ROW_NUMBER ===")
spark.sql("SELECT name, salary, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) as rank FROM emp").show()

print("\n=== LEAD ===")
spark.sql("SELECT name, salary, LEAD(salary) OVER (ORDER BY salary) as next_sal FROM emp").show()

print("\n=== LAG ===")
spark.sql("SELECT name, salary, LAG(salary) OVER (ORDER BY salary) as prev_sal FROM emp").show()

print("\n=== Running Total ===")
spark.sql("SELECT name, salary, SUM(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total FROM emp").show()
