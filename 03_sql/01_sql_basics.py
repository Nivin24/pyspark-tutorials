"""Spark SQL Basics - Views and Simple Queries

This tutorial covers:
- Creating temporary and global views
- Basic SELECT statements
- WHERE clauses for filtering
- ORDER BY and LIMIT
- Simple aggregations
- Running SQL queries
"""

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("SQL Basics").getOrCreate()

# Sample employee data
employee_data = [
    (1, "Alice", "Sales", 60000),
    (2, "Bob", "Engineering", 95000),
    (3, "Charlie", "Sales", 75000),
    (4, "David", "Management", 110000),
    (5, "Eve", "Engineering", 85000),
    (6, "Frank", "Sales", 70000)
]

df = spark.createDataFrame(employee_data, ["emp_id", "name", "department", "salary"])

print("\n=== Original DataFrame ===")
df.show()

# Method 1: Create a temporary view
print("\n=== Creating Temporary View ===")
df.createOrReplaceTempView("employees")
print("Temporary view 'employees' created")

# Method 2: Create a global temporary view
print("\n=== Creating Global Temporary View ===")
df.createGlobalTempView("employees_global")
print("Global temporary view 'employees_global' created")

# Method 3: Basic SELECT query
print("\n=== Basic SELECT Query ===")
result = spark.sql("SELECT * FROM employees")
result.show()

# Method 4: SELECT specific columns
print("\n=== SELECT Specific Columns ===")
result = spark.sql("SELECT name, salary FROM employees")
result.show()

# Method 5: WHERE clause for filtering
print("\n=== WHERE Clause - Salary > 75000 ===")
result = spark.sql("SELECT * FROM employees WHERE salary > 75000")
result.show()

# Method 6: WHERE with text comparison
print("\n=== WHERE Clause - Department = 'Engineering' ===")
result = spark.sql("SELECT * FROM employees WHERE department = 'Engineering'")
result.show()

# Method 7: ORDER BY (ascending)
print("\n=== ORDER BY Salary (Ascending) ===")
result = spark.sql("SELECT * FROM employees ORDER BY salary")
result.show()

# Method 8: ORDER BY (descending)
print("\n=== ORDER BY Salary (Descending) ===")
result = spark.sql("SELECT * FROM employees ORDER BY salary DESC")
result.show()

# Method 9: LIMIT clause
print("\n=== LIMIT Top 3 Rows ===")
result = spark.sql("SELECT * FROM employees LIMIT 3")
result.show()

# Method 10: Combined WHERE, ORDER BY, LIMIT
print("\n=== Combined: WHERE + ORDER BY + LIMIT ===")
result = spark.sql("""
  SELECT name, salary
  FROM employees
  WHERE department IN ('Sales', 'Engineering')
  ORDER BY salary DESC
  LIMIT 3
""")
result.show()

# Method 11: COUNT aggregate
print("\n=== COUNT Query ===")
result = spark.sql("SELECT COUNT(*) as total_employees FROM employees")
result.show()

# Method 12: Simple aggregations
print("\n=== Multiple Aggregations ===")
result = spark.sql("""
  SELECT 
    COUNT(*) as total,
    AVG(salary) as avg_salary,
    MIN(salary) as min_salary,
    MAX(salary) as max_salary
  FROM employees
""")
result.show()

# Method 13: Using global temporary view
print("\n=== Access Global Temporary View ===")
result = spark.sql("SELECT name FROM global_temp.employees_global LIMIT 3")
result.show()

# Method 14: EXPLAIN query plan
print("\n=== EXPLAIN Query Plan ===")
spark.sql("""
  EXPLAIN
  SELECT name, salary
  FROM employees
  WHERE salary > 75000
  ORDER BY salary DESC
""").show()

# Method 15: Using aliases
print("\n=== Using Column Aliases ===")
result = spark.sql("""
  SELECT 
    name as employee_name,
    salary as annual_salary,
    department as dept
  FROM employees
  LIMIT 3
""")
result.show()
