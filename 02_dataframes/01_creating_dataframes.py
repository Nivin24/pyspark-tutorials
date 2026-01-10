"""
Creating DataFrames in PySpark
=============================
This tutorial covers:
- Creating DataFrames from various sources
- Schema definition (explicit and inferred)
- Different DataFrame creation methods
- Working with complex data types
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType

# Initialize Spark Session
spark = SparkSession.builder.appName("CreatingDataFrames").getOrCreate()

print("\n=== Method 1: From List of Tuples ===")
employee_data = [
    (1, "Alice", 25, 50000.0),
    (2, "Bob", 30, 60000.0),
    (3, "Charlie", 35, 75000.0),
    (4, "David", 28, 55000.0)
]
columns = ["EmpID", "Name", "Age", "Salary"]
df1 = spark.createDataFrame(employee_data, columns)
df1.show()
df1.printSchema()

print("\n=== Method 2: From List of Dictionaries ===")
employee_dicts = [
    {"EmpID": 5, "Name": "Emma", "Age": 26, "Salary": 52000.0},
    {"EmpID": 6, "Name": "Frank", "Age": 32, "Salary": 65000.0},
    {"EmpID": 7, "Name": "Grace", "Age": 29, "Salary": 58000.0}
]
df2 = spark.createDataFrame(employee_dicts)
df2.show()
df2.printSchema()

print("\n=== Method 3: With Explicit Schema ===")
schema = StructType([
    StructField("EmpID", IntegerType(), False),
    StructField("Name", StringType(), False),
    StructField("Age", IntegerType(), True),
    StructField("Salary", DoubleType(), True)
])
df3 = spark.createDataFrame(employee_data, schema)
df3.show()
df3.printSchema()

print("\n=== Method 4: Schema Inference ===")
# DataFrame automatically infers schema
df4 = spark.createDataFrame(employee_dicts)
print(f"Inferred Schema:")
df4.printSchema()

print("\n=== Method 5: From RDD ===")
rdd = spark.sparkContext.parallelize([("Alice", 25), ("Bob", 30)])
df_from_rdd = rdd.map(lambda x: (x[0], x[1])).toDF(["Name", "Age"])
df_from_rdd.show()

print("\n=== DataFrame Info ===")
print(f"Number of rows: {df1.count()}")
print(f"Number of columns: {len(df1.columns)}")
print(f"Column names: {df1.columns}")
print(f"Data types: {df1.dtypes}")

print("\n=== View DataFrame Content ===")
df1.show(truncate=False)
df1.head(2)
df1.take(1)

print("\n=== DataFrame Info Method ===")
df1.info()
df1.describe().show()

spark.stop()
