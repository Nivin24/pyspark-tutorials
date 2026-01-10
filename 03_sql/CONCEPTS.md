# Spark SQL Concepts

## Table of Contents
1. SQL Fundamentals
2. Views and Databases
3. Query Execution
4. Joins and Subqueries
5. Aggregations and Grouping
6. Window Functions
7. Query Optimization
8. Performance Tuning
9. Best Practices

## 1. SQL Fundamentals

### What is Spark SQL?
Spark SQL is Apache Spark's module for structured data processing. It provides a unified programming interface that leverages SQL and programmatic interfaces through DataFrames and Datasets.

### Key Features:
- **SQL Queries:** Standard SQL syntax for data analysis
- **DataFrames & Datasets:** Distributed data structures with optimizations
- **Catalyst Optimizer:** Automatic query optimization
- **Tungsten:** Memory and CPU optimization

## 2. Views and Databases

### Temporary Views
Created within a session, automatically dropped when session ends:
```sql
df.createOrReplaceTempView("employees")
```

### Global Temporary Views
Accessible across sessions, dropped when Spark app terminates:
```sql
df.createGlobalTempView("employees")
SELECT * FROM global_temp.employees
```

### Permanent Views
Stored in the metastore, persist across sessions:
```sql
CREATE VIEW employees_view AS SELECT * FROM employees
```

### Databases
Logical grouping of tables and views:
```sql
CREATE DATABASE analytics
USE analytics
```

## 3. Query Execution

### SQL Query Lifecycle
1. **Parsing:** Syntax validation
2. **Analysis:** Table and column resolution
3. **Optimization:** Catalyst optimizes the plan
4. **Physical Planning:** Creates executables
5. **Execution:** Distributes across cluster

### EXPLAIN Command
```sql
EXPLAIN SELECT * FROM employees WHERE salary > 50000
EXPLAIN FORMATTED SELECT * FROM employees
EXPLAIN EXTENDED SELECT * FROM employees
```

## 4. Joins and Subqueries

### Join Types
- **INNER JOIN:** Only matching rows
- **LEFT OUTER JOIN:** All left rows + matching right
- **RIGHT OUTER JOIN:** All right rows + matching left
- **FULL OUTER JOIN:** All rows from both
- **CROSS JOIN:** Cartesian product

### Subqueries
```sql
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
```

### CTEs (Common Table Expressions)
```sql
WITH high_earners AS (
  SELECT * FROM employees WHERE salary > 80000
)
SELECT * FROM high_earners
```

## 5. Aggregations and Grouping

### Aggregate Functions
- **COUNT:** Number of rows
- **SUM:** Total of values
- **AVG:** Average value
- **MIN/MAX:** Minimum/Maximum
- **STDDEV:** Standard deviation
- **VAR:** Variance
- **COLLECT_LIST:** Array of values
- **COLLECT_SET:** Set of unique values

### GROUP BY
```sql
SELECT department, COUNT(*) as emp_count, AVG(salary)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5
```

## 6. Window Functions

### Syntax
```sql
function() OVER (
  PARTITION BY col1, col2
  ORDER BY col3
  ROWS/RANGE BETWEEN start AND end
)
```

### Function Types
- **Ranking:** ROW_NUMBER(), RANK(), DENSE_RANK()
- **Analytic:** LEAD(), LAG(), FIRST_VALUE(), LAST_VALUE()
- **Aggregate:** SUM(), AVG(), COUNT() (as window functions)

## 7. Query Optimization

### Catalyst Optimizer Techniques
1. **Predicate Pushdown:** Filter early
2. **Projection Pruning:** Select only needed columns
3. **Constant Folding:** Pre-compute constants
4. **Join Reordering:** Optimize join sequence
5. **Expression Simplification:** Reduce complexity

### Cost-Based Optimization
Uses table statistics to choose best plan:
```sql
ANALYZE TABLE employees COMPUTE STATISTICS
```

## 8. Performance Tuning

### Partitioning
Divide data by column for faster queries:
```sql
CREATE TABLE employees_partitioned
PARTITIONED BY (year)
AS SELECT * FROM employees
```

### Bucketing
Pre-sort for efficient joins:
```sql
CREATE TABLE employees_bucketed
BUCKETED BY (emp_id) INTO 10 BUCKETS
AS SELECT * FROM employees
```

### Caching
Store frequently accessed data:
```python
df.cache()
df.show()
```

## 9. Best Practices

1. **Use EXPLAIN:** Understand query plans before execution
2. **Analyze Statistics:** Helps optimizer make better decisions
3. **Partition Data:** Significant performance improvement
4. **Push Predicates:** Filter as early as possible
5. **Avoid Cartesian Joins:** Can cause memory issues
6. **Use Columnar Formats:** Parquet for storage
7. **Cache Strategically:** Don't cache everything
8. **Monitor Execution:** Use Spark UI for bottleneck identification
9. **Write Readable SQL:** Use proper formatting
10. **Test Performance:** Benchmark before production
