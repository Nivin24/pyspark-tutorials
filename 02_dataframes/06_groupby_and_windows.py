"""GroupBy and Window Functions in PySpark

This tutorial covers:
- Group by with single and multiple columns
- Window functions for ranking
- Row number, rank, dense rank
- Lead and lag functions
- Running total and cumulative aggregations
- Partitioning with window functions
"""

from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import row_number, rank, dense_rank, lead, lag, sum as spark_sum, col

# Initialize Spark Session
spark = SparkSession.builder.appName("GroupBy and Windows").getOrCreate()

# Sample sales data with dates
sales_data = [
    ("Alice", "Sales", 1000, "2024-01-01"),
    ("Bob", "Sales", 1200, "2024-01-02"),
    ("Charlie", "Engineering", 500, "2024-01-01"),
    ("Alice", "Sales", 950, "2024-01-03"),
    ("Bob", "Sales", 1100, "2024-01-04"),
    ("Charlie", "Engineering", 600, "2024-01-03"),
    ("Alice", "Sales", 1050, "2024-01-05"),
    ("David", "Sales", 1300, "2024-01-02")
]

df = spark.createDataFrame(sales_data, ["Name", "Department", "Amount", "Date"])

print("\n=== Original DataFrame ===")
df.show()

print("\n=== Method 1: Simple GroupBy ===")
df.groupBy("Department").count().show()

print("\n=== Method 2: GroupBy with Aggregation ===")
df.groupBy("Department").agg({"Amount": "sum", "Name": "count"}).show()

print("\n=== Method 3: Multiple GroupBy Columns ===")
df.groupBy("Department", "Name").agg({"Amount": "sum"}).show()

print("\n=== Method 4: Row Number Window Function ===")
window_spec = Window.partitionBy("Department").orderBy(col("Amount").desc())
df.withColumn("row_num", row_number().over(window_spec)).show()

print("\n=== Method 5: Rank Window Function ===")
df.withColumn("rank", rank().over(window_spec)).show()

print("\n=== Method 6: Dense Rank Window Function ===")
df.withColumn("dense_rank", dense_rank().over(window_spec)).show()

print("\n=== Method 7: Lead Function ===")
window_by_name = Window.partitionBy("Name").orderBy("Date")
df.withColumn("next_amount", lead("Amount").over(window_by_name)).show()

print("\n=== Method 8: Lag Function ===")
df.withColumn("prev_amount", lag("Amount").over(window_by_name)).show()

print("\n=== Method 9: Running Total ===")
window_running = Window.partitionBy("Name").orderBy("Date").rangeBetween(Window.unboundedPreceding, 0)
df.withColumn("running_total", spark_sum("Amount").over(window_running)).show()

print("\n=== Method 10: Top 2 Per Department ===")
df.withColumn("rank", rank().over(window_spec)).filter(col("rank") <= 2).show()
