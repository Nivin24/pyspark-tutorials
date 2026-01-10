# Spark SQL Q&A

## Beginner Level

### Q1: What is Spark SQL?
**A:** Spark SQL is Apache Spark's module for structured data processing, providing SQL-like queries on DataFrames with automatic optimization.

### Q2: How do you create a temporary view?
**A:** Using `df.createOrReplaceTempView("view_name")`. Accessible only in the current session.

### Q3: What is the difference between temporary and global views?
**A:** Temporary views are session-scoped. Global views are app-scoped and accessed via `global_temp.view_name`.

### Q4: How do you write a basic SELECT query?
**A:** `spark.sql("SELECT * FROM table_name")`

### Q5: What is a WHERE clause?
**A:** Filters rows based on conditions: `WHERE salary > 50000`

### Q6: What is ORDER BY?
**A:** Sorts results: `ORDER BY salary DESC`

### Q7: What is LIMIT?
**A:** Restricts number of rows: `LIMIT 10`

### Q8: What is GROUP BY?
**A:** Groups rows by column(s) for aggregation: `GROUP BY department`

### Q9: What is JOIN?
**A:** Combines rows from two tables: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`

### Q10: What is an aggregate function?
**A:** Functions that compute values: COUNT(), SUM(), AVG(), MIN(), MAX()

## Intermediate Level

### Q11: How do you use WHERE with AND/OR?
**A:** `WHERE salary > 50000 AND department = 'Sales'`

### Q12: What is HAVING?
**A:** Filters groups: `GROUP BY dept HAVING COUNT(*) > 5`

### Q13: What is a subquery?
**A:** Query inside another query: `WHERE salary > (SELECT AVG(salary))`

### Q14: What is a CTE?
**A:** Common Table Expression: `WITH high_earners AS (SELECT...) SELECT...`

### Q15: What are INNER JOINs?
**A:** Returns only matching rows from both tables.

### Q16: What are LEFT JOINs?
**A:** Returns all rows from left table + matching rows from right.

### Q17: What is UNION?
**A:** Combines results from two queries: `SELECT * FROM t1 UNION SELECT * FROM t2`

### Q18: What is DISTINCT?
**A:** Returns unique values: `SELECT DISTINCT department`

### Q19: What is NULL?
**A:** Missing/unknown value. Check with `IS NULL` or `IS NOT NULL`.

### Q20: What is CASE WHEN?
**A:** Conditional logic: `CASE WHEN salary > 80000 THEN 'High' ELSE 'Low' END`

## Advanced Level

### Q21: What is a window function?
**A:** Computes values across rows: `ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary)`

### Q22: What is PARTITION BY?
**A:** Divides rows into groups for window functions.

### Q23: What is ROW_NUMBER()?
**A:** Assigns sequential numbers to rows: `ROW_NUMBER() OVER (ORDER BY salary)`

### Q24: What is RANK()?
**A:** Assigns ranks with gaps for ties: `RANK() OVER (ORDER BY salary)`

### Q25: What is DENSE_RANK()?
**A:** Assigns ranks without gaps: `DENSE_RANK() OVER (ORDER BY salary)`

### Q26: What is LEAD()?
**A:** Accesses next row: `LEAD(salary) OVER (ORDER BY hire_date)`

### Q27: What is LAG()?
**A:** Accesses previous row: `LAG(salary) OVER (ORDER BY hire_date)`

### Q28: What is EXPLAIN?
**A:** Shows query plan: `EXPLAIN SELECT * FROM employees`

### Q29: What is the Catalyst optimizer?
**A:** Spark's optimizer that automat queries for efficiency.

### Q30: What is query pushdown?
**A:** Filtering data early to reduce processing.

## Advanced Concepts

### Q31: What is partitioning?
**A:** Dividing table by column for faster queries.

### Q32: What is bucketing?
**A:** Pre-sorting data for efficient joins.

### Q33: What is a view?
**A:** Virtual table created from SQL query.

### Q34: Can you modify a view?
**A:** No, views are read-only. Modify the underlying query instead.

### Q35: What is a database?
**A:** Logical grouping of tables and views.

### Q36: What is data skew?
**A:** Uneven data distribution causing performance issues.

### Q37: How to handle NULL in GROUP BY?
**A:** NULLs are treated as a group.

### Q38: What is CROSS JOIN?
**A:** Cartesian product - all combinations of rows.

### Q39: What is table hint?
**A:** Directs optimizer: `/*+ BROADCAST(table) */`

### Q40: What is COALESCE()?
**A:** Returns first non-NULL value: `COALESCE(col1, col2, 'default')`

### Q41: What is CAST()?
**A:** Converts data types: `CAST(age AS STRING)`

### Q42: What is string concatenation?
**A:** `CONCAT('Hello', ' ', 'World')`

### Q43: What is aggregation with NULL?
**A:** Most aggregations ignore NULLs (except COUNT(*))

### Q44: What is window frame?
**A:** Specifies rows for window: `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING`

### Q45: What is DEFAULT value?
**A:** Value assigned if none provided during insert.

### Q46: What is CHECK constraint?
**A:** Ensures column values meet condition.

### Q47: What is PRIMARY KEY?
**A:** Unique identifier for each row.

### Q48: What is FOREIGN KEY?
**A:** References primary key in another table.

### Q49: What is INDEX?
**A:** Speeds up queries on columns (Spark uses metadata).

### Q50: What are best practices?
**A:** Use EXPLAIN, partition data, push filters, cache strategically, use columnar formats.
