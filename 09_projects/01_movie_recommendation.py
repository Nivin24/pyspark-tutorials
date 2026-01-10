# Movie Recommendation System - Complete Project
# Build a collaborative filtering-based recommendation engine

from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col, avg, count

# Initialize Spark
spark = SparkSession.builder.appName("MovieRecommendation").getOrCreate()

# Load sample data (movies, ratings, users)
movies_data = [
    (1, "The Shawshank Redemption", "Drama"),
    (2, "The Dark Knight", "Action"),
    (3, "Inception", "Sci-Fi"),
    (4, "Titanic", "Romance"),
    (5, "Interstellar", "Sci-Fi"),
]

ratings_data = [
    (1, 1, 5.0),
    (1, 2, 4.0),
    (1, 3, 5.0),
    (2, 1, 5.0),
    (2, 2, 5.0),
    (2, 4, 3.0),
    (3, 2, 5.0),
    (3, 3, 4.0),
    (3, 5, 5.0),
    (4, 1, 3.0),
    (4, 4, 5.0),
    (4, 5, 4.0),
]

users_data = [
    (1, "Alice", "25-34"),
    (2, "Bob", "35-44"),
    (3, "Charlie", "18-24"),
    (4, "Diana", "45-54"),
]

# Create DataFrames
movies_df = spark.createDataFrame(movies_data, ["movieId", "title", "genre"])
ratings_df = spark.createDataFrame(ratings_data, ["userId", "movieId", "rating"])
users_df = spark.createDataFrame(users_data, ["userId", "name", "age_group"])

print("=" * 50)
print("MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

# 1. Exploratory Data Analysis
print("\n1. Dataset Overview")
print(f"Total Movies: {movies_df.count()}")
print(f"Total Ratings: {ratings_df.count()}")
print(f"Total Users: {users_df.count()}")

print("\nRating Statistics:")
ratings_df.describe().show()

# 2. Data Quality Checks
print("\n2. Data Quality Checks")
print(f"Missing values in ratings: {ratings_df.filter(col('rating').isNull()).count()}")
print(f"Rating range: {ratings_df.agg({'rating': 'min'}).collect()[0][0]} - {ratings_df.agg({'rating': 'max'}).collect()[0][0]}")

# 3. Build Recommendation Model
print("\n3. Building ALS Recommendation Model...")

# Split data
train_data, test_data = ratings_df.randomSplit([0.8, 0.2], seed=42)

# ALS Configuration
als = ALS(
    maxIter=10,
    regParam=0.01,
    userCol="userId",
    itemCol="movieId",
    ratingCol="rating",
    coldStartStrategy="drop",
    seed=42
)

# Train model
model = als.fit(train_data)
print("Model trained successfully!")

# 4. Make predictions
print("\n4. Making Predictions")
predictions = model.transform(test_data)
predictions.select("userId", "movieId", "rating", "prediction").show(5)

# 5. Evaluate Model
print("\n5. Model Evaluation")
evaluator = RegressionEvaluator(
    metricName="rmse",
    labelCol="rating",
    predictionCol="prediction"
)
rmse = evaluator.evaluate(predictions)
print(f"RMSE: {rmse:.4f}")

# 6. Generate Recommendations
print("\n6. Top Movie Recommendations for Each User")
user_recs = model.recommendForAllUsers(3)
user_recs.show(truncate=False)

print("\n7. Top Users for Each Movie")
movie_recs = model.recommendForAllItems(2)
movie_recs.show(truncate=False)

# 8. Get recommendations for specific user
print("\n8. Personalized Recommendations for User 1")
user1_recs = model.recommendForUserSubset(spark.createDataFrame([(1,)], ["userId"]), 3)
user1_recs.select("userId", "recommendations").show(truncate=False)

print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 50)
