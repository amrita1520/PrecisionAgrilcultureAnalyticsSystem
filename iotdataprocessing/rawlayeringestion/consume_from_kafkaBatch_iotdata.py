from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, DoubleType


class SparkKafkaBatchJob:
    def __init__(self, kafka_bootstrap_servers: str, kafka_topic: str, output_path: str):
        """Initialize Spark Batch Job"""
        self.spark = self._create_spark_session()
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.kafka_topic = kafka_topic
        self.schema = self._define_schema()
        self.output_path = output_path

    def _create_spark_session(self):
        """Creates and returns a SparkSession"""
        return SparkSession.builder \
            .appName("KafkaSparkBatch") \
            .getOrCreate()

    def _define_schema(self):
        """Defines the schema for incoming JSON sensor data"""
        return StructType() \
            .add("sensor_id", StringType()) \
            .add("timestamp", StringType()) \
            .add("temperature", DoubleType()) \
            .add("humidity", DoubleType()) \
            .add("soil_moisture", DoubleType()) \
            .add("energy_usage", DoubleType())

    def read_from_kafka(self):
        """Reads data from Kafka topic as a DataFrame (BATCH MODE)"""
        return self.spark.read \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_bootstrap_servers) \
            .option("subscribe", self.kafka_topic) \
            .option("startingOffsets", "earliest") \
            .option("endingOffsets", "latest") \
            .load()

    def process_batch(self, raw_df):
        """Processes the batch Kafka messages"""
        return raw_df.selectExpr("CAST(value AS STRING) as json_string") \
            .select(from_json(col("json_string"), self.schema).alias("data")) \
            .select("data.*")  # Flatten the JSON structure
    
    def display_to_console(self, processed_df):
        """Displays processed data in console (for debugging)"""
        processed_df.show(truncate=False)

    def write_to_parquet(self, processed_df):
        """Writes the raw batch data to Parquet format"""
        processed_df.write.mode("append").parquet(self.output_path)

    def run(self):
        """Main function to execute the Spark Batch Job"""
        raw_df = self.read_from_kafka()
        processed_df = self.process_batch(raw_df)
        self.display_to_console(processed_df)
        self.write_to_parquet(processed_df)


if __name__ == "__main__":
    kafka_bootstrap_servers = "localhost:9092"
    kafka_topic = "sensor-data"
    output_path = "C:/Users/Arghya/PrecisionAgricultureAnalyticsSystem/iotdatagenerator/output_parquet"
    batch_job = SparkKafkaBatchJob(kafka_bootstrap_servers, kafka_topic, output_path)
    batch_job.run()
