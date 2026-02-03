#!/bin/bash

export PYTHONPATH=$(pwd)

echo "Starting Kafka CSV Producer..."
python ingestion/producer.py
