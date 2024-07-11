from messaging import get_rabbitmq_connection, close_channel
import json
from db.status import insert_status
from dto.status import Status

connection, channel, queue_name = get_rabbitmq_connection()


def callback(ch, method, properties, body):
    status = json.loads(body)['status']
    insert_status(Status(status=status))

def start_consumer():
    print("Starting consumer")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    print("Consumer started successfully.")


def stop_consumer():
    print("Stopping consumer")
    channel.stop_consuming()
    connection.close()