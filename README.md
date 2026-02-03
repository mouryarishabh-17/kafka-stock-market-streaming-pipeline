# Kafka Stock Market Streaming Pipeline (with GenAI SQL Assistant)

## 🚀 Project Overview

This project is a **real-time stock market data streaming system** designed to demonstrate how modern data platforms ingest, process, store, and query continuously arriving data.

The system simulates live stock market feeds using historical data and processes them in real time using **Apache Kafka**, **Apache Spark Structured Streaming**, and **PostgreSQL**, all deployed on **AWS EC2**.  
On top of the data pipeline, a **GenAI-style query layer** allows users to ask business-style questions and receive results from the database.

The goal of this project is to showcase **end-to-end data engineering skills**, system design thinking, and production-style workflows.

---

## What Problem Does This Project Solve?

In real companies:
- Market data arrives continuously
- Systems must process data in real time
- Storage must support analytics
- Analysts need simple ways to query data

Instead of using paid or rate-limited APIs, this project **recreates a real-time environment** by converting historical stock data into a streaming data source. 

This makes the system:
- Reproducible
- Cost-effective
- Easy to test and explain

---

## Architecture
```
                                                   +-----------------------------+
                                                   | Historical Stock Data (CSV) |
                                                   +-----------------------------+
                                                                  |
                                                                  v
                                             +-----------------------------------------+
                                             | Kafka Producer (Simulated Real-Time Feed)|
                                             +-----------------------------------------+
                                                                  |
                                                                  v
                                                         +----------------+
                                                         |  Apache Kafka  |
                                                         +----------------+
                                                                  |
                                                                  v
                                                   +-----------------------------+
                                                   | Spark Structured Streaming  |
                                                   +-----------------------------+
                                                                  |
                                                                  v
                                                         +----------------+
                                                         | PostgreSQL     |
                                                         +----------------+
                                                                  |
                                                                  v
                                                +----------------------------------+
                                                | Natural Language → SQL Interface |
                                                +----------------------------------+

```


---

## Technologies Used

| Category | Technology |
|-------|-----------|
| Programming | Python |
| Streaming Platform | Apache Kafka |
| Stream Processing | Apache Spark Structured Streaming |
| Database | PostgreSQL |
| Cloud | AWS EC2 |
| Query Interface | GenAI-style SQL Generator |

---

## How the System Works

### 1. Data Ingestion
Historical stock market data (from Kaggle) is read row by row and published to a Kafka topic using a Python producer. A small delay between messages simulates real-time market activity.

### 2. Streaming & Processing
Apache Spark Structured Streaming consumes messages from Kafka, applies a defined schema, and processes the data in micro-batches.

### 3. Storage
Processed data is written into PostgreSQL with correct data types and structure, making it suitable for analytics and reporting.

### 4. Querying with GenAI Logic
Users can ask simple business-style questions (for example, “Show recent Tesla prices”).  
The system converts the question into an SQL query and executes it on PostgreSQL.

---

## Cloud Deployment

All core components (Kafka, Spark, PostgreSQL, producer, and streaming jobs) run on **AWS EC2 (Ubuntu)**.  
The project was developed locally using **VS Code** and then deployed to the cloud to reflect real-world workflows.

---

## Why This Project Is Different

- Uses **real-time streaming**, not batch processing
- Avoids paid APIs while maintaining realistic behavior
- Demonstrates **event-driven architecture**
- Shows how large-scale systems are built in industry
- Includes a **query abstraction layer** similar to analyst tools

---

## Key Skills Demonstrated

- Data pipeline design
- Kafka-based event streaming
- Spark Structured Streaming
- Cloud deployment (AWS EC2)
- Database modeling
- Debugging distributed systems
- Translating business questions into data queries

---

## Future Improvements

- Integrate an LLM (OpenAI / open-source) for more advanced querying
- Add dashboards for visualization
- Containerize services using Docker
- Improve fault tolerance and monitoring

---

## Summary

This project represents a **production-style data engineering pipeline** that processes streaming data end to end.  
It demonstrates both technical depth and practical system design, making it suitable for real-world data engineering and analytics roles.


