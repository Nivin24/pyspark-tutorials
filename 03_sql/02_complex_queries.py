"""Spark SQL - Complex Queries (Joins, Subqueries, CTEs)

Covers: INNER/LEFT/RIGHT/FULL JOINs, subqueries, CTEs
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Complex Queries").getOrCreate()

# Employee data
emp_data = [(1, "Alice", 1), (2, "Bob", 1), (3, "Charlie", 2)]
df_emp = spark.createDataFrame(emp_data, ["emp_id", "name", "dept_id"])

# Department data
dept_data = [(1, "Sales"), (2, "Engineering")]
df_dept = spark.createDataFrame(dept_data, ["dept_id", "dept_name"])

df_emp.createOrReplaceTempView("employees")
df_dept.createOrReplaceTempView("departments")

print("\n=== INNER JOIN ===")
spark.sql("""
  SELECT e.name, d.dept_name
  FROM employees e
  INNER JOIN departments d ON e.dept_id = d.dept_id
""").show()

print("\n=== LEFT JOIN ===")
spark.sql("""
  SELECT e.name, d.dept_name
  FROM employees e
  LEFT JOIN departments d ON e.dept_id = d.dept_id
""").show()

print("\n=== Subquery ===")
spark.sql("""
  SELECT name FROM employees
  WHERE dept_id = (SELECT dept_id FROM departments WHERE dept_name = 'Sales')
""").show()

print("\n=== CTE (WITH clause) ===")
spark.sql("""
  WITH sales_dept AS (
    SELECT dept_id FROM departments WHERE dept_name = 'Sales'
  )
  SELECT e.name FROM employees e
  WHERE e.dept_id IN (SELECT dept_id FROM sales_dept)
""").show()
