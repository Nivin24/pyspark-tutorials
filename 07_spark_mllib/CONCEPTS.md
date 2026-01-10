# Machine Learning Concepts in PySpark MLlib

## Classification
Classification predicts discrete categories. Algorithms include:
- **Logistic Regression**: Binary/multiclass classification, probability outputs
- **Random Forest**: Ensemble method, handles non-linear relationships
- **Gradient Boosted Trees**: Sequential tree building, high accuracy
- **Naive Bayes**: Probabilistic classifier based on Bayes' theorem
- **Support Vector Machines**: Linear and nonlinear classification

### Key Metrics:
- **Accuracy**: Correct predictions / Total predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Area under the ROC curve

## Regression
Regression predicts continuous values. Algorithms include:
- **Linear Regression**: Simple, interpretable, assumes linear relationship
- **Ridge/Lasso Regression**: Adds regularization to prevent overfitting
- **Random Forest Regressor**: Ensemble of decision trees
- **Gradient Boosted Trees Regressor**: Sequential boosting for regression

### Key Metrics:
- **RMSE**: Root Mean Squared Error
- **MAE**: Mean Absolute Error
- **R² Score**: Proportion of variance explained (0-1)
- **MAPE**: Mean Absolute Percentage Error

## Clustering
Clustering groups similar data points. Algorithms include:
- **K-Means**: Partitions data into k clusters, minimizes within-cluster variance
- **Gaussian Mixture Model**: Probabilistic approach, soft assignments
- **Hierarchical Clustering**: Creates dendrogram of clusters
- **DBSCAN**: Density-based, finds arbitrary shaped clusters

### Evaluation:
- **Silhouette Score**: Measures cluster cohesion and separation (-1 to 1)
- **Davies-Bouldin Index**: Ratio of within to between cluster distances
- **Elbow Method**: Find optimal k by plotting inertia vs k

## Recommendation Systems
Recommendation predicts user preferences. Approaches include:
- **Collaborative Filtering**: ALS - uses matrix factorization
- **Content-Based**: Recommends based on item features
- **Hybrid**: Combines multiple approaches

### Key Concepts:
- **Latent Factors**: Hidden representations of users and items
- **Cold-Start Problem**: New users/items with no history
- **Sparsity**: Most user-item interactions are unknown

## Model Evaluation

### Training/Testing Split:
- Train on 70-80% of data
- Test on remaining 20-30%
- Use stratified sampling for imbalanced data

### Cross-Validation:
- K-fold cross-validation (k=5 or 10)
- Reduces variance in performance estimates
- More robust than single train/test split

### Hyperparameter Tuning:
- Grid Search: Test all combinations
- Random Search: Sample random combinations
- Bayesian Optimization: Use probabilistic model

## Common Challenges

### Overfitting
Model learns training data too well:
- Reduce model complexity
- Increase training data
- Use regularization
- Early stopping

### Underfitting
Model too simple:
- Increase model complexity
- Reduce regularization
- Feature engineering
- More training iterations

### Class Imbalance
Different class distributions:
- Oversample minority class
- Undersample majority class
- Use class weights
- Adjust decision threshold

### Data Quality
- Handle missing values
- Remove duplicates
- Detect outliers
- Validate assumptions

## Best Practices

1. **Exploratory Data Analysis**: Understand data distribution
2. **Feature Engineering**: Create meaningful features
3. **Cross-Validation**: Robust performance estimates
4. **Regularization**: Prevent overfitting
5. **Monitoring**: Track metrics on validation data
6. **Documentation**: Record decisions and assumptions
7. **Reproducibility**: Use seeds for randomization
8. **Interpretability**: Understand model decisions

## MLlib Pipeline

ML pipelines chain transformers and estimators:
1. Transformers: Feature scaling, encoding
2. Estimators: Models that learn from data
3. Evaluators: Assess model performance
4. Hyperparameter Tuning: Find best parameters

## References
- MLlib Documentation
- Spark ML Guide
- Machine Learning Fundamentals
