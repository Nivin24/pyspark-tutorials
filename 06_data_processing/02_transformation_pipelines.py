# Data Transformation Pipelines in PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit, split, explode, array_contains
from pyspark.sql.functions import lower, upper, trim, substring, length
from pyspark.sql.functions import when, case

# Initialize Spark Session
spark = SparkSession.builder.appName("DataTransformation").getOrCreate()

# Create sample data
data = [
    ("Alice Johnson", "alice.johnson@email.com", "Engineering", 25),
    ("Bob Smith", "bob.smith@email.com", "Sales", 30),
    ("Charlie Brown", "charlie.brown@email.com", "Marketing", 28),
    ("David Lee", "david.lee@email.com", "Engineering", 32),
]

df = spark.createDataFrame(data, ["name", "email", "department", "age"])

print("\n=== Original DataFrame ===")
df.show(truncate=False)

# 1. String transformations
print("\n=== String Transformations ===")
df_strings = df.select(
    col("name"),
    lower(col("email")).alias("email_lower"),
    upper(col("department")).alias("dept_upper"),
    length(col("name")).alias("name_length")
)
df_strings.show()

# 2. Column extraction
print("\n=== Column Extraction ===")
df_extracted = df.select(
    col("name"),
    split(col("name"), " ").getItem(0).alias("first_name"),
    split(col("name"), " ").getItem(1).alias("last_name"),
    substring(col("email"), 1, 5).alias("email_prefix")
)
df_extracted.show()

# 3. Conditional transformations
print("\n=== Conditional Transformations ===")
df_conditional = df.select(
    col("name"),
    col("age"),
    col("department"),
    when(col("age") < 30, "Junior")
        .when(col("age") < 35, "Mid-Level")
        .otherwise("Senior")
        .alias("experience_level")
)
df_conditional.show()

# 4. Data enrichment
print("\n=== Data Enrichment ===")
df_enriched = df.select(
    col("name"),
    col("email"),
    col("department"),
    col("age"),
    when(col("department") == "Engineering", 150000)
        .when(col("department") == "Sales", 100000)
        .when(col("department") == "Marketing", 90000)
        .otherwise(80000)
        .alias("estimated_salary")
)
df_enriched.show()

# 5. Combining transformations in pipeline
print("\n=== Full Transformation Pipeline ===")
df_pipeline = (df
    .select(
        split(col("name"), " ").getItem(0).alias("first_name"),
        split(col("name"), " ").getItem(1).alias("last_name"),
        lower(col("email")).alias("email"),
        col("department"),
        col("age")
    )
    .withColumn(
        "salary_band",
        when(col("age") < 30, "Entry-Level")
            .when(col("age") < 35, "Mid-Level")
            .otherwise("Senior")
    )
    .filter(col("department").isin(["Engineering", "Sales"]))
)
df_pipeline.show()
