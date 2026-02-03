set -e

SPARK_HOME=${SPARK_HOME:-/opt/spark}
PROJECT_ROOT=$(pwd)

echo "Submitting Spark Structured Streaming Job..."

export PYTHONPATH=$PROJECT_ROOT

$SPARK_HOME/bin/spark-submit \
  --master local[*] \
  --conf spark.sql.streaming.forceDeleteTempCheckpointLocation=true \
  --conf spark.driver.extraJavaOptions="-Dlog4j.shutdownHookEnabled=false" \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  spark/stream_processing.py
