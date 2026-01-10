# Regression in PySpark MLlib

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression, RandomForestRegressor, GBTRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("Regression").getOrCreate()

# Create sample data (House price prediction)
data = [
    (2500, 4, 2, 500000),
    (1800, 3, 2, 350000),
    (3200, 5, 3, 600000),
    (1500, 2, 1, 250000),
    (2800, 4, 3, 550000),
    (2000, 3, 2, 400000),
    (3500, 5, 3, 700000),
    (1200, 2, 1, 200000),
]

df = spark.createDataFrame(data, ["sqft", "bedrooms", "bathrooms", "price"])

print("\n=== Dataset ===")
df.show()

# Prepare features
feature_cols = ["sqft", "bedrooms", "bathrooms"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df_features = assembler.transform(df)

# Split data
train_data, test_data = df_features.randomSplit([0.8, 0.2], seed=42)

print(f"Training samples: {train_data.count()}")
print(f"Testing samples: {test_data.count()}")

# 1. Linear Regression
print("\n=== Linear Regression ===")
lr = LinearRegression(featuresCol="features", labelCol="price", maxIter=10)
lr_model = lr.fit(train_data)
lr_predictions = lr_model.transform(test_data)

evaluator = RegressionEvaluator(labelCol="price", predictionCol="prediction", metricName="rmse")
lr_rmse = evaluator.evaluate(lr_predictions)
print(f"RMSE: ${lr_rmse:,.2f}")
print(f"R² Score: {lr_model.summary.r2:.4f}")

# 2. Random Forest Regressor
print("\n=== Random Forest Regressor ===")
rf = RandomForestRegressor(
    featuresCol="features",
    labelCol="price",
    numTrees=5,
    seed=42
)
rf_model = rf.fit(train_data)
rf_predictions = rf_model.transform(test_data)

rf_rmse = evaluator.evaluate(rf_predictions)
print(f"RMSE: ${rf_rmse:,.2f}")
print(f"\nFeature Importance:")
for i, importance in enumerate(rf_model.featureImportances):
    print(f"  Feature {i}: {importance:.4f}")

# 3. Gradient Boosted Trees Regressor
print("\n=== Gradient Boosted Trees Regressor ===")
gbt = GBTRegressor(
    featuresCol="features",
    labelCol="price",
    maxIter=5,
    seed=42
)
gbt_model = gbt.fit(train_data)
gbt_predictions = gbt_model.transform(test_data)

gbt_rmse = evaluator.evaluate(gbt_predictions)
print(f"RMSE: ${gbt_rmse:,.2f}")

# 4. Sample Predictions
print("\n=== Sample Predictions ===")
lr_predictions.select("price", "prediction", col("prediction" - col("price")).alias("error")).show(3)

# 5. Model Comparison
print("\n=== Model Comparison ===")
print(f"Linear Regression RMSE: ${lr_rmse:,.2f}")
print(f"Random Forest RMSE: ${rf_rmse:,.2f}")
print(f"Gradient Boosted Trees RMSE: ${gbt_rmse:,.2f}")
print(f"\nBest Model: {'Linear Regression' if lr_rmse <= min(rf_rmse, gbt_rmse) else 'Random Forest' if rf_rmse <= gbt_rmse else 'Gradient Boosted Trees'}")
print(f"Best RMSE: ${min(lr_rmse, rf_rmse, gbt_rmse):,.2f}")
