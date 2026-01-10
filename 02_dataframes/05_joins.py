"""DataFrame Joins in PySpark

This tutorial covers:
- Inner joins
- Left outer joins
- Right outer joins
- Full outer joins
- Left semi joins
- Left anti joins
- Cross joins
"""

from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("Joins").getOrCreate()

# Employee data
employee_data = [
    (1, "Alice", "Sales"),
    (2, "Bob", "Engineering"),
    (3, "Charlie", "Sales"),
    (4, "David", "Management"),
    (5, "Eve", "Engineering")
]

# Department data
dept_data = [
    ("Sales", "NYC"),
    ("Engineering", "SF"),
    ("HR", "Boston")
]

# Salary data
salary_data = [
    (1, 60000),
    (2, 95000),
    (3, 75000),
    (6, 80000)  # Extra record for join examples
]

emp_df = spark.createDataFrame(employee_data, ["emp_id", "name", "dept"])
dept_df = spark.createDataFrame(dept_data, ["dept", "location"])
sal_df = spark.createDataFrame(salary_data, ["emp_id", "salary"])

print("\n=== Employee DataFrame ===")
emp_df.show()

print("\n=== Department DataFrame ===")
dept_df.show()

print("\n=== Salary DataFrame ===")
sal_df.show()

print("\n=== Method 1: Inner Join ===")
emp_df.join(dept_df, emp_df.dept == dept_df.dept, "inner").show()

print("\n=== Method 2: Left Outer Join ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "left_outer").show()

print("\n=== Method 3: Right Outer Join ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "right_outer").show()

print("\n=== Method 4: Full Outer Join ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "outer").show()

print("\n=== Method 5: Left Semi Join ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "left_semi").show()

print("\n=== Method 6: Left Anti Join ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "left_anti").show()

print("\n=== Method 7: Cross Join ===")
small_dept = dept_df.filter(dept_df.dept.isin(["Sales", "Engineering"]))
emp_df.crossJoin(small_dept).show()

print("\n=== Method 8: Join with Select Specific Columns ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "inner").select(
    emp_df.name, emp_df.dept, sal_df.salary
).show()

print("\n=== Method 9: Multiple Joins ===")
emp_df.join(sal_df, emp_df.emp_id == sal_df.emp_id, "inner").join(
    dept_df, emp_df.dept == dept_df.dept, "inner"
).select(emp_df.name, emp_df.dept, dept_df.location, sal_df.salary).show()

print("\n=== Method 10: Using SQL Joins ===")
emp_df.createOrReplaceTempView("employees")
sal_df.createOrReplaceTempView("salaries")
spark.sql("SELECT e.name, e.dept, s.salary FROM employees e INNER JOIN salaries s ON e.emp_id = s.emp_id").show()
