import random
import json
import time

from messaging import get_rabbitmq_connection, close_channel

connection, channel, queue_name = get_rabbitmq_connection()

stop_publish: bool = False


def publish_status():
    while not stop_publish:
        status = {"status": random.randint(0, 6)}
        channel.basic_publish(
            exchange="exchange", routing_key="randomStatus", body=json.dumps(status)
        )
        print(f" [x] Sent {status}")
        time.sleep(1)


def start_publisher():
    print("Starting publisher")
    publish_status()


def stop_publisher():
    print("Stopping publisher")
    global stop_publish
    stop_publish = True
    if channel and channel.is_open:
        channel.close()
    
    if connection and connection.is_open:
        connection.close()