from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("Big Data Route Optimization") \
    .getOrCreate()

print("=" * 70)
print("PROJECT FOLDER:", os.getcwd())
print("=" * 70)

print("\nSearching datasets folder...\n")

for root, dirs, files in os.walk("datasets"):
    print(f"\nFolder: {root}")

    if dirs:
        print(" Subfolders:")
        for d in dirs:
            print("   ", d)

    if files:
        print(" Files:")
        for f in files:
            print("   ", f)

print("\nSearch Complete!")

spark.stop()