from kafka import KafkaConsumer
import json

KAFKA_SERVER = ['kafka:9092']
KAFKA_TOPIC = 'shop_data'
FILE_PATH = 'data.json'

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def main():
    with open(FILE_PATH, 'a', encoding='utf-8') as file:
        for message in consumer:
            file.write(json.dumps(message.value, ensure_ascii=False) + '\n')
            break

    print("Data written to file and program is shutting down.")

if __name__ == "__main__":
    main()
