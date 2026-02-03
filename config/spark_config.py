# config/spark_config.py

APP_NAME = "MarketDataKafkaToPostgres"

KAFKA_PACKAGE = "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"

CHECKPOINT_LOCATION = "/tmp/spark-checkpoints/market-data"
