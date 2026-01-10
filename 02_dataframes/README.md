# DataFrame Operations in PySpark

## Overview
This folder contains comprehensive tutorials on working with Spark DataFrames - the primary data abstraction in modern PySpark. DataFrames provide a structured, SQL-like interface for data manipulation with powerful optimizations.

## 📚 Learning Progression

**Weeks:** 2-4 of the full curriculum
**Level:** Beginner to Intermediate
**Prerequisites:** Complete 01_fundamentals/ first

## 📋 Topics Covered

### Tutorial Files

1. **01_creating_dataframes.py** - Creating DataFrames from various sources
   - From Python collections (lists, tuples, dicts)
   - From CSV, JSON, Parquet files
   - From RDDs
   - With explicit schema definition
   - Inferring schema

2. **02_dataframe_operations.py** - Column operations and transformations
   - Selecting columns
   - Renaming columns
   - Adding new columns
   - Dropping columns
   - Type casting
   - Working with column expressions

3. **03_filtering_and_selection.py** - Filtering rows and selecting data
   - Filter conditions (where, ==, !=, >, <, >=, <=)
   - Complex conditions (AND, OR, NOT)
   - Contains, Like, In operations
   - Null value handling
   - distinct() and drop duplicates

4. **04_aggregations.py** - Aggregation functions and statistics
   - Count, sum, mean, min, max
   - Standard deviation, variance
   - Custom aggregations
   - Multiple aggregations
   - describe() for statistics

5. **05_joins.py** - Combining DataFrames
   - Inner join
   - Left/right outer join
   - Full outer join
   - Cross join
   - Left semi-join
   - Left anti-join
   - Join optimization

6. **06_groupby_and_windows.py** - Grouping and window functions
   - groupBy() with single/multiple columns
   - Aggregation after grouping
   - Window functions (ROW_NUMBER, RANK, LAG, LEAD)
   - Partitions within windows
   - Frame specifications

## 🎯 Learning Objectives

After completing this section, you will be able to:

- ✅ Create DataFrames from multiple data sources
- ✅ Select and transform columns efficiently
- ✅ Filter data using complex conditions
- ✅ Perform aggregations and statistical operations
- ✅ Join DataFrames in various ways
- ✅ Use groupBy for data aggregation
- ✅ Apply window functions for advanced analytics
- ✅ Optimize DataFrame operations
- ✅ Handle missing data
- ✅ Work with different data types

## 🔑 Key DataFrame Operations

| Operation | Purpose | Example |
|-----------|---------|----------|
| `select()` | Choose specific columns | `df.select("name", "age")` |
| `filter()` | Filter rows by condition | `df.filter(df.age > 25)` |
| `groupBy()` | Group data for aggregation | `df.groupBy("department")` |
| `join()` | Combine DataFrames | `df1.join(df2, on="id")` |
| `agg()` | Aggregate functions | `df.agg({"salary": "avg"})` |
| `window()` | Window functions | `Window.partitionBy("dept")` |
| `withColumn()` | Add/modify columns | `df.withColumn("bonus", df.salary*0.1)` |
| `orderBy()` | Sort DataFrame | `df.orderBy("salary".desc())` |
| `limit()` | Get first N rows | `df.limit(10)` |
| `distinct()` | Remove duplicates | `df.distinct()` |

## 📋 Prerequisites

Before starting this section, ensure you have:

- ✅ Completed 01_fundamentals/ section
- ✅ Understanding of Spark fundamentals (RDD, lazy evaluation)
- ✅ Knowledge of Spark Session setup
- ✅ Basic SQL understanding (SELECT, WHERE, JOIN, GROUP BY)
- ✅ Python knowledge (functions, loops, data structures)

## 📚 Study Materials

### Theoretical Concepts
- **CONCEPTS.md** - Detailed DataFrame concepts, optimization, best practices

### Practice Questions
- **Q&A.md** - 60+ questions covering all topics

### Code Examples
- All 6 tutorial files with real-world examples

## 🚀 Running the Tutorials

```bash
# Navigate to folder
cd 02_dataframes

# Run individual tutorials
python 01_creating_dataframes.py
python 02_dataframe_operations.py
python 03_filtering_and_selection.py
python 04_aggregations.py
python 05_joins.py
python 06_groupby_and_windows.py

# Or run in Jupyter notebook
jupyter notebook
```

## 💡 Tips for Learning

1. **Read the theory first** - Start with CONCEPTS.md for deep understanding
2. **Run examples** - Execute each tutorial file and modify examples
3. **Experiment** - Try different column names, conditions, and operations
4. **Review Q&A** - Test your understanding with Q&A.md
5. **Compare operations** - Understand how different approaches yield same results
6. **Monitor execution** - Use Spark UI (localhost:4040) to see job details
7. **Optimize gradually** - Learn what makes queries slow and how to optimize

## 🔗 Related Concepts

### From 01_fundamentals
- Lazy evaluation enables DataFrame optimization
- Partitions affect how DataFrames are processed
- Transformations (lazy) vs Actions (trigger execution)

### To 03_sql
- DataFrames are optimized through Catalyst optimizer
- SQL queries on DataFrames work similarly
- Same operations can be written in SQL or DataFrame API

## 📊 Common Performance Pitfalls

### ❌ Avoid:
1. Collecting large DataFrames to driver memory
2. Using RDD methods with DataFrames
3. Not caching frequently used DataFrames
4. Creating unnecessary columns
5. Filtering late instead of early
6. Inefficient join orders

### ✅ Do:
1. Use DataFrame API instead of RDDs
2. Push filters as early as possible
3. Cache intermediate results
4. Use appropriate join types
5. Broadcast small tables in joins
6. Use columnar storage (Parquet)

## 🎓 Advanced Topics

After mastering basics, explore:
- Bucketing for optimized joins
- Broadcast joins for small tables
- Skew handling in joins
- Complex window partitioning
- Custom aggregations with UDFs
- Performance tuning strategies

## 📈 Progression Map

```
01_Fundamentals (RDD, Spark Session, Basics)
            ↓
02_DataFrames (THIS SECTION)
    ├─ Creating DataFrames
    ├─ Operations & Filtering
    ├─ Aggregations
    ├─ Joins
    └─ GroupBy & Windows
            ↓
03_SQL (SQL Queries, Optimization)
            ↓
04_Streaming (Real-time processing)
            ↓
Advanced Topics & Projects
```

## ❓ Next Steps

1. Study CONCEPTS.md for theoretical foundation
2. Run all 6 tutorial files
3. Complete exercises in Q&A.md
4. Modify examples with your own data
5. Build small projects combining multiple operations
6. Move to 03_sql/ for SQL-based DataFrame operations

## 📚 Resources

- [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)
- [PySpark Functions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/functions.html)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)

## 📝 Tips for Success

1. **Understand schema** - Always know your DataFrame structure
2. **Use explain()** - Check execution plans
3. **Think in sets** - DataFrames operate on entire columns, not rows
4. **Leverage caching** - Avoid recomputation
5. **Monitor resources** - Watch memory usage
6. **Practice joins** - Most complex operation, worth extra time

---

**Total Files in This Folder:**
- 6 Python tutorial files
- 1 Concepts guide (markdown)
- 1 Q&A guide with 60+ questions
- 1 README (this file)

**Estimated Time:** 8-12 hours of study and practice

**Difficulty Level:** Beginner to Intermediate

---

**Last Updated:** January 2026
**Created for:** Data Science & Python enthusiasts
**Status:** Complete and Ready to Learn
