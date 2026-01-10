"""DataFrame Aggregations in PySpark

This tutorial covers:
- count(), sum(), avg(), min(), max()
- Multiple aggregations
- Aggregations with group by
- Named aggregations
- Window functions basics
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count, min, max, col

# Initialize Spark Session
spark = SparkSession.builder.appName("Aggregations").getOrCreate()

# Sample sales data
sales_data = [
    ("Electronics", "Laptop", 5, 1000),
    ("Electronics", "Phone", 10, 500),
    ("Furniture", "Chair", 8, 200),
    ("Electronics", "Tablet", 4, 300),
    ("Furniture", "Desk", 3, 600),
    ("Electronics", "Monitor", 7, 350),
    ("Furniture", "Shelf", 6, 150)
]

df = spark.createDataFrame(sales_data, ["Category", "Product", "Quantity", "Price"])
df = df.withColumn("Total", col("Quantity") * col("Price"))

print("\n=== Original DataFrame ===")
df.show()

print("\n=== Method 1: Count ===")
print(f"Total rows: {df.count()}")

print("\n=== Method 2: Sum ===")
df.agg({"Total": "sum"}).show()
df.agg(sum("Total")).show()

print("\n=== Method 3: Average ===")
df.agg(avg("Price")).show()

print("\n=== Method 4: Min and Max ===")
df.agg(min("Price"), max("Price")).show()

print("\n=== Method 5: Multiple Aggregations ===")
df.agg(
    count("Product"),
    sum("Total"),
    avg("Price"),
    min("Quantity"),
    max("Quantity")
).show()

print("\n=== Method 6: Group By Single Column ===")
df.groupBy("Category").agg(sum("Total")).show()

print("\n=== Method 7: Group By with Alias ===")
df.groupBy("Category").agg(sum("Total").alias("Total_Sales")).show()

print("\n=== Method 8: Multiple Group By Aggregations ===")
df.groupBy("Category").agg(
    count("Product").alias("Item_Count"),
    sum("Total").alias("Total_Revenue"),
    avg("Price").alias("Avg_Price")
).show()

print("\n=== Method 9: Order by Aggregation ===")
df.groupBy("Category").agg(sum("Total").alias("Total_Sales")).orderBy(col("Total_Sales").desc()).show()

print("\n=== Method 10: Using SQL ===")
df.createOrReplaceTempView("sales")
spark.sql("SELECT Category, COUNT(*) as Items, SUM(Total) as Revenue FROM sales GROUP BY Category").show()
