# Spark Structured Streaming - Questions and Answers

## Beginner Level Questions

### Q1: What is Apache Spark Structured Streaming?
A: Apache Spark Structured Streaming is a stream processing API built on top of Apache Spark that allows developers to write streaming applications using the same DataFrame/SQL API used for batch processing. It provides scalable, fault-tolerant stream processing with exactly-once semantics.

### Q2: How is Structured Streaming different from DStream?
A: Structured Streaming uses DataFrames and SQL while DStream uses RDDs. Structured Streaming has better performance, simpler API, easier integration with batch processing, and supports SQL queries directly on streams.

### Q3: What are the main components of a Structured Streaming application?
A: The main components are:
1. **Source**: Where data comes from (Kafka, Socket, File, etc.)
2. **Transformations**: Operations on the stream (map, filter, groupBy, etc.)
3. **Sink**: Where data goes (Console, Parquet, Kafka, etc.)
4. **Query**: The execution of the streaming computation

### Q4: What does "micro-batching" mean?
A: Micro-batching divides the incoming stream into small batches and processes each batch as a separate Spark job. This allows for high throughput while maintaining the DataFrame API.

### Q5: What is the difference between streaming and batch processing?
A: Batch processing processes all data at once while streaming processes data continuously as it arrives. Streaming has lower latency, handles unbounded data, and is event-driven.

### Q6: Can you mix batch and streaming DataFrames?
A: Yes, you can join streaming DataFrames with static/batch DataFrames. This is useful for enriching stream data with reference tables.

### Q7: What are the common sources for Structured Streaming?
A: Common sources include Kafka, Socket, Files, Rate (for testing), Kinesis, Pubsub, and JDBC.

### Q8: What are the common sinks for Structured Streaming?
A: Common sinks include Console, Parquet, JSON, CSV, Kafka, Foreach, Memory, and Delta Lake.

### Q9: What is the default output mode?
A: The default output mode is "Append", which only writes new rows in the result table.

### Q10: What does "Exactly-once processing" mean?
A: It means each record is processed exactly once, even in case of failures. This is achieved through checkpointing and idempotent writes.

## Intermediate Level Questions

### Q11: What is the purpose of a watermark in Structured Streaming?
A: A watermark allows the system to automatically drop state about old data that is not expected to arrive. It defines how late the engine expects data to arrive.

### Q12: How do you define a watermark in Spark Structured Streaming?
A: Using the withWatermark function:
```python
df.withWatermark("timestamp", "10 minutes").groupBy(window("timestamp", "5 minutes")).agg(sum("value"))
```

### Q13: What are the three output modes in Structured Streaming?
A:
1. **Append**: Only new rows are written (default)
2. **Update**: Modified rows are written
3. **Complete**: Entire result table is written

### Q14: When should you use Complete mode?
A: Use Complete mode when:
- You need the entire aggregation result
- The result set is small
- Interactive queries are required
- You can afford the storage overhead

### Q15: What is the difference between Event Time and Processing Time?
A: Event Time is when the event actually occurred (in the data), while Processing Time is when Spark processes the event.

### Q16: How do you handle late-arriving data in Structured Streaming?
A: Using watermarks with withWatermark() to define the allowed lateness period. Data arriving after the watermark can be processed with Update mode.

### Q17: What is a stateful operation in Structured Streaming?
A: An operation that maintains state from previous rows. Examples include aggregations, windowing, and custom state updates.

### Q18: What is checkpointing in Structured Streaming?
A: Checkpointing saves the current state and offsets to a reliable storage. It allows recovery from failures and enables exactly-once processing semantics.

### Q19: How do you configure checkpointing?
A: By specifying the checkpointLocation option:
```python
query = streamDF.writeStream \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start()
```

### Q20: What are window operations in Structured Streaming?
A: Window operations group data based on time windows. Common types are tumbling (fixed-size), sliding (overlapping), and session windows.

## Advanced Level Questions

### Q21: What are the different types of window operations?
A:
1. **Tumbling Window**: Fixed-size, non-overlapping windows
2. **Sliding Window**: Overlapping windows based on slide interval
3. **Session Window**: Groups events by inactivity period

### Q22: How do you perform stream-to-stream joins?
A: Using join with time-based conditions and watermarks:
```python
joined = stream1.join(stream2, [stream1.key == stream2.key, 
    stream1.ts.between(stream2.ts - interval("10 minutes"), stream2.ts)])
```

### Q23: What is the difference between Append and Update modes?
A: Append mode writes only new rows, while Update mode writes modified rows. Append is suitable for append-only operations, Update for aggregations.

### Q24: How do you implement custom state management?
A: Using flatMapGroupsWithState() or mapGroupsWithState() for advanced state operations.

### Q25: What are the limitations of continuous processing mode?
A: Limited transformation support, cannot use multiple aggregations or joins in the same query, and only supports specific output formats.

### Q26: How do you monitor a Structured Streaming query?
A: Using StreamingQuery methods like status(), recentProgress, and lastProgress to monitor metrics like input rate, processing rate, and batch duration.

### Q27: What are common performance bottlenecks in Structured Streaming?
A: High shuffle operations, unbounded state growth, inefficient watermarking, insufficient memory, and slow sink operations.

### Q28: How do you optimize windowed aggregations?
A: Use appropriate window sizes, enable state cleanup with TTL, apply filters early, and partition data efficiently.

### Q29: What is idempotent writing in Spark Structured Streaming?
A: Writing data in a way that produces the same result regardless of how many times the operation is executed, crucial for exactly-once semantics.

### Q30: How do you integrate Spark Structured Streaming with machine learning?
A: Pre-trained ML models can be applied to streaming DataFrames using the same transformation APIs as batch processing.

### Q31: What is State TTL in Structured Streaming?
A: Time To Live (TTL) automatically removes state entries that haven't been updated for a specified duration, preventing unbounded state growth.

### Q32: How do you handle schema evolution in Structured Streaming?
A: Using Delta Lake with schema evolution enabled, or by catching exceptions and validating schema compatibility.

### Q33: What is the difference between once and availableNow triggers?
A: Once executes a single micro-batch, while availableNow processes all available data then stops.

### Q34: How do you test Structured Streaming applications?
A: Using Memory sink for output, Rate source for input, and unit tests with small batch intervals.

### Q35: What are best practices for production Structured Streaming?
A: Use checkpointing, implement proper monitoring, configure appropriate watermarks, use idempotent sinks, enable state cleanup, and plan for scalability.
