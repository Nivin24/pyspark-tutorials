# Recommendation Systems in PySpark MLlib

from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("Recommendation").getOrCreate()

# Create sample data (Movie ratings)
data = [
    (1, 1, 5),    # User 1 rated Movie 1 as 5
    (1, 2, 3),    # User 1 rated Movie 2 as 3
    (1, 3, 4),
    (2, 1, 4),    # User 2 rated Movie 1 as 4
    (2, 2, 5),
    (2, 3, 2),
    (3, 1, 2),    # User 3 rated Movie 1 as 2
    (3, 2, 4),
    (3, 3, 5),
    (4, 1, 5),
    (4, 2, 2),
    (4, 3, 3),
]

df = spark.createDataFrame(data, ["userId", "movieId", "rating"])

print("\n=== Rating Data ===")
df.show()
df.describe().show()

# Split data
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

print(f"\nTraining samples: {train_data.count()}")
print(f"Testing samples: {test_data.count()}")

# ALS (Alternating Least Squares) for Collaborative Filtering
print("\n=== ALS Collaborative Filtering ===")
als = ALS(
    userCol="userId",
    itemCol="movieId",
    ratingCol="rating",
    numBlocks=1,
    rank=10,
    maxIter=10,
    regParam=0.01,
    coldStartStrategy="drop"
)

als_model = als.fit(train_data)
als_predictions = als_model.transform(test_data)

print("\nPredictions:")
als_predictions.select("userId", "movieId", "rating", "prediction").show()

# Evaluate recommendations
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating",
    predictionCol="prediction"
)

rmse = evaluator.evaluate(als_predictions)
print(f"\nRMSE: {rmse:.4f}")

# Generate top-k recommendations
print("\n=== Top 2 Movies for Each User ===")
userRecs = als_model.recommendForAllUsers(2)
print("\nUser Recommendations:")
userRecs.show(truncate=False)

# Generate top-k recommendations for all movies
print("\n=== Top 2 Users for Each Movie ===")
moviewRecs = als_model.recommendForAllItems(2)
print("\nMovie Recommendations:")
moviewRecs.show(truncate=False)

# User factors and item factors
print("\n=== Model Components ===")
print("User Factors:")
als_model.userFactors.show(truncate=False)
print("\nMovie Factors:")
als_model.itemFactors.show(truncate=False)

print(f"\n=== Summary ===")
print(f"Number of Users: {als_model.userFactors.count()}")
print(f"Number of Movies: {als_model.itemFactors.count()}")
print(f"Rank: {als_model.rank}")
print(f"Test RMSE: {rmse:.4f}")
