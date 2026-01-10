# Spark Structured Streaming - Core Concepts

## 1. Stream Processing Fundamentals

### What is Stream Processing?
Stream processing is the real-time processing of data that flows continuously into a system. Unlike batch processing which processes data in fixed blocks, stream processing handles data as it arrives.

**Key Characteristics:**
- Continuous data flow
- Real-time processing
- Unbounded datasets
- Low-latency results
- Stateless and stateful operations

### Apache Spark Structured Streaming
Structured Streaming is Spark's engine for building streaming applications with the same DataFrame/SQL API used in batch processing. It provides:
- Unified batch and streaming API
- Exactly-once processing semantics
- Incremental state management
- SQL support for streaming queries
- Built-in micro-batching for high throughput

## 2. Streaming Sources and Sinks

### Common Streaming Sources:
1. **Kafka** - Distributed message queue
2. **Socket** - TCP socket connections
3. **File** - Files in a directory
4. **Rate** - Built-in source for testing
5. **Kinesis** - AWS streaming service
6. **Pubsub** - Google Cloud Pub/Sub

### Common Streaming Sinks:
1. **Console** - Print to console
2. **Parquet/CSV/JSON** - File-based outputs
3. **Kafka** - Write to Kafka topics
4. **Foreach** - Custom sink for each row
5. **Memory** - In-memory table (testing only)
6. **Delta Lake** - ACID-compliant data lake

## 3. DataFrame and Dataset APIs for Streaming

### Streaming DataFrames
```python
streamingDF = spark.readStream \
    .format("source") \
    .option("key", "value") \
    .load()
```

### Key Differences from Batch:
- **Unbounded**: Continuously appended with new data
- **Lazy Evaluation**: Queries define computation graph
- **Incremental Execution**: Only new data is processed

## 4. Window Operations

### Tumbling Windows (Fixed Size)
Divide data into fixed-size, non-overlapping windows
```python
windowed_data = df.groupBy("column", window("timestamp", "10 minutes")).agg(sum("value"))
```

### Sliding Windows (Overlapping)
Windows overlap based on slide interval
```python
windowed_data = df.groupBy("column", window("timestamp", "10 minutes", "5 minutes")).agg(sum("value"))
```

### Session Windows
Group events by inactivity periods
```python
session_data = df.groupBy("column", session_window("timestamp", "5 minutes")).agg(sum("value"))
```

## 5. Stateful Operations

### Stateless Operations
No dependency on previous data:
- select(), where(), filter()
- map(), flatMap()
- Windowed aggregations without state

### Stateful Operations
Depend on previous data in stream:
- Aggregations: count, sum, avg, max, min
- updateStateByKey() - Custom state updates
- flatMapGroupsWithState() - Advanced state management

### State Management
- **In-memory state**: Fast but limited by RAM
- **State checkpointing**: Persists state for fault recovery
- **State TTL**: Automatic cleanup of old state

## 6. Triggers and Micro-batching

### Processing Modes
1. **Default (Micro-batch)**
   - Executes micro-batches at intervals
   - Latency: 0.5-2 seconds
   - Throughput: Very high

2. **Continuous**
   - True low-latency processing
   - Latency: ~1ms
   - Limited transformation support

3. **Once**
   - Single micro-batch execution
   - Useful for testing

### Trigger Types
```python
# Default trigger
query.writeStream.trigger(processingTime="5 seconds")

# Once trigger
query.writeStream.trigger(once=True)

# Continuous processing
query.writeStream.trigger(continuous="1 second")
```

## 7. Output Modes

### Append Mode (Default)
- Only new rows in result table are written
- Use when: No aggregations or only append-only aggregations
- Lowest latency and storage

### Update Mode
- Modified rows in result table are written
- Use when: Updating aggregations
- Lower storage than Complete mode

### Complete Mode
- Entire result table is written
- Use when: Interactive queries
- Highest latency and storage

## 8. Handling Late Data

### Event Time vs Processing Time
- **Event Time**: When event occurred (from data)
- **Processing Time**: When Spark processes event
- **Watermarking**: Allows late data handling

### Watermarks
```python
df.withWatermark("timestamp", "10 minutes") \
    .groupBy(window("timestamp", "5 minutes")) \
    .agg(sum("value"))
```

### Late Data Tolerance
- Events arriving after watermark are dropped in append mode
- Can be re-processed with update mode
- Configurable watermark delay

## 9. Fault Tolerance and Checkpointing

### Why Checkpointing Matters
- Ensures exactly-once processing semantics
- Allows recovery from failures
- Maintains state consistency

### Checkpoint Types
1. **WAL (Write-Ahead Logs)**
   - Records all operations
   - Fast write, slower reads

2. **Offset/State Checkpoints**
   - Source offsets
   - Operator state
   - Custom metrics

### Checkpoint Configuration
```python
query.writeStream \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start()
```

## 10. Stream-to-Stream Joins

### Inner Joins on Streaming DataFrames
Join two streams based on keys and window
```python
join_result = stream1.join(stream2, 
    [stream1.key == stream2.key, 
     stream1.event_time.between(stream2.event_time - interval("10 minutes"), stream2.event_time)])
```

### Stream-Static Table Joins
Enrich streaming data with static reference data
```python
enriched = streamDF.join(staticDF, "key", "left")
```

### Requirements
- Both streams must have watermarks
- Time bounds must be specified
- Window-based join semantics

## 11. Monitoring and Debugging

### Query Statistics
- Input rate (rows/sec)
- Processing rate (rows/sec)
- Batch duration
- Number of added/removed rows

### Common Issues
1. **Slow Processing**: High input rates vs low processing capacity
2. **State Size Growth**: Unbounded stateful operations
3. **Late Data**: Not handling watermark properly
4. **Inconsistent Results**: Wrong output mode

### Logging and Tracking
- StreamingQuery object provides status
- explain() shows execution plan
- Custom metrics via accumulator

## 12. Performance Tuning

### Optimization Strategies
1. **Batch Interval**: Balance latency vs throughput
2. **Parallelism**: Partition count and tasks
3. **State Size**: Limit state retention
4. **Shuffles**: Minimize repartitioning
5. **Memory**: Allocate sufficient memory

### Best Practices
- Use appropriate window sizes
- Apply filters early
- Monitor resource utilization
- Test with production data volumes
- Use delta lake for checkpointing

## Key Takeaways
1. Structured Streaming provides batch-like API for streaming
2. Understand sources, sinks, and transformations
3. Properly configure windows for time-based aggregations
4. Use watermarks for handling late data
5. Configure checkpointing for fault tolerance
6. Monitor and tune for production workloads
7. Choose appropriate output modes based on use case
