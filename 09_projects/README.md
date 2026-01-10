# 09_projects - Real-World PySpark Applications

## Overview
This folder contains end-to-end PySpark projects demonstrating practical applications in machine learning, data engineering, and analytics. Each project showcases best practices for building production-grade data systems.

## Projects in This Folder

### 1. **Movie Recommendation System** (`01_movie_recommendation.py`)
A collaborative filtering recommendation engine using Apache Spark MLlib's Alternating Least Squares (ALS) algorithm.

**What You'll Learn:**
- Building recommendation systems at scale
- Matrix factorization techniques
- Model evaluation and hyperparameter tuning
- Handling sparse user-item interaction matrices

**Key Techniques:**
- ALS algorithm for implicit/explicit feedback
- Training/testing data split
- Precision@K metric calculation
- Root Mean Squared Error (RMSE) evaluation

**Real-World Application:**
- Netflix movie recommendations
- Spotify music suggestions
- Amazon product recommendations
- YouTube video suggestions

**Code Complexity:** Medium | **Data Volume:** 10K-100K interactions

---

### 2. **ETL Data Pipeline** (`02_etl_pipeline.py`)
A complete Extract-Transform-Load pipeline demonstrating data ingestion, cleaning, transformation, and output to multiple formats.

**What You'll Learn:**
- Designing robust ETL workflows
- Data quality validation
- Handling multiple data sources
- Writing to multiple output formats

**Key Stages:**
- **Extract**: Read raw data from multiple sources (CSV, JSON)
- **Transform**: Clean, validate, and enrich data
- **Load**: Write to Parquet, CSV, and database formats

**Transformations Covered:**
- Null value handling
- Duplicate removal
- Type conversions
- Aggregations and joins
- Derived metrics calculation

**Real-World Application:**
- Daily data warehouse loading
- API data ingestion
- Log aggregation pipelines
- Business intelligence feeds

**Code Complexity:** Medium-High | **Data Volume:** 100K-1M records

---

### 3. **Real-Time Log Analysis** (`03_log_analysis.py`)
A comprehensive log analysis system for error detection, anomaly identification, and operational insights.

**What You'll Learn:**
- Parsing unstructured log data
- Error pattern detection
- Anomaly identification
- Time-series analysis
- Service monitoring

**Analysis Components:**
- Error frequency and patterns
- Problematic IP addresses tracking
- Log level distribution
- Critical incident reporting
- Service-level anomalies

**Metrics Calculated:**
- Error rate per service
- Error patterns and types
- Time-based activity analysis
- Critical incident count
- Service health statistics

**Real-World Application:**
- Production system monitoring
- Root cause analysis
- Performance troubleshooting
- SLA compliance tracking
- Security incident detection

**Code Complexity:** Medium | **Data Volume:** 1M+ log entries

---

## Getting Started

### Prerequisites
```bash
# Install PySpark
pip install pyspark

# Install additional libraries (optional)
pip install numpy pandas scikit-learn
```

### Running the Projects

#### Project 1: Movie Recommendations
```bash
cd 09_projects
spark-submit 01_movie_recommendation.py
```

#### Project 2: ETL Pipeline
```bash
spark-submit 02_etl_pipeline.py
```

#### Project 3: Log Analysis
```bash
spark-submit 03_log_analysis.py
```

### Expected Output
- Structured analysis results
- Performance metrics
- Data quality statistics
- Actionable insights

## Project Architecture

### Common Components
```
Each project includes:
├── Data Generation/Loading (sample data)
├── Data Transformation (business logic)
├── Analysis/Modeling (insights extraction)
└── Results Output (metrics and reports)
```

### Spark Configuration
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ProjectName") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()
```

## Key Concepts Demonstrated

### 1. Distributed Computing
- Leveraging multiple cores and nodes
- Partition strategies
- Shuffle minimization

### 2. Data Quality
- Validation rules
- Anomaly detection
- Error handling

### 3. Performance Optimization
- Query optimization
- Caching strategies
- Broadcast joins

### 4. Scalability
- Handling large datasets
- Memory management
- Cluster configuration

## Data Specifications

### Dataset Sizes
| Project | Records | Size | Processing Time |
|---------|---------|------|------------------|
| Movie Recommendations | 10K | ~2MB | 10-15s |
| ETL Pipeline | 100K | ~20MB | 20-30s |
| Log Analysis | 10K logs | ~5MB | 15-20s |

## Learning Path

**Beginner:** Start with Project 1 (Movie Recommendations)
- Understand ALS algorithm basics
- Learn about model evaluation
- Practice with MLlib

**Intermediate:** Move to Project 2 (ETL Pipeline)
- Design multi-stage pipelines
- Implement data validation
- Handle multiple formats

**Advanced:** Explore Project 3 (Log Analysis)
- Parse unstructured data
- Implement anomaly detection
- Build monitoring systems

## Performance Metrics

### Typical Results
- **Movie Recommendations**: RMSE ~0.8-1.2, Coverage ~80%
- **ETL Pipeline**: Process 10K records in <5 seconds
- **Log Analysis**: Identify anomalies in 100K logs within 10 seconds

## Optimization Tips

### For Better Performance:
1. Use Parquet format for data storage
2. Enable adaptive query execution
3. Broadcast small tables in joins
4. Partition data by time/category
5. Cache frequently accessed DataFrames
6. Use column selection to reduce I/O

### Memory Management:
- Monitor executor memory with Spark UI
- Adjust `spark.executor.memory` as needed
- Use `unpersist()` to release cached data
- Avoid collecting large results to driver

## Troubleshooting

### Common Issues

**Out of Memory Errors:**
- Increase executor memory
- Reduce DataFrame size with filtering
- Use sampling for testing

**Slow Job Execution:**
- Check for shuffle operations in DAG
- Increase partition count
- Use broadcast variables for small tables

**Data Quality Issues:**
- Add explicit validation steps
- Log rejected records
- Monitor null percentages

## Extension Ideas

### Project 1 Enhancements:
- Add cross-validation
- Implement content-based filtering
- Build hybrid recommendation system
- Add real-time prediction capability

### Project 2 Enhancements:
- Add data lineage tracking
- Implement incremental loading
- Add data profiling
- Build failure recovery mechanisms

### Project 3 Enhancements:
- Implement streaming log processing
- Add machine learning anomaly detection
- Build alerting system
- Create visualization dashboards

## Best Practices

1. **Code Organization**: Structure code into functions and classes
2. **Error Handling**: Implement try-catch blocks and data validation
3. **Logging**: Add informative print statements at each stage
4. **Testing**: Validate outputs at each transformation step
5. **Documentation**: Include comments explaining complex logic
6. **Version Control**: Track changes and maintain history

## Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark MLlib Guide](https://spark.apache.org/docs/latest/ml-guide.html)
- [Spark SQL Programming Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Performance Tuning](https://spark.apache.org/docs/latest/tuning.html)

## Additional Files

- **CONCEPTS.md**: Detailed explanations of algorithms and techniques
- **Q&A.md**: Common questions and answers about these projects

## Next Steps

1. Run each project with provided sample data
2. Understand the transformations and analysis
3. Modify parameters and observe results
4. Try with your own datasets
5. Combine techniques across projects
6. Deploy to production clusters

## Summary

These projects demonstrate:
✓ Building production-grade data systems  
✓ Scalable machine learning  
✓ ETL best practices  
✓ Real-time data analysis  
✓ Performance optimization  
✓ Data quality assurance  

By studying and extending these projects, you'll gain practical skills for enterprise data engineering and analytics roles.
