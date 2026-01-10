# Data Cleaning and Validation in PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, drop_duplicates, isnan, isnull
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Initialize Spark Session
spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

# Create sample data with issues
data = [
    ("Alice", 25, 50000.0),
    ("Bob", None, 60000.0),
    ("Alice", 25, 50000.0),  # Duplicate
    ("Charlie", 35, None),
    ("David", 28, 55000.0),
    ("Eve", -5, 65000.0),  # Invalid age
]

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True),
])

df = spark.createDataFrame(data, schema=schema)

print("\n=== Original DataFrame ===")
df.show()
print(f"Count: {df.count()}")

# 1. Handle Duplicates
print("\n=== After Removing Duplicates ===")
df_no_dup = df.dropDuplicates()
df_no_dup.show()

# 2. Handle Missing Values - Drop
print("\n=== After Dropping Rows with Null Values ===")
df_no_null = df.dropna()
df_no_null.show()

# 3. Handle Missing Values - Fill with Values
print("\n=== After Filling Null Values ===")
df_filled = df.fillna({"age": 0, "salary": 0.0})
df_filled.show()

# 4. Validate Data (remove negative ages)
print("\n=== After Data Validation ===")
df_valid = df.filter((col("age") > 0) | col("age").isNull())
df_valid.show()

# 5. Combine operations
print("\n=== Final Cleaned DataFrame ===")
df_cleaned = (df
    .dropDuplicates()
    .dropna(subset=["name"])
    .filter((col("age") > 0) | col("age").isNull())
    .fillna({"age": 30, "salary": 50000.0})
)
df_cleaned.show()
df_cleaned.printSchema()
