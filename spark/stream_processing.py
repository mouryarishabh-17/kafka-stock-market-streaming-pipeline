from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType

from config.kafka_config import BOOTSTRAP_SERVERS, TOPIC_NAME
from config.spark_config import APP_NAME, CHECKPOINT_LOCATION
from config.postgres_config import (
    POSTGRES_URL,
    POSTGRES_TABLE,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)

# ---------------------------
# Spark Session
# ---------------------------
def get_spark_session():
    return (
        SparkSession.builder
        .appName(APP_NAME)
        .getOrCreate()
    )


# ---------------------------
# Schema
# ---------------------------
def get_stock_schema():
    return StructType([
        StructField("symbol", StringType(), True),
        StructField("timestamp", StringType(), True),
        StructField("open", DoubleType(), True),
        StructField("high", DoubleType(), True),
        StructField("low", DoubleType(), True),
        StructField("close", DoubleType(), True),
        StructField("volume", LongType(), True),
    ])


# ---------------------------
# Kafka Read
# ---------------------------
def read_kafka_stream(spark):
    return (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS)
        .option("subscribe", TOPIC_NAME)
        .option("startingOffsets", "earliest")
        .load()
    )


# ---------------------------
# Parse JSON
# ---------------------------
def parse_kafka_value(kafka_df, schema):
    return (
        kafka_df
        .selectExpr("CAST(value AS STRING) as json")
        .select(from_json(col("json"), schema).alias("data"))
        .select("data.*")
    )


# ---------------------------
# Write Batch to Postgres
# ---------------------------
def write_batch(batch_df, batch_id):
    print(f"\n===== ENTERED write_batch | batch_id={batch_id} =====")
    print(f"Rows in batch: {batch_df.count()}")

    if batch_df.count() == 0:
        print("Empty batch — skipping write")
        return

    fixed_df = batch_df.withColumn(
        "timestamp",
        to_date(col("timestamp"), "yyyy-MM-dd")
    )

    fixed_df.write \
        .format("jdbc") \
        .option("url", POSTGRES_URL) \
        .option("dbtable", POSTGRES_TABLE) \
        .option("user", POSTGRES_USER) \
        .option("password", POSTGRES_PASSWORD) \
        .option("driver", "org.postgresql.Driver") \
        .mode("append") \
        .save()

    print("✅ Batch written successfully")

# ---------------------------
# Main
# ---------------------------
def main():
    spark = get_spark_session()
    schema = get_stock_schema()

    kafka_df = read_kafka_stream(spark)
    parsed_df = parse_kafka_value(kafka_df, schema)

    query = (
        parsed_df.writeStream
        .foreachBatch(write_batch)
        .outputMode("append")
        .option("checkpointLocation", CHECKPOINT_LOCATION)
        .queryName("kafka_to_postgres_stream")
        .start()
    )

    print("🚀 Spark streaming query started. Waiting for data...")
    query.awaitTermination()


if __name__ == "__main__":
    main()
