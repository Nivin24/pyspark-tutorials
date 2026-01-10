# 03_log_analysis.py
# Real-time Log Analysis System using PySpark
# Analyzes application logs for errors, patterns, and anomalies

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, split, from_unixtime, unix_timestamp, 
    when, count, window, substring_index, regexp_extract,
    avg, max, min, sum as spark_sum, lit, desc
)
from datetime import datetime, timedelta
import json

print("\n" + "="*70)
print("REAL-TIME LOG ANALYSIS SYSTEM")
print("="*70)

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("LogAnalysisSystem") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

print("\n[PHASE 1: LOADING LOG DATA]")
print("-" * 70)

# Generate sample log data
logs_data = [
    ("2024-01-15 10:05:23.123", "INFO", "user_service", "User login successful", "192.168.1.100"),
    ("2024-01-15 10:05:45.456", "ERROR", "payment_service", "Connection timeout", "192.168.1.101"),
    ("2024-01-15 10:06:12.789", "WARN", "cache_service", "Cache miss ratio high", "192.168.1.102"),
    ("2024-01-15 10:06:34.012", "ERROR", "database_service", "Query timeout after 30s", "192.168.1.101"),
    ("2024-01-15 10:07:01.345", "INFO", "user_service", "User logout", "192.168.1.100"),
    ("2024-01-15 10:07:23.678", "ERROR", "auth_service", "Authentication failed", "192.168.1.103"),
    ("2024-01-15 10:08:01.901", "WARN", "payment_service", "Retry attempt 2 of 3", "192.168.1.101"),
    ("2024-01-15 10:08:45.234", "ERROR", "cache_service", "Memory threshold exceeded", "192.168.1.102"),
    ("2024-01-15 10:09:12.567", "INFO", "database_service", "Connection pool restored", "192.168.1.104"),
    ("2024-01-15 10:10:01.890", "ERROR", "user_service", "Rate limit exceeded", "192.168.1.105"),
]

logs_df = spark.createDataFrame(
    logs_data,
    ["timestamp", "level", "service", "message", "ip_address"]
)

print("Logs loaded successfully!")
logs_df.show(5, truncate=False)

print("\n[PHASE 2: DATA PARSING & CLEANING]")
print("-" * 70)

# Parse timestamp and extract service info
parsed_logs = logs_df.withColumn(
    "parsed_timestamp", 
    from_unixtime(unix_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss.SSS"))
).withColumn(
    "hour",
    substring_index(col("timestamp"), " ", 1)
).withColumn(
    "time_part",
    substring_index(col("timestamp"), " ", -1)
).withColumn(
    "service_type",
    regexp_extract(col("service"), "^([a-z]+)", 1)
)

print("\nParsed and cleaned logs:")
parsed_logs.select("timestamp", "level", "service_type", "ip_address").show()

print("\n[PHASE 3: ERROR ANALYSIS]")
print("-" * 70)

# Count errors by service
error_df = parsed_logs.filter(col("level") == "ERROR")
error_counts = error_df.groupBy("service").agg(count("*").alias("error_count")).orderBy(desc("error_count"))

print("\nError count by service:")
error_counts.show(truncate=False)

total_errors = error_df.count()
total_logs = parsed_logs.count()
error_rate = (total_errors / total_logs) * 100

print(f"\nTotal logs: {total_logs}")
print(f"Total errors: {total_errors}")
print(f"Error rate: {error_rate:.2f}%")

print("\n[PHASE 4: IP & SERVICE ANALYSIS]")
print("-" * 70)

# Top problematic IPs
problematic_ips = parsed_logs.groupBy("ip_address") \
    .agg(
        count("*").alias("log_count"),
        sum(when(col("level") == "ERROR", 1).otherwise(0)).alias("error_count")
    ) \
    .withColumn("error_percentage", (col("error_count") / col("log_count") * 100).cast("decimal(5,2)")) \
    .orderBy(desc("error_count"))

print("\nProblematic IPs:")
problematic_ips.show(truncate=False)

print("\n[PHASE 5: LOG LEVEL DISTRIBUTION]")
print("-" * 70)

# Distribution by log level
level_distribution = parsed_logs.groupBy("level").agg(
    count("*").alias("count"),
    (count("*") * 100.0 / parsed_logs.count()).alias("percentage")
).orderBy(desc("count"))

print("\nLog level distribution:")
level_distribution.show(truncate=False)

print("\n[PHASE 6: ANOMALY DETECTION]")
print("-" * 70)

# Find unusual patterns
error_threshold = error_counts.agg(avg("error_count")).collect()[0][0]
anomalies = error_counts.filter(col("error_count") > error_threshold)

print(f"\nError threshold (average): {error_threshold:.2f}")
print("\nServices with anomalous error rates:")
anomalies.show(truncate=False)

print("\n[PHASE 7: MESSAGE PATTERN ANALYSIS]")
print("-" * 70)

# Extract error patterns from messages
error_patterns = error_df.withColumn(
    "error_type",
    when(col("message").contains("timeout"), "Timeout")
    .when(col("message").contains("exceeded"), "Threshold Exceeded")
    .when(col("message").contains("failed"), "Authentication Failed")
    .otherwise("Other")
)

error_pattern_counts = error_patterns.groupBy("error_type").agg(
    count("*").alias("count")
).orderBy(desc("count"))

print("\nError patterns identified:")
error_pattern_counts.show(truncate=False)

print("\n[PHASE 8: TIME-BASED ANALYSIS]")
print("-" * 70)

# Logs per hour
time_analysis = parsed_logs.groupBy("hour").agg(
    count("*").alias("total_logs"),
    sum(when(col("level") == "ERROR", 1).otherwise(0)).alias("errors")
).orderBy("hour")

print("\nActivity timeline:")
time_analysis.show(truncate=False)

print("\n[PHASE 9: CRITICAL INCIDENTS REPORT]")
print("-" * 70)

# Critical incidents (errors in critical services)
critical_services = ["payment_service", "database_service", "auth_service"]
critical_incidents = error_df.filter(col("service").isin(critical_services)).select(
    "timestamp", "service", "message", "ip_address"
).orderBy(col("timestamp").desc())

print(f"\nCritical incidents (services: {', '.join(critical_services)}):")
print(f"Total critical incidents: {critical_incidents.count()}")
critical_incidents.show(truncate=False)

print("\n[PHASE 10: SUMMARY STATISTICS]")
print("-" * 70)

summary_data = [
    ("Total Logs", total_logs),
    ("Total Errors", total_errors),
    ("Error Rate (%)", f"{error_rate:.2f}"),
    ("Unique Services", parsed_logs.select("service").distinct().count()),
    ("Unique IPs", parsed_logs.select("ip_address").distinct().count()),
    ("Critical Incidents", critical_incidents.count()),
]

summary_df = spark.createDataFrame(summary_data, ["Metric", "Value"])
print("\nSummary Statistics:")
summary_df.show(truncate=False)

print("\n" + "="*70)
print("LOG ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*70)
