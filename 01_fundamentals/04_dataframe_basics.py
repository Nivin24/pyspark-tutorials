"""
DataFrame Basics in PySpark
===========================
This tutorial covers:
- Creating DataFrames from various sources
- Basic DataFrame operations
- Viewing and inspecting data
- Basic transformations
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Initialize Spark Session
spark = SparkSession.builder.appName("DataFrameBasics").getOrCreate()

# Method 1: Create DataFrame from list of tuples
print("\n=== Method 1: From list of tuples ===")
data_tuples = [
    ("Alice", 25, 50000.0),
    ("Bob", 30, 60000.0),
    ("Charlie", 35, 75000.0),
    ("David", 28, 55000.0)
]
columns = ["Name", "Age", "Salary"]
df1 = spark.createDataFrame(data_tuples, columns)
df1.show()

# Method 2: Create DataFrame from list of dictionaries
print("\n=== Method 2: From list of dictionaries ===")
data_dicts = [
    {"Name": "Emma", "Age": 26, "Salary": 52000.0},
    {"Name": "Frank", "Age": 32, "Salary": 65000.0},
    {"Name": "Grace", "Age": 29, "Salary": 58000.0}
]
df2 = spark.createDataFrame(data_dicts)
df2.show()

# Method 3: Create DataFrame with explicit schema
print("\n=== Method 3: With explicit schema ===")
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True),
    StructField("Salary", DoubleType(), True)
])
df3 = spark.createDataFrame(data_tuples, schema)
df3.show()

# DataFrame Info
print("\n=== DataFrame Schema ===")
df1.printSchema()

# Get DataFrame info
print("\n=== DataFrame Info ===")
print(f"Number of rows: {df1.count()}")
print(f"Number of columns: {len(df1.columns)}")
print(f"Column names: {df1.columns}")

# View specific rows
print("\n=== First 2 rows ===")
df1.show(2)

# Get specific column
print("\n=== Get 'Name' column ===")
df1.select("Name").show()

# Filter data
print("\n=== Employees with Age > 28 ===")
df1.filter(df1.Age > 28).show()

# Add a new column
print("\n=== Add new column (Bonus) ===")
df_with_bonus = df1.withColumn("Bonus", df1.Salary * 0.1)
df_with_bonus.show()

# Rename column
print("\n=== Rename 'Salary' to 'Annual_Salary' ===")
df_renamed = df1.withColumnRenamed("Salary", "Annual_Salary")
df_renamed.show()

# Drop a column
print("\n=== Drop 'Age' column ===")
df_no_age = df1.drop("Age")
df_no_age.show()

# Summary statistics
print("\n=== Summary Statistics ===")
df1.describe().show()

# Summary for specific columns
print("\n=== Summary for Age and Salary ===")
df1.describe("Age", "Salary").show()

print("\n=== DataFrame Basic Operations Completed ===")

# Stop Spark Session
spark.stop()
