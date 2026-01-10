# Handling Missing Values in PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean, when, isnan, isnull, coalesce, lead, lag
from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Initialize Spark Session
spark = SparkSession.builder.appName("MissingValues").getOrCreate()

# Create sample data with missing values
data = [
    ("Alice", 25, 50000.0, "Engineering"),
    ("Bob", None, 60000.0, "Sales"),
    ("Charlie", 35, None, "Engineering"),
    ("Diana", 28, 55000.0, None),
    ("Eve", None, None, "Marketing"),
    ("Frank", 32, 70000.0, "Engineering"),
]

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True),
    StructField("department", StringType(), True),
])

df = spark.createDataFrame(data, schema=schema)

print("\n=== Original DataFrame with Missing Values ===")
df.show()

# 1. Count missing values
print("\n=== Count Missing Values ===")
from pyspark.sql.functions import countDistinct
for column in df.columns:
    missing_count = df.filter(col(column).isNull()).count()
    print(f"{column}: {missing_count} null values")

# 2. Drop rows with ANY null values
print("\n=== After Dropping Rows with Any Null Values ===")
df_dropna = df.dropna()
df_dropna.show()

# 3. Drop rows with null in specific columns
print("\n=== After Dropping Rows with Null in Specific Columns ===")
df_drop_specific = df.dropna(subset=["age", "salary"])
df_drop_specific.show()

# 4. Fill missing values with a constant
print("\n=== Fill Missing Values with Constants ===")
df_filled_const = df.fillna({
    "age": 0,
    "salary": 0.0,
    "department": "Unknown"
})
df_filled_const.show()

# 5. Fill missing values with column mean
print("\n=== Fill Missing Values with Column Mean ===")
# Calculate mean age and salary
mean_age = df.select(mean(col("age"))).collect()[0][0]
mean_salary = df.select(mean(col("salary"))).collect()[0][0]

print(f"Mean Age: {mean_age}")
print(f"Mean Salary: {mean_salary}")

df_filled_mean = df.fillna({
    "age": int(mean_age) if mean_age else 0,
    "salary": mean_salary if mean_salary else 0.0
})
df_filled_mean.show()

# 6. Forward Fill (Last Observation Carried Forward)
print("\n=== Forward Fill (LOCF) ===")
window_spec = Window.orderBy("name").rowsBetween(Window.unboundedPreceding, 0)
df_forward = df.withColumn(
    "age_filled",
    coalesce(
        col("age"),
        lead(col("age"), 1).over(window_spec)
    )
)
df_forward.show()

# 7. Fill with different strategies per column
print("\n=== Mixed Fill Strategy ===")
df_mixed = (df
    .fillna({"age": 30, "department": "Not Assigned"})  # Fill with constants
    .filter(col("salary").isNotNull())  # Drop rows where salary is null
)
df_mixed.show()

# 8. Replace specific values
print("\n=== Replace Specific Values ===")
df_replaced = df.replace({"Unknown": "Not Specified", "Sales": "Sales Team"})
df_replaced.show()

print("\n=== Summary ===")
print("Missing value handling strategies:")
print("1. Drop rows with missing values")
print("2. Fill with constants")
print("3. Fill with statistical measures (mean, median)")
print("4. Forward fill (LOCF)")
print("5. Mixed strategies for different columns")
print("6. Replace specific values")
