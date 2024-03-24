from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName("simple pyspark") \
        .getOrCreate()

df = spark.read.csv(path=r'C:\Users\AKASH.S\Documents\data.csv',header=True,inferSchema=True)
df.show()
df.printSchema()



