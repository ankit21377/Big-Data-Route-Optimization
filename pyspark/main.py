from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("BODS TransXChange") \
    .master("local[*]") \
    .getOrCreate()