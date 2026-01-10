# Google Cloud Dataproc Integration
# Deploy and run Spark jobs on Google Cloud Platform

import subprocess
import json
from google.cloud import dataproc_v1
from google.cloud import storage

# Configuration
project_id = "your-project-id"
region = "us-central1"
cluster_name = "pyspark-cluster"
zone = "us-central1-a"

# 1. Create a Dataproc Cluster
def create_dataproc_cluster():
    """
    Create a Dataproc cluster
    """
    cluster_client = dataproc_v1.ClusterControllerClient(
        credentials=None,  # Use default credentials
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com"}
    )
    
    cluster_config = {
        "master_config": {"num_instances": 1, "machine_type_uri": "n1-standard-4"},
        "worker_config": {"num_instances": 2, "machine_type_uri": "n1-standard-4"},
    }
    
    cluster = {
        "project_id": project_id,
        "cluster_name": cluster_name,
        "config": cluster_config,
    }
    
    operation = cluster_client.create_cluster(
        request={
            "project_id": project_id,
            "region": region,
            "cluster": cluster,
        }
    )
    
    print(f"Creating cluster {cluster_name}...")
    result = operation.result()
    print(f"Cluster created: {result.cluster_name}")
    return result

# 2. Submit a Spark Job
def submit_spark_job(bucket_name, script_path):
    """
    Submit a PySpark job to Dataproc
    """
    job_client = dataproc_v1.JobControllerClient(
        credentials=None,
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com"}
    )
    
    job_config = {
        "placement": {"cluster_name": cluster_name},
        "pyspark_job": {
            "main_python_file_uri": f"gs://{bucket_name}/{script_path}",
        },
    }
    
    operation = job_client.submit_job(
        request={
            "project_id": project_id,
            "region": region,
            "job": job_config,
        }
    )
    
    print(f"Submitting job...")
    result = operation.result()
    print(f"Job completed: {result.reference.job_id}")
    return result

# 3. Read data from Cloud Storage
def read_from_gcs(bucket_name, file_path):
    """
    Read data from Google Cloud Storage
    """
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("GCS-Reader").getOrCreate()
    
    # Configure GCS access
    spark.conf.set("google.cloud.auth.type", "APPLICATION_DEFAULT")
    
    # Read from GCS
    df = spark.read.parquet(f"gs://{bucket_name}/{file_path}")
    return df

# 4. Write data to Cloud Storage
def write_to_gcs(df, bucket_name, output_path):
    """
    Write DataFrame to Google Cloud Storage
    """
    df.write.mode("overwrite").parquet(f"gs://{bucket_name}/{output_path}")
    print(f"Data written to gs://{bucket_name}/{output_path}")

# 5. Delete the cluster
def delete_dataproc_cluster():
    """
    Delete the Dataproc cluster
    """
    cluster_client = dataproc_v1.ClusterControllerClient(
        credentials=None,
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com"}
    )
    
    operation = cluster_client.delete_cluster(
        request={
            "project_id": project_id,
            "region": region,
            "cluster_name": cluster_name,
        }
    )
    
    print(f"Deleting cluster {cluster_name}...")
    result = operation.result()
    print(f"Cluster deleted")
    return result

# Main workflow
if __name__ == "__main__":
    print("=== Google Cloud Dataproc Integration ===")
    print(f"Project: {project_id}")
    print(f"Region: {region}")
    print(f"Cluster: {cluster_name}")
    
    # Uncomment to create cluster
    # create_dataproc_cluster()
    
    # Submit job
    # submit_spark_job("your-bucket", "scripts/analysis.py")
    
    # Uncomment to delete cluster
    # delete_dataproc_cluster()
