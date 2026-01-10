# Classification in PySpark MLlib

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
from pyspark.ml import Pipeline
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("Classification").getOrCreate()

# Create sample data (Customer churn prediction)
data = [
    ("Alice", 5, 50, 150.0, 0),
    ("Bob", 2, 35, 80.0, 1),
    ("Charlie", 7, 28, 200.0, 0),
    ("Diana", 1, 45, 60.0, 1),
    ("Eve", 4, 32, 120.0, 0),
    ("Frank", 8, 55, 250.0, 0),
    ("Grace", 3, 42, 90.0, 1),
    ("Henry", 6, 38, 180.0, 0),
]

df = spark.createDataFrame(data, ["name", "months_active", "age", "monthly_charges", "churn"])

print("\n=== Dataset ===")
df.show()

# Prepare features
feature_cols = ["months_active", "age", "monthly_charges"]
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df_features = assembler.transform(df.select(feature_cols + ["churn"]))

print("\n=== Features ===")
df_features.select("features", "churn").show()

# Split data
train_data, test_data = df_features.randomSplit([0.8, 0.2], seed=42)

print(f"Training samples: {train_data.count()}")
print(f"Testing samples: {test_data.count()}")

# 1. Logistic Regression
print("\n=== Logistic Regression ===")
lr = LogisticRegression(featuresCol="features", labelCol="churn", maxIter=10)
lr_model = lr.fit(train_data)
lr_predictions = lr_model.transform(test_data)

evaluator = BinaryClassificationEvaluator(labelCol="churn", rawPredictionCol="rawPrediction")
lr_auc = evaluator.evaluate(lr_predictions)
print(f"AUC: {lr_auc:.4f}")

# 2. Random Forest
print("\n=== Random Forest ===")
rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="churn",
    numTrees=10,
    seed=42
)
rf_model = rf.fit(train_data)
rf_predictions = rf_model.transform(test_data)

rf_auc = evaluator.evaluate(rf_predictions)
print(f"AUC: {rf_auc:.4f}")
print(f"\nFeature Importance:")
for i, importance in enumerate(rf_model.featureImportances):
    print(f"  Feature {i}: {importance:.4f}")

# 3. Gradient Boosted Trees
print("\n=== Gradient Boosted Trees ===")
gbt = GBTClassifier(
    featuresCol="features",
    labelCol="churn",
    maxIter=10,
    seed=42
)
gbt_model = gbt.fit(train_data)
gbt_predictions = gbt_model.transform(test_data)

gbt_auc = evaluator.evaluate(gbt_predictions)
print(f"AUC: {gbt_auc:.4f}")

# 4. Predictions
print("\n=== Sample Predictions ===")
lr_predictions.select("churn", "probability", "prediction").show(3, truncate=False)

# 5. Feature Importance
print("\n=== Model Comparison ===")
print(f"Logistic Regression AUC: {lr_auc:.4f}")
print(f"Random Forest AUC: {rf_auc:.4f}")
print(f"Gradient Boosted Trees AUC: {gbt_auc:.4f}")

print("\n=== Classification Metrics ===")
print(f"Best Model: {'Random Forest' if rf_auc >= lr_auc and rf_auc >= gbt_auc else 'Gradient Boosted Trees' if gbt_auc >= lr_auc else 'Logistic Regression'}")
print(f"Best AUC: {max(lr_auc, rf_auc, gbt_auc):.4f}")
