from kafka import KafkaProducer
import json
import time
from datetime import datetime
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
topic = "sensor-data"
sensor_ids = ["sensor-001", "sensor-002", "sensor-003", "sensor-004", "sensor-005"]

while True:
    data = {
        "sensor_id": random.choice(sensor_ids),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "temperature": round(random.uniform(20.0, 35.0), 1),
        "humidity": round(random.uniform(30.0, 60.0), 1),
        "soil_moisture": round(random.uniform(20.0, 40.0), 1),
        "energy_usage": round(random.uniform(1.0, 10.0), 1)
    }

    producer.send(topic, value=data)
    print(f"Sent: {data} from {data['sensor_id']}")
    time.sleep(10)