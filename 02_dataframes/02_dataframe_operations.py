"""DataFrame Operations in PySpark

This tutorial demonstrates common DataFrame operations including:
- Selecting and dropping columns
- Renaming columns
- Sorting and limiting
- Adding new columns
- Data types and schema inspection
- Distinct and unique values
"""

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("DataFrame Operations").getOrCreate()

# Sample employee data
employee_data = [
    ("Alice", 28, "Sales", 60000),
    ("Bob", 35, "Engineering", 95000),
    ("Charlie", 32, "Sales", 75000),
    ("David", 45, "Management", 110000),
    ("Eve", 29, "Engineering", 85000)
]

df = spark.createDataFrame(employee_data, ["Name", "Age", "Department", "Salary"])

print("\n=== Original DataFrame ===")
df.show()

print("\n=== Method 1: Select Specific Columns ===")
df.select("Name", "Salary").show()

print("\n=== Method 2: Select with Expression ===")
df.select("Name", "Age", (df.Salary * 1.1).alias("Salary_With_Bonus")).show()

print("\n=== Method 3: Drop Columns ===")
df.drop("Department").show()

print("\n=== Method 4: Rename Columns ===")
df.withColumnRenamed("Age", "Employee_Age").show()

print("\n=== Method 5: Add New Column ===")
df.withColumn("Annual_Bonus", df.Salary * 0.15).show()

print("\n=== Method 6: Sort by Salary ===")
df.orderBy(df.Salary.desc()).show()

print("\n=== Method 7: Limit Rows ===")
df.limit(3).show()

print("\n=== Method 8: Distinct Department ===")
df.select("Department").distinct().show()

print("\n=== Method 9: Filter and Select ===")
df.filter(df.Salary > 70000).select("Name", "Department", "Salary").show()

print("\n=== Method 10: Using SQL ===")
df.createOrReplaceTempView("employees")
spark.sql("SELECT Name, Salary FROM employees WHERE Salary > 80000 ORDER BY Salary DESC").show()

print("\n=== Schema Information ===")
df.printSchema()
print(f"Number of rows: {df.count()}")
print(f"Number of columns: {len(df.columns)}")
print(f"Column names: {df.columns}")
print(f"Data types: {df.dtypes}")
