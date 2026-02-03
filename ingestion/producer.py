import csv
import json
import time
import os
from kafka import KafkaProducer

from config.kafka_config import BOOTSTRAP_SERVERS, TOPIC_NAME


DATA_DIR = os.path.join("ingestion", "data")


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_csv_files(directory):
    return [
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith(".csv")
    ]


def stream_csv_to_kafka():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=json_serializer,
        retries=5
    )

    csv_files = get_csv_files(DATA_DIR)

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {DATA_DIR}")

    print(f"Found CSV files: {csv_files}")

    while True:
        for file_path in csv_files:
            symbol = os.path.basename(file_path).replace(".csv", "")

            with open(file_path, "r") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    event = {
                        "symbol": symbol,
                        "timestamp": row["Date"],
                        "open": float(row["Open"]),
                        "high": float(row["High"]),
                        "low": float(row["Low"]),
                        "close": float(row["Close"]),
                        "volume": int(float(row["Volume"]))
                    }

                    producer.send(TOPIC_NAME, event)
                    print(f"Sent: {event}")

                    time.sleep(1)

        print("Completed one full cycle. Restarting...")


if __name__ == "__main__":
    stream_csv_to_kafka()
