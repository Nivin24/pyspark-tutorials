# AWS EMR (Elastic MapReduce) Integration
# Deploy and run Spark jobs on Amazon Web Services

import boto3
import json
from botocore.exceptions import ClientError

# Configuration
region = "us-east-1"
cluster_name = "pyspark-emr-cluster"
job_flow_role = "EMR_EC2_DefaultRole"
service_role = "EMR_DefaultRole"
instance_count = 3
instance_type = "m5.xlarge"

# 1. Create an EMR Cluster
def create_emr_cluster():
    """
    Create an EMR cluster with Spark
    """
    client = boto3.client("emr", region_name=region)
    
    response = client.run_job_flow(
        Name=cluster_name,
        ReleaseLabel="emr-6.9.0",  # Spark 3.1
        Instances={
            "InstanceGroups": [
                {
                    "Name": "Master",
                    "Market": "ON_DEMAND",
                    "InstanceRole": "MASTER",
                    "InstanceType": instance_type,
                    "InstanceCount": 1,
                },
                {
                    "Name": "Worker",
                    "Market": "SPOT",  # Use spot instances for cost savings
                    "InstanceRole": "CORE",
                    "InstanceType": instance_type,
                    "InstanceCount": instance_count - 1,
                },
            ],
            "Ec2SubnetId": "subnet-xxxxxxxx",  # Your subnet ID
        },
        ServiceRole=service_role,
        JobFlowRole=job_flow_role,
        Applications=[
            {"Name": "Spark"},
            {"Name": "Hadoop"},
            {"Name": "Hive"},
        ],
        Configurations=[
            {
                "Classification": "spark",
                "Properties": {
                    "maximizeResourceAllocation": "true"
                },
            }
        ],
        LogUri="s3://your-bucket/logs/",
        StepConcurrencyLevel=2,
    )
    
    cluster_id = response["JobFlowId"]
    print(f"Created EMR cluster: {cluster_id}")
    return cluster_id

# 2. Submit a Spark Job
def submit_spark_step(cluster_id, script_path):
    """
    Submit a PySpark step to EMR cluster
    """
    client = boto3.client("emr", region_name=region)
    
    response = client.add_job_flow_steps(
        JobFlowId=cluster_id,
        Steps=[
            {
                "Name": "Spark Job",
                "ActionOnFailure": "TERMINATE_CLUSTER",
                "HadoopJarStep": {
                    "Jar": "command-runner.jar",
                    "Args": [
                        "spark-submit",
                        "--deploy-mode",
                        "cluster",
                        "--master",
                        "yarn",
                        f"s3://your-bucket/{script_path}",
                    ],
                },
            }
        ],
    )
    
    step_id = response["StepIds"][0]
    print(f"Submitted step: {step_id}")
    return step_id

# 3. Read data from S3
def read_from_s3(bucket, key):
    """
    Read data from S3 into Spark DataFrame
    """
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.appName("S3-Reader").getOrCreate()
    
    # Configure S3 access
    spark.sparkContext.hadoopConfiguration.set(
        "fs.s3a.aws.credentials.provider",
        "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
    )
    
    # Read from S3
    df = spark.read.parquet(f"s3a://{bucket}/{key}")
    return df

# 4. Write data to S3
def write_to_s3(df, bucket, key):
    """
    Write DataFrame to S3
    """
    df.write.mode("overwrite").parquet(f"s3a://{bucket}/{key}")
    print(f"Data written to s3a://{bucket}/{key}")

# 5. Describe cluster
def describe_cluster(cluster_id):
    """
    Get cluster information
    """
    client = boto3.client("emr", region_name=region)
    
    response = client.describe_cluster(ClusterId=cluster_id)
    cluster = response["Cluster"]
    
    print(f"Cluster Name: {cluster['Name']}")
    print(f"Status: {cluster['Status']['State']}")
    print(f"Master: {cluster.get('MasterPublicDNSName', 'N/A')}")
    print(f"Spark Version: {cluster.get('ReleaseLabel', 'N/A')}")
    
    return cluster

# 6. Terminate cluster
def terminate_cluster(cluster_id):
    """
    Terminate the EMR cluster
    """
    client = boto3.client("emr", region_name=region)
    
    response = client.terminate_job_flows(JobFlowIds=[cluster_id])
    print(f"Terminated cluster: {cluster_id}")
    return response

# Main workflow
if __name__ == "__main__":
    print("=== AWS EMR Integration ===")
    print(f"Region: {region}")
    print(f"Cluster: {cluster_name}")
    
    # Create cluster
    # cluster_id = create_emr_cluster()
    
    # Describe cluster
    # describe_cluster(cluster_id)
    
    # Submit job
    # submit_spark_step(cluster_id, "scripts/analysis.py")
    
    # Terminate cluster
    # terminate_cluster(cluster_id)
