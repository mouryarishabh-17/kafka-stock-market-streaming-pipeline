# Kafka Streaming Data Pipeline with GenAI

A real-time data engineering pipeline that ingests stock market data, processes it with **Apache Spark**, stores it in **PostgreSQL**, and allows users to query the data using natural language (**GenAI**).

## 🚀 Architecture
1. **Ingestion**: Reads stock CSV data and streams it to **Kafka** (`ingestion/producer.py`).
2. **Processing**: **Spark Structured Streaming** reads from Kafka, transforms data, and writes to Postgres (`spark/stream_processing.py`).
3. **Storage**: Data is stored in **PostgreSQL** (`storage/schema.sql`).
4. **Interface**: A command-line Chat UI allows users to ask questions like *"What was the closing price of Apple?"* (`genai/chat_ui.py`).

## 🛠️ Prerequisites
- Python 3.8+
- Apache Kafka (Running locally or on AWS/Docker)
- PostgreSQL (Running locally or on AWS/Docker)
- Java 8/11/17 (Required for Spark)

## 📦 Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   # Run the SQL commands in storage/schema.sql in your Postgres DB
   ```

## ⚙️ Configuration
Update the configuration files in `config/` to match your environment variables or local setup:
- `config/kafka_config.py` (Kafka Broker)
- `config/postgres_config.py` (DB Credentials)

## ▶️ How to Run
1. **Start the Producer** (Sends data to Kafka):
   ```bash
   python ingestion/producer.py
   ```
2. **Start the Spark Processor** (Consumes and writes to DB):
   ```bash
   python spark/stream_processing.py
   ```
3. **Chat with Data**:
   ```bash
   python genai/chat_ui.py
   ```

## 📂 Project Structure
- `ingestion/` - Data producers and raw data.
- `spark/` - Spark streaming logic.
- `genai/` - Natural Language to SQL logic.
- `config/` - Configuration files.
- `storage/` - Database schemas.
