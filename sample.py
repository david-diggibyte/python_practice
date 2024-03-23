# create dataframe

from pyspark.sql import SparkSession
from pyspark.sql.types import *

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .getOrCreate()

data = [(1, "David"), (2, "Susai")]

# schema = ["id", "name"]
schema = StructType([StructField(name='id', dataType=IntegerType()),
                     StructField(name='name', dataType=StringType())])


# Create DataFrame

df = spark.createDataFrame(data=data,schema=schema)
df.show()
df.printSchema()
print(type(spark))
print(dir(spark))
print(help(StructType))
