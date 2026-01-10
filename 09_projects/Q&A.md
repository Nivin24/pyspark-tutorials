# 09_projects - Questions & Answers

## Project Implementation Questions

### Q1: Why use Collaborative Filtering instead of Content-Based Filtering?
**A:** Collaborative Filtering discovers patterns human curators might miss by leveraging collective preferences. Content-Based might fail for cold-start items (new movies with no metadata). CF works better when user preferences are more important than item features.

### Q2: How does ALS (Alternating Least Squares) handle sparse user-item matrices?
**A:** ALS works with sparse matrices efficiently by:
- Not computing missing ratings explicitly
- Only updating factors for observed interactions
- Using iterative optimization that converges with partial data
- Reducing memory footprint compared to dense matrix approaches

### Q3: What are the optimal values for ALS hyperparameters (rank, iterations, lambda)?
**A:** 
- **Rank**: 10-100 (higher = more expressive, slower, overfitting risk)
- **Iterations**: 5-20 (diminishing returns after 10)
- **Lambda (regularization)**: 0.01-0.1 (prevents overfitting)
- Use cross-validation with your data to find optimal values

### Q4: How do you handle the cold-start problem in recommendations?
**A:** 
1. **New Users**: Use popularity-based or content-based recommendations
2. **New Items**: Use item features or collaborative signal from similar items
3. **Hybrid**: Combine multiple approaches
4. **Context**: Use user demographics or session information

### Q5: What's the difference between implicit and explicit feedback in ALS?
**A:**
- **Explicit**: Ratings (1-5 stars) - direct preference signal
- **Implicit**: Purchases, views, clicks - interpret as preference intensity
- Implicit matrices are denser but noisier
- ALS can handle both, but parameter tuning differs

---

## ETL Pipeline Questions

### Q6: What makes a good ETL pipeline design?
**A:** A good pipeline:
- **Idempotent**: Safe to re-run without side effects
- **Traceable**: Clear data lineage and transformation history
- **Resilient**: Handles failures gracefully with retry logic
- **Performant**: Optimized for throughput and latency
- **Monitored**: Logs metrics for health checks

### Q7: How do you ensure data quality in ETL pipelines?
**A:** Implement quality gates:
1. **Schema Validation**: Check column types and names
2. **Range Checks**: Verify numeric values are within expected bounds
3. **Null Checks**: Identify missing critical data
4. **Referential Integrity**: Validate foreign key relationships
5. **Duplicate Detection**: Find and handle duplicates
6. **Statistical Checks**: Compare row counts, distributions

### Q8: When should you use streaming vs batch ETL?
**A:**
- **Batch**: Large volumes, scheduled processing (nightly), cost-sensitive
- **Streaming**: Low-latency requirements, event-driven, real-time dashboards
- **Hybrid**: Combine both (streaming for real-time, batch for reprocessing)

### Q9: How do you handle late-arriving data in ETL?
**A:**
- Use watermarks to track data completeness
- Re-process data with late arrivals
- Maintain state for late updates
- Define SLA for data arrival cutoff
- Flag late data separately for reconciliation

### Q10: What's the optimal partition strategy for ETL pipelines?
**A:** Partition by:
- **Time**: Daily, hourly (enables incremental loading)
- **Geography**: Region, country (natural business division)
- **Business Logic**: Product category, customer segment
- **Data Volume**: Maintain 128MB-1GB partitions
- Avoid over-partitioning (too many small files)

### Q11: How do you handle backfilling historical data?
**A:**
1. Write backfill logic that recomputes aggregates
2. Use date parameters to limit processing
3. Store raw data separately from aggregates
4. Validate against expected outputs
5. Update dependents after backfill completes

### Q12: What's idempotency and why is it critical for ETL?
**A:** Idempotency means running the same operation multiple times produces the same result. Critical for:
- Recovering from failures without data corruption
- Re-running failed jobs without manual cleanup
- Ensuring data consistency across retries
- Example: Use `upsert` instead of `insert` to be safe

---

## Log Analysis Questions

