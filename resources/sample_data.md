# Sample Datasets & Data Resources

This guide provides links to publicly available datasets and resources for practicing PySpark.

## Public Datasets

### 1. **Kaggle Datasets** (Free with account)
- **URL**: https://www.kaggle.com/datasets
- **Popular PySpark-friendly datasets**:
  - MovieLens Dataset (ratings, recommendations)
  - Netflix Prize Dataset
  - NYC Taxi Dataset
  - Amazon Reviews Dataset
  - Stock Market Data
- **Format**: CSV, JSON, Parquet
- **Size**: 100MB to 50GB+
- **Use Cases**: Recommendations, time-series, regression

### 2. **Google Cloud Public Datasets**
- **URL**: https://console.cloud.google.com/marketplace/browse?filter=gcp-public
- **Notable Datasets**:
  - NYC Taxi and Uber Data
  - GitHub Archive
  - Wikipedia Dataset
  - COVID-19 Dataset
  - Stack Overflow Data
- **Format**: BigQuery, GCS
- **Cost**: Free tier available
- **Scale**: Terabytes

### 3. **UCI Machine Learning Repository**
- **URL**: https://archive.ics.uci.edu/ml/
- **Datasets**: 600+ ML datasets
- **Popular for PySpark**:
  - Adult Income Dataset
  - Iris Dataset
  - Wine Dataset
  - Credit Card Fraud Detection
  - Customer Churn Data
- **Format**: CSV, UCI format
- **Size**: Small to medium

### 4. **Open Data Portal**
- **URL**: https://www.data.gov/
- **Content**: US Government datasets
- **Datasets**:
  - Census Data
  - Climate Data
  - Health Statistics
  - Education Data
  - Energy Data
- **Format**: CSV, Excel, JSON

### 5. **Awesome Datasets Repository**
- **URL**: https://github.com/awesomedata/awesome-public-datasets
- **Curated collection**: 1000+ datasets
- **Categories**: Computer Science, Medicine, Social Science, etc.
- **Regular updates**: Community maintained

### 6. **Reddit Datasets**
- **URL**: https://www.reddit.com/r/datasets/
- **Community-shared**: Free datasets
- **Formats**: Various
- **Topics**: Varied

## Quick Dataset Downloads

### Movie Ratings Data (MovieLens)
```bash
# Download MovieLens 100K dataset
wget https://files.grouplens.org/datasets/movielens/ml-100k.zip
unzip ml-100k.zip

# Download MovieLens 1M dataset
wget https://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip
```

### NYC Taxi Data
```bash
# January 2021 Yellow Taxi Data
wget https://d37ciml9tz8tbg.cloudfront.net/nyc-taxi/yellow_tripdata_2021-01.parquet
```

### COVID-19 Data
```bash
# Johns Hopkins COVID-19 data
git clone https://github.com/CSSEGISandData/COVID-19.git
```

## Synthetic Data Generation

### Using Python libraries to create test data:

```python
from faker import Faker
import random

faker = Faker()
data = []
for _ in range(10000):
    data.append({
        'user_id': faker.uuid4(),
        'name': faker.name(),
        'email': faker.email(),
        'purchase_amount': random.uniform(10, 1000),
        'date': faker.date_this_year()
    })
```

## Data Format Examples

### CSV Format
```csv
user_id,product_id,rating,timestamp
1,101,5,2024-01-15
2,102,4,2024-01-16
3,101,3,2024-01-17
```

### JSON Format
```json
[
  {"user_id": 1, "product_id": 101, "rating": 5, "timestamp": "2024-01-15"},
  {"user_id": 2, "product_id": 102, "rating": 4, "timestamp": "2024-01-16"}
]
```

### Parquet Format (Binary)
- Most efficient for Spark
- Compressed and columnar
- Preserves schema
- Fastest reading in Spark

## Sample CSV Data

