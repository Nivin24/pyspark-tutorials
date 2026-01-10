# Phase 7: Machine Learning with Spark MLlib

## Overview
SparkML is PySpark's scalable machine learning library for building and deploying ML pipelines on distributed data.

## Learning Objectives
- Build classification, regression, clustering models
- Implement recommendation systems
- Evaluate and tune ML models
- Deploy ML pipelines in production

## Module Files

### 1. **01_classification.py**
Multi-class classification using:
- Logistic Regression
- Random Forest Classifier
- Gradient Boosted Trees

Use cases: Spam detection, sentiment analysis, customer churn prediction

### 2. **02_regression.py**
Continuous value prediction with:
- Linear Regression
- Random Forest Regressor
- Gradient Boosted Trees Regressor

Use cases: Price prediction, sales forecasting, trend analysis

### 3. **03_clustering.py**
Unsupervised grouping using:
- K-Means Clustering
- Bisecting K-Means
- Gaussian Mixture Models

Use cases: Customer segmentation, document clustering, anomaly detection

### 4. **04_recommendation.py**
Collaborative filtering using:
- Alternating Least Squares (ALS)

Use cases: Movie recommendations, product suggestions, personalized content

## Running Examples

```bash
python 01_classification.py
python 02_regression.py
python 03_clustering.py
python 04_recommendation.py
```

## Key Concepts

### Model Development Pipeline
1. Data Preparation
2. Feature Engineering
3. Model Training
4. Evaluation
5. Hyperparameter Tuning
6. Deployment

### Important Metrics
- **Classification**: Accuracy, Precision, Recall, F1, AUC
- **Regression**: RMSE, MAE, R² Score
- **Clustering**: Silhouette Score, Davies-Bouldin Index

## Best Practices

✅ Always use train/test split (70/30 or 80/20)
✅ Use cross-validation for robust estimates
✅ Scale features when using distance-based algorithms
✅ Handle class imbalance appropriately
✅ Monitor both training and test metrics
✅ Document all decisions and assumptions
✅ Use ML pipelines for reproducibility

## Next Steps

- Explore 08_cloud_integration for deployment
- Build real projects in 09_projects
- Apply to your own datasets

## Resources

- See CONCEPTS.md for detailed explanations
- See Q&A.md for common questions
- PySpark MLlib Documentation
- Machine Learning Mastery Blog
