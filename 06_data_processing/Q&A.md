# Data Processing - Frequently Asked Questions

## Data Cleaning

### Q1: When should I drop rows vs. fill missing values?
**A:** Drop rows when:
- Missing values are < 5% of data
- Missing data is random (MCAR)
- Records are not critical

Fill missing values when:
- Missing percentage is 5-30%
- Data has patterns (MAR/MNAR)
- You want to preserve sample size

### Q2: How do I detect and remove duplicate rows efficiently?
**A:** Use `dropDuplicates()` for all columns or specify key columns:
```python
df.dropDuplicates()  # Remove complete duplicates
df.dropDuplicates(["id", "date"])  # Remove duplicates on specific columns
```

### Q3: What's the difference between null and NaN in Spark?
**A:**
- **null**: Database NULL value (missing data)
- **NaN**: "Not a Number" (mathematical undefined, only for floats)
- Use `isNull()` for null checks
- Use both `isNull()` and `isnan()` for complete validation

## Data Transformation

### Q4: How do I handle string splitting efficiently?
**A:** Use `split()` function with array indexing:
```python
df.select(
    split(col("name"), " ").getItem(0).alias("first_name")
)
```

### Q5: When should I use conditional logic (when) vs. separate columns?
**A:** Use `when()` when:
- Creating categorical features from numerical data
- Business logic is complex
- Want to reduce column count

Create separate columns when:
- Each condition produces independent features
- Downstream models need explicit features

### Q6: How do I create efficient transformation pipelines?
**A:**
1. Validate schema early
2. Filter unnecessary data before transformations
3. Avoid repeated similar transformations
4. Cache intermediate DataFrames if reused
5. Use `select()` to keep only needed columns

## Feature Engineering

### Q7: What's the best scaling method for features?
**A:**
- **Min-Max Scaling**: When you know data bounds, for [0,1] range
- **Z-Score Normalization**: When data is normally distributed
- **Robust Scaling**: When data has outliers
- **Log Scaling**: For skewed distributions

### Q8: How do I handle categorical variables for ML models?
**A:**
- **Binary Categories**: One-hot encoding (2 classes)
- **Multiple Categories**: One-hot or label encoding
- **Ordinal Data**: Label encoding preserves order
- **High Cardinality**: Target encoding or frequency encoding

### Q9: When should I create interaction features?
**A:** Create interactions when:
- Domain knowledge suggests relationships
- Exploratory analysis shows patterns
- Features are conditionally dependent
- Avoid overfitting with too many interactions

### Q10: How do I prevent data leakage in feature engineering?
**A:**
- Fit transformations on train data only
- Never use future information for predictions
- Separate target engineering from features
- Document all feature creation logic

## Missing Value Imputation

### Q11: What's the difference between MCAR, MAR, and MNAR?
**A:**
- **MCAR** (Missing Completely At Random): Missing data is random, no pattern
- **MAR** (Missing At Random): Missing pattern depends on observed data
- **MNAR** (Missing Not At Random): Missing data depends on unobserved values

Use simple imputation (mean) for MCAR, advanced methods for MAR/MNAR.

### Q12: How do I choose between mean and median imputation?
**A:**
- **Mean**: Better for normally distributed, no outliers
- **Median**: Better for skewed data, robust to outliers
- Test both and compare model performance

### Q13: Is forward fill (LOCF) appropriate for non-time-series data?
**A:** Generally no. Forward fill is designed for:
- Time series data with temporal ordering
- Sequential observations

For non-temporal data, use statistical or domain-based imputation.

### Q14: How do I handle missing values in categorical columns?
**A:**
- **Option 1**: Create "Unknown" or "Missing" category
- **Option 2**: Use mode (most frequent value)
- **Option 3**: Use domain knowledge for appropriate default
- **Option 4**: Drop rows (if percentage is low)

## Performance

### Q15: How do I optimize data processing performance?
**A:**
1. Use appropriate partitioning
2. Cache DataFrames used multiple times
3. Broadcast small lookup tables
4. Minimize shuffling operations
5. Use columnar storage (Parquet)
6. Filter early, select late

### Q16: Should I normalize/scale data for tree-based models?
**A:** No. Tree-based models (Random Forest, XGBoost) are scale-invariant. Scale only for:
- Distance-based algorithms (KNN, K-Means)
- Gradient descent algorithms (Linear/Logistic Regression, Neural Networks)

## Best Practices

### Q17: What's a good data processing pipeline structure?
**A:**
```
1. Data Ingestion
   ↓
2. Schema Validation
   ↓
3. Deduplication & Cleaning
   ↓
4. Missing Value Handling
   ↓
5. Outlier Detection
   ↓
6. Feature Engineering
   ↓
7. Feature Scaling
   ↓
8. Data Quality Validation
   ↓
9. Output Generation
```

### Q18: How do I validate data quality?
**A:**
- Check row counts and schema changes
- Validate null percentages
- Compare statistics (mean, std, min, max)
- Check for unexpected values
- Verify data types

### Q19: Should I handle outliers before or after scaling?
**A:** Before scaling. Outliers affect scaling parameters:
1. Detect outliers (IQR, Z-score)
2. Handle outliers (remove, transform, cap)
3. Then apply scaling

### Q20: How do I document data processing transformations?
**A:**
- Add comments for business logic
- Document assumptions
- Record data quality checks
- Version control all transformations
- Maintain transformation lineage
