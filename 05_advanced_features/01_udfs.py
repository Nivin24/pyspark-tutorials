# User-Defined Functions Tutorial
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, pandas_udf
from pyspark.sql.types import IntegerType, StringType

spark = SparkSession.builder.appName("UDFs").getOrCreate()
df = spark.createDataFrame([(1,), (2,), (3,)], ["value"])

# Python UDF (slower)
@udf(IntegerType())
def add_ten(x):
    return x + 10

# Pandas UDF (faster)
@pandas_udf(IntegerType())
def add_twenty(s):
    return s + 20

df.withColumn("plus_ten", add_ten("value")).withColumn("plus_twenty", add_twenty("value")).show()
print("UDF examples completed")
