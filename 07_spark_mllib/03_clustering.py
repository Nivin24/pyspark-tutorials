# Clustering in PySpark MLlib

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans, GaussianMixture, BisectingKMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Initialize Spark Session
spark = SparkSession.builder.appName("Clustering").getOrCreate()

# Create sample data (Customer segmentation)
data = [
    (30, 50000, 100),  # Young, low income, low spending
    (25, 45000, 80),
    (28, 48000, 90),
    (45, 120000, 500),  # Middle-age, high income, high spending
    (50, 130000, 600),
    (48, 115000, 480),
    (35, 80000, 300),  # Middle-age, medium income, medium spending
    (38, 85000, 350),
    (32, 75000, 280),
]

df = spark.createDataFrame(data, ["age", "income", "spending"])

print("\n=== Dataset ===")
df.show()
df.describe().show()

# Prepare features
feature_cols = ["age", "income", "spending"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df_features = assembler.transform(df)

print("\n=== Features ===")
df_features.select("features").show(truncate=False)

# 1. K-Means Clustering
print("\n=== K-Means Clustering ===")
kmeans = KMeans(k=3, seed=42, maxIter=20)
kmeans_model = kmeans.fit(df_features)
kmeans_predictions = kmeans_model.transform(df_features)

print("K-Means Centers:")
for i, center in enumerate(kmeans_model.clusterCenters()):
    print(f"  Cluster {i}: {center}")

print("\nCluster Assignments:")
kmeans_predictions.select("age", "income", "spending", "prediction").show()

# 2. Bisecting K-Means
print("\n=== Bisecting K-Means ===")
bisect = BisectingKMeans(k=3, seed=42)
bisect_model = bisect.fit(df_features)
bisect_predictions = bisect_model.transform(df_features)

print("Bisecting K-Means Centers:")
for i, center in enumerate(bisect_model.clusterCenters()):
    print(f"  Cluster {i}: {center}")

# 3. Gaussian Mixture Model
print("\n=== Gaussian Mixture Model ===")
gmm = GaussianMixture(k=3, seed=42, maxIter=50)
gmm_model = gmm.fit(df_features)
gmm_predictions = gmm_model.transform(df_features)

print("GMM Cluster Assignments:")
gmm_predictions.select("age", "income", "spending", "prediction").show()

# 4. Clustering Evaluation
print("\n=== Clustering Evaluation ===")
evaluator = ClusteringEvaluator(
    predictionCol="prediction",
    featuresCol="features",
    metricName="silhouette"
)

kmeans_silhouette = evaluator.evaluate(kmeans_predictions)
bisect_silhouette = evaluator.evaluate(bisect_predictions)
gmm_silhouette = evaluator.evaluate(gmm_predictions)

print(f"K-Means Silhouette Score: {kmeans_silhouette:.4f}")
print(f"Bisecting K-Means Silhouette Score: {bisect_silhouette:.4f}")
print(f"Gaussian Mixture Model Silhouette Score: {gmm_silhouette:.4f}")

print("\n=== Cluster Distribution ===")
print("K-Means Cluster Sizes:")
kmeans_predictions.groupBy("prediction").count().show()
print("\nGaussian Mixture Model Cluster Sizes:")
gmm_predictions.groupBy("prediction").count().show()
