from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.functions import lag
from pyspark.sql.functions import when, col
from pyspark.sql.functions import sum
from pyspark.sql.functions import  to_timestamp

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("ReadParquet") \
    .getOrCreate()

# Path to the Parquet output folder
parquet_path = "C:/Users/Arghya/PrecisionAgricultureAnalyticsSystem/iotdatagenerator/output_parquet"

# Read Parquet files
df = spark.read.parquet(parquet_path)

#Divide the monitored area into small zones (grid cells) for localized analysis.
df = df.withColumn("area_grid",
                   when((col("sensor_id").endswith("1")), "North")
                   .when((col("sensor_id").endswith("2")), "South")
                   .when((col("sensor_id").endswith("3")), "East")
                   .otherwise("West"))

#If an area’s average temperature increases over the last 3 readings, flag it
#Use Case: Early warning system for climate shifts or weather anomalies.
window_spec = Window.partitionBy("area_grid").orderBy("timestamp")

df = df.withColumn("prev_temp", lag("temperature").over(window_spec))
df = df.withColumn("temp_trend",
                   when(col("temperature") > col("prev_temp"), "Increasing")
                   .when(col("temperature") < col("prev_temp"), "Decreasing")
                   .otherwise("Stable"))

#If soil moisture is below 20% for more than 3 timestamps in a row, flag it.
#Use Case: Helps in automated irrigation – only water the areas that need it.

df = df.withColumn("low_soil_moisture_flag", when(col("soil_moisture") < 20, 1).otherwise(0))
window_spec = Window.partitionBy("area_grid").orderBy("timestamp").rowsBetween(-3, 0)
df = df.withColumn("low_soil_moisture_streak", sum("low_soil_moisture_flag").over(window_spec))
df = df.withColumn("drought_alert", when(col("low_soil_moisture_streak") >= 3, 1).otherwise(0))


# Show data in console
df.show(truncate=False)

# Write the DataFrame to a Parquet file
output_parquet_path = "C:/Users/Arghya/PrecisionAgricultureAnalyticsSystem/iotdatagenerator/output_parquet_processed"
df.write.mode("overwrite").parquet(output_parquet_path)

# Stop Spark session
spark.stop()
