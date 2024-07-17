from fastapi import FastAPI
from kafka import KafkaConsumer
from datetime import datetime

app = FastAPI()

# Replace with your Kafka broker address
KAFKA_BROKER_ADDRESS = "localhost:9092"

@app.get("/metrics/{topic_name}/{group_id}")
async def get_kafka_metrics(topic_name: str, group_id: str):
  consumer = KafkaConsumer(topic_name, bootstrap_servers=KAFKA_BROKER_ADDRESS, 
                           group_id=group_id, auto_offset_reset="earliest")
  
  metrics = {
      "topic_name": topic_name,
      "dt": datetime.now().isoformat(),
      "group_id": group_id,
      "partitions": []
  }

  for partition in consumer.partitions_for_topic(topic_name):
    max_offset = consumer.offsets([partition])[partition][0]
    last_committed_offset = consumer.committed(partition).get(partition, None)
    lag = max_offset - last_committed_offset if last_committed_offset is not None else max_offset
    
    metrics["partitions"].append({
        "max_offsets": max_offset,
        "last_committed_offsets": last_committed_offset,
        "lag": lag,
        "partition_id": partition
    })
  
  consumer.close()
  return metrics
