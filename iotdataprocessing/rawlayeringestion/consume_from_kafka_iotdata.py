from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, DoubleType
from pyspark.sql.streaming import DataStreamWriter


class SparkKafkaStreamingJob:
    def __init__(self, kafka_bootstrap_servers: str, kafka_topic: str):
        """Initialize Spark Streaming Job"""
        self.spark = self._create_spark_session()
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.kafka_topic = kafka_topic
        self.schema = self._define_schema()

    def _create_spark_session(self):
        """Creates and returns a SparkSession with Structured Streaming support"""
        return SparkSession.builder \
            .appName("KafkaSparkStreaming") \
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
        """Reads data from Kafka topic as a DataFrame"""
        return self.spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_bootstrap_servers) \
            .option("subscribe", self.kafka_topic) \
            .option("startingOffsets", "earliest") \
            .load()
    
    def process_stream(self, raw_df):
        """Processes the incoming Kafka messages"""
        return raw_df.selectExpr("CAST(value AS STRING) as json_string") \
            .select(from_json(col("json_string"), self.schema).alias("data")) \
            .select("data.*")  # Flatten the JSON structure

    def write_to_console(self, processed_df):
        """Writes the transformed stream to the console"""
        return processed_df.writeStream \
            .outputMode("append") \
            .format("console") \
            .start()
    
    def run(self):
        """Main function to execute the Spark Streaming Job"""
        raw_df = self.read_from_kafka()
        processed_df = self.process_stream(raw_df)
        query = self.write_to_console(processed_df)
        self.spark.streams.awaitAnyTermination()

if __name__ == "__main__":
    kafka_bootstrap_servers = "localhost:9092"
    kafka_topic = "sensor-data"
    streaming_job = SparkKafkaStreamingJob(kafka_bootstrap_servers, kafka_topic)
    streaming_job.run()