### Q13: How do you parse unstructured logs efficiently?
**A:**
- Use regex patterns with `regexp_extract()`
- Pre-define schema for known log formats
- Use `from_unixtime()` for timestamp conversion
- Filter non-matching logs separately
- Cache parsed results if reusing

### Q14: What's the best way to detect anomalies in logs?
**A:** Multi-level approach:
1. **Rule-based**: Known error patterns, thresholds
2. **Statistical**: Z-score, IQR for outliers
3. **Time-series**: Prophet, ARIMA for trend deviations
4. **ML-based**: Isolation Forest, One-Class SVM
5. **Correlation**: Track related metrics together

### Q15: How do you handle log data that exceeds available memory?
**A:**
- Use Spark's distributed processing (problem solved!)
- Partition by time (process in chunks)
- Aggregate before collecting results
- Use streaming instead of batch for continuous data
- Archive old logs to cheaper storage

### Q16: What metrics matter most for production monitoring?
**A:**
- **Error Rate**: Percentage of failed operations
- **Latency**: P50, P95, P99 response times
- **Throughput**: Operations per second
- **Availability**: Uptime percentage
- **Resource Utilization**: CPU, Memory, Disk
- **Business Metrics**: Conversion rate, user impact

### Q17: How do you correlate errors across services?
**A:**
- Use **correlation IDs**: Same ID across service logs
- **Distributed tracing**: OpenTelemetry, Jaeger
- **Shared timestamp**: Time-sync all servers
- **Log aggregation**: Centralize logs (ELK, Splunk)
- **Event streams**: Kafka for ordered correlation

### Q18: What's the retention strategy for log data?
**A:**
- **Hot**: 7-30 days in fast storage (SSD)
- **Warm**: 1-3 months in cloud storage
- **Cold**: Long-term archive (S3 Glacier)
- **Delete**: Non-critical logs after retention period
- Regulatory: Follow compliance requirements (GDPR, HIPAA)

---

## PySpark Optimization Questions

### Q19: How do you optimize slow Spark jobs?
**A:** Systematic approach:
1. Check DAG for shuffle operations
2. Increase parallelism (partition count)
3. Use proper join strategies (broadcast small tables)
4. Enable adaptive query execution
5. Cache intermediate results
6. Use Parquet format instead of CSV
7. Profile with Spark UI to find bottlenecks

### Q20: What's the difference between persist() and cache()?
**A:**
- `cache()`: Shorthand for `persist(StorageLevel.MEMORY_ONLY)`
- `persist()`: Flexible - MEMORY, DISK, BOTH, OFF_HEAP
- Both are lazy - trigger with action
- Use `unpersist()` to free memory
- Cache for reused DataFrames, not one-time operations

### Q21: When should you use broadcast variables?
**A:** Use for:
- Small reference tables < 100MB
- Lookup dictionaries in joins
- Configuration parameters
- Avoid: Large DataFrames (memory waste), frequently changing data
- Example: Broadcasting dimension tables to join with fact tables

### Q22: How do you handle data skew in Spark?
**A:**
- **Identify**: Use `groupBy().count()` to find hot partitions
- **Salting**: Add random suffix to skewed keys
- **Isolation**: Handle skewed keys separately
- **Bucketing**: Pre-organize data
- **Sampling**: Use random sampling instead of full processing

### Q23: What's the optimal partition size for Spark?
**A:**
- **Target**: 128MB - 512MB per partition
- **Too small**: Overhead, scheduling delays
- **Too large**: Memory pressure, slower recovery
- Calculate: Total Data Size / (Executor Memory * Parallelism)
- Repartition if needed: `df.repartition(num_partitions)`

### Q24: How do you debug Spark applications?
**A:**
- **Spark UI**: localhost:4040 for job visualization
- **Logs**: Check executor and driver logs
- **sample()**: Test on subset before full run
- **explain()`: Check physical plan with `df.explain()`
- **print statements**: Use `show()` for data validation
- **Unit tests**: Test transformations in isolation

### Q25: Should you use RDDs or DataFrames?
**A:** **Use DataFrames** unless:
- Unstructured data (text, binary)
- Need fine-grained control
- Complex DAG manipulation
- Otherwise: DataFrames are 10-100x faster due to Catalyst optimizer
