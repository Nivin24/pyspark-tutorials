# Fundamentals of PySpark

## Overview
This folder contains introductory tutorials to learn the basics of Apache Spark and PySpark.

## Topics Covered

1. **01_introduction_to_spark.py** - Introduction to Spark architecture and ecosystem
2. **02_spark_session_setup.py** - Setting up and configuring Spark Session
3. **03_rdd_basics.py** - Resilient Distributed Datasets (RDDs) fundamentals
4. **04_dataframe_basics.py** - Introduction to DataFrames

## Learning Objectives

- Understand Spark architecture (Driver, Executors, Cluster Manager)
- Learn about RDDs and their operations
- Create and manipulate DataFrames
- Understand lazy evaluation in Spark
- Work with basic transformations and actions

## Prerequisites
- Python 3.7+
- PySpark 3.0+
- Basic Python knowledge

## Running the Tutorials

```bash
cd 01_fundamentals
python 01_introduction_to_spark.py
```

## Key Concepts

- **RDD**: Immutable, distributed collection of objects
- **DataFrame**: Distributed collection with named columns (like a table)
- **Transformation**: Lazy operation that returns a new RDD/DataFrame
- **Action**: Operation that returns a value to the driver or writes data
- **Spark Session**: Entry point for Spark functionality

## Next Steps
After completing this section, move to `02_dataframes/` to learn more about DataFrame operations.
