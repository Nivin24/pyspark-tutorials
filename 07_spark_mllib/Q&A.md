# Machine Learning Q&A in PySpark

## Classification vs Regression

**Q: When should I use classification vs regression?**
A: Use classification when predicting categories (yes/no, 1-5 rating). Use regression when predicting continuous values (price, temperature).

## Model Selection

**Q: How do I choose between Logistic Regression, Random Forest, and GBT?**
A:
- Logistic Regression: Fast, interpretable, good for linear relationships
- Random Forest: Handles non-linear relationships, less prone to overfitting
- GBT: Most accurate but slowest, needs careful tuning

## Evaluation Metrics

**Q: What's the best evaluation metric for my model?**
A:
- Classification: Accuracy (balanced classes), Precision/Recall (imbalanced), F1-Score (balance), AUC (threshold-independent)
- Regression: RMSE (penalizes large errors), MAE (robust to outliers), R² (interpretability)

## Class Imbalance

**Q: How do I handle imbalanced datasets?**
A:
1. Use stratified sampling for train/test split
2. Use class weights
3. Oversample minority class
4. Undersample majority class
5. Change decision threshold
6. Use different metrics (F1, AUC instead of accuracy)

## Feature Engineering

**Q: How many features should my model have?**
A: Start with domain knowledge, use feature selection, and iterate. More features ≠ better models. Remove low-variance features and correlated features.

## Hyperparameter Tuning

**Q: How do I find the best hyperparameters?**
A:
- Start with default values
- Use GridSearchCV or random search
- Focus on key parameters (learning rate, regularization, depth)
- Use cross-validation for robust estimates

## Data Scaling

**Q: Do I need to scale features for tree-based models?**
A: No, tree-based models (Random Forest, GBT) are scale-invariant. Scale for distance-based (KNN) and gradient descent (Linear Regression, Neural Networks).

## Training Tips

**Q: My model is overfitting. What should I do?**
A:
1. Reduce model complexity
2. Add regularization (L1/L2)
3. Increase training data
4. Reduce features
5. Use early stopping
6. Increase dropout rate

**Q: My model is underfitting. What should I do?**
A:
1. Increase model complexity
2. Remove regularization
3. Add more features (feature engineering)
4. Train longer
5. Tune learning rate

## Clustering

**Q: How do I determine the optimal number of clusters k?**
A:
- Elbow method: Plot inertia vs k
- Silhouette score: Find k with highest score
- Domain knowledge: Consider business requirements

**Q: What's the difference between K-Means and GMM?**
A:
- K-Means: Hard assignments, faster, simpler
- GMM: Soft assignments (probabilities), more flexible, slower

## Recommendation Systems

**Q: How do I handle the cold-start problem?**
A:
1. Content-based filtering for new users
2. Recommend popular items
3. Ask for explicit ratings
4. Use side information (demographics, item features)

**Q: What's the difference between user-based and item-based CF?**
A:
- User-based: Find similar users
- Item-based: Find similar items
- ALS: Matrix factorization, latent factors

## Performance

**Q: How do I optimize training speed?**
A:
1. Use larger batch sizes
2. Reduce data size (sampling)
3. Use simpler models
4. Increase parallelism
5. Cache intermediate DataFrames
6. Use appropriate data types

## ML Pipelines

**Q: What's an ML pipeline?**
A: A sequence of transformers and estimators that processes data end-to-end, making workflows reproducible and maintainable.

## Production Deployment

**Q: How do I deploy a Spark ML model?**
A:
1. Save the model: `model.save(path)`
2. Load in production: `PipelineModel.load(path)`
3. Make predictions: `model.transform(data)`
4. Monitor performance
5. Retrain periodically

## Common Errors

**Q: Getting NaN values in predictions?**
A: Check for missing values, infinite values, or numerical instability. Use proper feature scaling and regularization.

**Q: Memory issues during training?**
A: Reduce batch size, use data sampling, increase executor memory, use simpler models.
