# Feature Engineering in PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit, coalesce, log, sqrt, pow
from pyspark.sql.functions import year, month, dayofmonth, datediff, to_date
from pyspark.ml.feature import StandardScaler, VectorAssembler, OneHotEncoder, StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.linalg import Vectors

# Initialize Spark Session
spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()

# Create sample data
data = [
    ("Alice", "Engineering", 60000, "2023-01-15", 3.5),
    ("Bob", "Sales", 45000, "2023-03-20", 2.8),
    ("Charlie", "Engineering", 70000, "2023-02-10", 4.1),
    ("Diana", "Marketing", 50000, "2023-04-05", 3.0),
]

df = spark.createDataFrame(data, ["name", "department", "salary", "join_date", "rating"])

print("\n=== Original DataFrame ===")
df.show()

# 1. Numerical Feature Engineering
print("\n=== Numerical Feature Engineering ===")
df_numeric = df.select(
    col("name"),
    col("salary"),
    # Transformations
    log(col("salary")).alias("salary_log"),
    sqrt(col("salary")).alias("salary_sqrt"),
    pow(col("rating"), 2).alias("rating_squared"),
    # Scaling (min-max)
    ((col("salary") - 45000) / (70000 - 45000)).alias("salary_scaled")
)
df_numeric.show()

# 2. Categorical Feature Encoding
print("\n=== String Indexing (Categorical to Numeric) ===")
string_indexer = StringIndexer(inputCol="department", outputCol="department_index")
df_indexed = string_indexer.fit(df).transform(df)
df_indexed.select("department", "department_index").show()

# 3. One-Hot Encoding
print("\n=== One-Hot Encoding ===")
one_hot = OneHotEncoder(inputCol="department_index", outputCol="department_encoded")
df_encoded = one_hot.fit(df_indexed).transform(df_indexed)
df_encoded.select("department", "department_encoded").show(truncate=False)

# 4. Date Feature Engineering
print("\n=== Date Feature Engineering ===")
df_dates = df.select(
    col("name"),
    to_date(col("join_date")).alias("join_date_parsed"),
    year(to_date(col("join_date"))).alias("join_year"),
    month(to_date(col("join_date"))).alias("join_month"),
    # Days since joining (approx)
    datediff(lit("2024-01-01"), to_date(col("join_date"))).alias("days_employed")
)
df_dates.show()

# 5. Feature Binning
print("\n=== Feature Binning (Creating Buckets) ===")
df_binned = df.select(
    col("name"),
    col("salary"),
    when(col("salary") < 50000, "Low")
        .when(col("salary") < 65000, "Medium")
        .otherwise("High")
        .alias("salary_bucket")
)
df_binned.show()

# 6. Vector Assembler for ML
print("\n=== Feature Vector Assembly ===")
assembler = VectorAssembler(
    inputCols=["salary", "rating"],
    outputCol="features"
)
df_vectors = assembler.transform(df.select("name", "salary", "rating"))
df_vectors.select("name", "features").show()

# 7. Feature Scaling
print("\n=== Feature Scaling ===")
scaler = StandardScaler(inputCol="features", outputCol="scaled_features", withMean=True, withStd=True)
scaled_df = scaler.fit(df_vectors).transform(df_vectors)
scaled_df.select("name", "scaled_features").show(truncate=False)
