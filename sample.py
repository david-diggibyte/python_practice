# create dataframe

from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .getOrCreate()

data = [(1, "David"), (2, "Susai")]
schema = ["id", "name"]

# Create DataFrame

df = spark.createDataFrame(data=data,schema=schema)
df.show()
df.printSchema()
print(type(spark))
print(dir(spark))

