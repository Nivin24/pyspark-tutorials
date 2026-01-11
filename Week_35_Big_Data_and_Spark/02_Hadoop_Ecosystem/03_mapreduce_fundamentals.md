# MapReduce Fundamentals

## 1. What is MapReduce?

MapReduce is a programming model and execution framework for processing large datasets in parallel across a cluster of machines [web:20][web:31]. It divides work into:

- A **map** phase that processes input data and emits intermediate key–value pairs.
- A **reduce** phase that aggregates intermediate values by key and produces final results.

MapReduce runs on top of HDFS and uses YARN for resource management in modern Hadoop versions [web:8][web:25].

## 2. Logical data flow

High-level phases:

1. **Input splitting**:
   - Input files in HDFS are split into logical input splits (often aligned with HDFS blocks).
2. **Map phase**:
   - Each map task processes one split and emits intermediate key–value pairs.
3. **Shuffle and sort**:
   - Intermediate data is grouped by key; data is transferred across nodes so that all values for a key go to the same reducer [web:20].
4. **Reduce phase**:
   - Each reduce task processes all values for a key and outputs a final result.

This model enables scalable batch processing on very large datasets.

## 3. WordCount example (conceptual)

WordCount is the classic example:

- **Map**:
  - Input: lines of text.
  - Output: `(word, 1)` for each word.
- **Reduce**:
  - Input: `(word, [1, 1, 1, ...])`.
  - Output: `(word, total_count)`.

Even this simple job demonstrates parallelism (many mappers and reducers) and the shuffle step to group words [web:20][web:31].

## 4. Strengths and limitations

Strengths:

- Scales to very large datasets (TBs–PBs).
- Fault tolerant via task re-execution and reliance on HDFS.
- Suitable for large batch ETL and analytics jobs [web:20][web:28].

Limitations:

- High latency; jobs can be slow to start and complete, especially for small queries.
- Programming can be verbose and low-level.
- Multiple MapReduce stages may be required for complex workflows.

These limitations motivated higher-level tools (Pig, Hive) and more efficient engines like Spark, which you will study later [web:26][web:6].

## 5. Relationship with YARN

In Hadoop 2.x and later:

- MapReduce jobs are executed as YARN applications.
- YARN handles resource allocation and scheduling, while MapReduce implements the data processing logic [web:12][web:25].

Understanding this separation is important before learning Spark’s own execution model.