### E-commerce Orders
```csv
order_id,customer_id,product_id,quantity,price,order_date,status
1001,C001,P101,2,25.99,2024-01-01,completed
1002,C002,P102,1,49.99,2024-01-01,pending
1003,C001,P103,5,10.50,2024-01-02,completed
```

### User Activity
```csv
user_id,event_type,event_timestamp,event_value,platform
U001,login,2024-01-15T10:30:00,1,web
U001,purchase,2024-01-15T10:35:00,99.99,web
U002,login,2024-01-15T10:32:00,1,mobile
```

### Product Reviews
```csv
review_id,product_id,user_id,rating,review_text,review_date
R001,P101,U001,5,"Great product!",2024-01-10
R002,P102,U002,3,"Average quality",2024-01-11
R003,P101,U003,4,"Good value for money",2024-01-12
```

## Data Volume Guidelines

### Small (< 1GB) - For Development
- Local machine testing
- Unit tests
- Quick prototyping
- Examples: UCI datasets, MovieLens 100K

### Medium (1GB - 10GB) - For Learning
- Single node Spark
- Algorithm experimentation
- Performance testing
- Examples: MovieLens 1M, reduced taxi data

### Large (10GB - 100GB) - For Production Simulation
- Multi-node Spark cluster
- Real-world scenarios
- Optimization exercises
- Examples: Full NYC taxi, GitHub Archive

### XL (> 100GB) - Enterprise Scale
- Distributed processing essential
- Cloud platforms recommended
- Examples: Google Cloud Public Datasets

## Data Privacy & Licensing

### Free to Use
- ✅ Kaggle datasets (most)
- ✅ UCI ML Repository
- ✅ data.gov (public domain)
- ✅ MovieLens (research purposes)

### Attribution Required
- ⚠️ Many research datasets
- ⚠️ Academic papers' datasets
- Check license before use

### Restricted Use
- ❌ Personal data without anonymization
- ❌ Proprietary datasets
- ❌ Commercial datasets without license

## Data Preparation Tips

1. **Check Data Quality**
   - Missing values
   - Duplicates
   - Data type consistency

2. **Handle Large Files**
   - Split into chunks
   - Use compression (gzip)
   - Consider Parquet format

3. **Schema Definition**
   - Define schema before loading
   - Reduces parsing overhead
   - Improves performance

4. **Data Sampling**
   - Test with 10% sample first
   - Validate transformations
   - Then scale to full dataset

## Creating Local Test Data

```python
from pyspark.sql import SparkSession
from datetime import datetime, timedelta
import random

spark = SparkSession.builder.appName("CreateTestData").getOrCreate()

# Create sample dataframe
data = [
    (1, "Alice", 25, "2024-01-01"),
    (2, "Bob", 30, "2024-01-02"),
    (3, "Charlie", 35, "2024-01-03"),
]

df = spark.createDataFrame(data, ["id", "name", "age", "date"])
df.write.csv("path/to/sample_data.csv", header=True)
```

## Storage Formats Comparison

| Format | Size | Speed | Schema | Compression |
|--------|------|-------|--------|-------------|
| CSV    | Large| Slow  | No     | Optional    |
| JSON   | Large| Medium| Yes    | Optional    |
| Parquet| Small| Fast  | Yes    | Built-in    |
| ORC    | Small| Fast  | Yes    | Built-in    |

## Recommended Learning Path

1. **Start**: UCI datasets (small, clean)
2. **Progress**: MovieLens (medium, real)
3. **Advanced**: NYC Taxi or Google Cloud (large, messy)
4. **Master**: Create your own dataset from APIs

## Resources Links Summary

- Kaggle: https://kaggle.com/
- UCI ML: https://archive.ics.uci.edu/ml/
- data.gov: https://www.data.gov/
- MovieLens: https://grouplens.org/datasets/movielens/
- NYC Taxi: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Google Cloud Public Data: https://console.cloud.google.com/marketplace/browse
