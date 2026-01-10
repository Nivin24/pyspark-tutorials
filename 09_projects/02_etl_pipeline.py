# ETL Pipeline - Complete End-to-End Data Processing
# Extract, Transform, Load pattern with real-world data

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when, split, upper, trim
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from datetime import datetime

spark = SparkSession.builder.appName("ETLPipeline").getOrCreate()

print("\n" + "=" * 60)
print("ETL PIPELINE - DATA PROCESSING WORKFLOW")
print("=" * 60)

# PHASE 1: EXTRACT
print("\nPHASE 1: EXTRACTING DATA FROM SOURCES")
print("-" * 60)

# Simulate data from multiple sources
customer_data = [
    (1, "John Doe", "john@email.com", "New York", "10001"),
    (2, "Jane Smith", "jane@email.com", "Los Angeles", "90001"),
    (3, "Bob Johnson", "bob@email.com", "Chicago", "60601"),
    (4, "Alice Brown", None, "Houston", "77001"),  # Missing email
]

order_data = [
    (101, 1, 150.00, "2024-01-15"),
    (102, 2, 200.00, "2024-01-16"),
    (103, 1, 75.50, "2024-01-17"),
    (104, 3, 300.00, "2024-01-18"),
    (105, 4, None, "2024-01-19"),  # Missing amount
]

product_data = [
    ("P001", "Laptop", 1000.00, "Electronics"),
    ("P002", "Mouse", 25.00, "Electronics"),
    ("P003", "Desk", 300.00, "Furniture"),
    ("P004", "Chair", 150.00, "Furniture"),
]

# Create DataFrames
customers_df = spark.createDataFrame(customer_data, ["customer_id", "name", "email", "city", "zip"])
orders_df = spark.createDataFrame(order_data, ["order_id", "customer_id", "amount", "date"])
products_df = spark.createDataFrame(product_data, ["product_id", "product_name", "price", "category"])

print(f"Extracted Customers: {customers_df.count()} records")
print(f"Extracted Orders: {orders_df.count()} records")
print(f"Extracted Products: {products_df.count()} records")

# PHASE 2: TRANSFORM
print("\nPHASE 2: TRANSFORMING DATA")
print("-" * 60)

# Data Cleaning
print("\nStep 1: Data Cleaning")
customers_clean = customers_df.dropna(subset=["email"])
orders_clean = orders_df.dropna(subset=["amount"])
print(f"Customers after removing nulls: {customers_clean.count()}")
print(f"Orders after removing nulls: {orders_clean.count()}")

# Data Standardization
print("\nStep 2: Data Standardization")
customers_std = customers_clean.select(
    col("customer_id"),
    upper(trim(col("name"))).alias("name"),
    lower(col("email")).alias("email"),
    upper(col("city")).alias("city"),
    col("zip")
)
customers_std.show(2)

# Data Enrichment
print("\nStep 3: Data Enrichment")
orders_enriched = orders_clean.select(
    col("order_id"),
    col("customer_id"),
    col("amount"),
    to_timestamp(col("date")).alias("order_date"),
    when(col("amount") > 150, "High Value").otherwise("Regular").alias("order_category")
)
orders_enriched.show(3)

# Data Integration (Join)
print("\nStep 4: Data Integration (Joining tables)")
integrated_df = orders_enriched.join(
    customers_std,
    orders_enriched.customer_id == customers_std.customer_id,
    "inner"
).select(
    orders_enriched.order_id,
    customers_std.name,
    customers_std.email,
    customers_std.city,
    orders_enriched.amount,
    orders_enriched.order_date,
    orders_enriched.order_category
)
integrated_df.show(3)

# PHASE 3: VALIDATE
print("\nPHASE 3: VALIDATING DATA QUALITY")
print("-" * 60)

print(f"Total records after integration: {integrated_df.count()}")
print(f"Records with null values: {integrated_df.select([col(c).isNull() for c in integrated_df.columns]).rdd.map(lambda row: sum(row)).sum()}")
print(f"Amount statistics:")
integrated_df.select("amount").describe().show()

# PHASE 4: LOAD
print("\nPHASE 4: LOADING RESULTS")
print("-" * 60)

# Write to different formats
print("\nWriting to Parquet format...")
integrated_df.write.mode("overwrite").parquet("/tmp/pyspark_etl_output/parquet")
print("✓ Parquet output saved")

print("\nWriting to CSV format...")
integrated_df.coalesce(1).write.mode("overwrite").option("header", "true").csv("/tmp/pyspark_etl_output/csv")
print("✓ CSV output saved")

print("\nWriting summary statistics...")
summary_df = integrated_df.groupBy("city").agg({
    "amount": "sum",
    "order_id": "count"
}).withColumnRenamed("sum(amount)", "total_amount").withColumnRenamed("count(order_id)", "order_count")
summary_df.show()

print("\n" + "=" * 60)
print("ETL PIPELINE COMPLETED SUCCESSFULLY!")
print(f"Total records processed: {integrated_df.count()}")
print("=" * 60)
