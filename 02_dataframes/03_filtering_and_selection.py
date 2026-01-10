"""DataFrame Filtering and Selection in PySpark

This tutorial covers:
- Basic filtering with where() and filter()
- Filtering with SQL expressions
- Logical operators (AND, OR, NOT)
- Filtering with multiple conditions
- String operations for filtering
- Null value handling
- isin() and between() operations
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("Filtering and Selection").getOrCreate()

# Sample employee data
employee_data = [
    ("Alice", 28, "Sales", 60000, "NYC"),
    ("Bob", 35, "Engineering", 95000, "SF"),
    ("Charlie", 32, "Sales", 75000, "NYC"),
    ("David", 45, "Management", 110000, "LA"),
    ("Eve", 29, "Engineering", 85000, "SF"),
    ("Frank", 38, "Sales", 70000, "NYC"),
    ("Grace", 31, "Engineering", 90000, None)
]

df = spark.createDataFrame(employee_data, ["Name", "Age", "Department", "Salary", "Location"])

print("\n=== Original DataFrame ===")
df.show()

print("\n=== Method 1: Basic Filter (Salary > 80000) ===")
df.filter(df.Salary > 80000).show()

print("\n=== Method 2: Using where() instead of filter() ===")
df.where(df.Age > 30).show()

print("\n=== Method 3: String Expression ===")
df.filter("Salary > 75000").show()

print("\n=== Method 4: AND Condition ===")
df.filter((df.Salary > 70000) & (df.Age > 30)).show()

print("\n=== Method 5: OR Condition ===")
df.filter((df.Department == "Sales") | (df.Department == "Engineering")).show()

print("\n=== Method 6: NOT Condition ===")
df.filter(~(df.Department == "Sales")).show()

print("\n=== Method 7: isin() for Multiple Values ===")
df.filter(df.Location.isin(["NYC", "SF"])).show()

print("\n=== Method 8: between() for Range ===")
df.filter(df.Salary.between(70000, 90000)).show()

print("\n=== Method 9: Null Value Handling ===")
df.filter(df.Location.isNotNull()).show()

print("\n=== Method 10: Null Values ===")
df.filter(df.Location.isNull()).show()

print("\n=== Method 11: String Filtering - contains ===")
df.filter(df.Name.contains("a")).show()

print("\n=== Method 12: String Filtering - startswith ===")
df.filter(df.Name.startswith("A")).show()

print("\n=== Method 13: Using SQL Query ===")
df.createOrReplaceTempView("emp")
spark.sql("SELECT * FROM emp WHERE Salary > 80000 AND Age < 40").show()

print("\n=== Method 14: Complex Filter ===")
df.filter(
    ((df.Salary > 75000) & (df.Age > 30)) | 
    ((df.Department == "Engineering") & (df.Location == "SF"))
).show()
