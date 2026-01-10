# Spark SQL and Query Optimization

## Overview

This folder contains comprehensive tutorials on working with Spark SQL - the powerful SQL engine in Apache Spark. Spark SQL provides a SQL-like interface for querying and analyzing structured data at scale, with optimizations that make it one of the fastest SQL engines available.

## 📚 Learning Progression

**Weeks: 3-4 of the full curriculum**
**Level: Beginner to Intermediate**
**Prerequisites:** Complete 01_fundamentals/ and 02_dataframes/

## 🎯 Topics Covered

### Tutorial Files:
1. **01_sql_basics.py** - SQL fundamentals and temp views
2. **02_complex_queries.py** - Joins, subqueries, CTEs
3. **03_aggregations_groupby.py** - Aggregation functions and grouping
4. **04_window_functions.py** - Window functions for advanced analytics
5. **05_query_optimization.py** - Performance tuning and query plans
6. **06_advanced_sql.py** - UNION, INTERSECT, EXCEPT operations

### Supplementary Materials:
- **CONCEPTS.md** - Deep dive into SQL theory and optimization
- **Q&A.md** - 50+ questions covering all difficulty levels

## 📖 Learning Path

### Beginner (Week 1)
- Creating temporary and permanent views
- Basic SELECT statements
- WHERE clauses and filtering
- ORDER BY and LIMIT

### Intermediate (Week 2)
- Joins (INNER, LEFT, RIGHT, FULL OUTER)
- Subqueries and CTEs
- Aggregation functions
- GROUP BY operations

### Advanced (Week 3-4)
- Window functions for rankings and running totals
- Query optimization and execution plans
- Set operations (UNION, INTERSECT, EXCEPT)
- Complex analytical queries

## 🔑 Key Concepts

### Spark SQL Features:
- **Catalyst Optimizer:** Optimizes SQL queries automatically
- **Cost-based Optimizer:** Selects best execution plan
- **Tungsten:** Project for efficient memory management
- **SQL-on-Data:** Direct SQL queries on structured data

### Query Optimization Techniques:
1. Push predicates down
2. Use columnar storage formats
3. Partition pruning
4. Broadcasting small tables
5. Caching intermediate results

## 💡 Best Practices

1. **Use SQL for Complex Queries:** SQL is often clearer than DataFrame API
2. **Optimize Early:** Use EXPLAIN to understand query plans
3. **Partition Your Data:** Improve query performance significantly
4. **Cache Strategically:** Avoid unnecessary caching overhead
5. **Use Standard SQL:** Ensures portability across systems
6. **Index Awareness:** Plan queries considering data distribution
7. **Monitor Performance:** Use Spark UI to track execution
8. **Write Readable Queries:** Use proper formatting and comments

## 🛠️ Tools & Resources

- **Spark SQL Documentation:** Official Apache Spark SQL guide
- **Catalyst Optimizer Insights:** Understanding query optimization
- **Query Plans:** EXPLAIN vs EXPLAIN FORMATTED
- **Benchmarking:** Performance comparison tools

## 📊 Real-World Scenarios

This module covers practical SQL scenarios:
- Customer analytics queries
- Sales trend analysis
- Data aggregation pipelines
- ETL transformations
- Report generation
- Data warehouse queries

## 🎓 Learning Tips

1. **Run Every Query:** Execute all examples and understand output
2. **Modify Code:** Change parameters and observe results
3. **Explain Plans:** Use EXPLAIN to see query optimization
4. **Practice:** Write your own queries from scratch
5. **Compare:** Execute same logic in SQL vs DataFrame API

## 📝 File Structure

```
03_sql/
├── README.md              # This file
├── CONCEPTS.md           # Theoretical foundations
├── Q&A.md               # Questions and answers
├── 01_sql_basics.py
├── 02_complex_queries.py
├── 03_aggregations_groupby.py
├── 04_window_functions.py
├── 05_query_optimization.py
└── 06_advanced_sql.py
```

## ✅ Checklist

Before moving to the next module, ensure you understand:
- [ ] How to create temporary views
- [ ] Writing complex SQL queries
- [ ] Joins across multiple tables
- [ ] Window functions usage
- [ ] Reading execution plans
- [ ] Query optimization techniques
- [ ] Performance best practices

## 🔗 Next Steps

After completing this module, proceed to **04_streaming/** for:
- Real-time data processing
- Structured streaming
- Event-time processing
- Stateful streaming operations
