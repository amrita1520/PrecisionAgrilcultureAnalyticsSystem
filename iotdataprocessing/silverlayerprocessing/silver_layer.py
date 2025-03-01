from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("ReadParquet") \
    .getOrCreate()

# Path to the Parquet output folder
parquet_path = "C:/Users/Arghya/PrecisionAgricultureAnalyticsSystem/iotdatagenerator/output_parquet"

# Read Parquet files
df = spark.read.parquet(parquet_path)

# Show data in console
df.show(truncate=False)

# Stop Spark session
spark.stop()
