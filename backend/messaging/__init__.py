import pika


def get_rabbitmq_connection():
    # RabbitMQ setup
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # Exchange
    channel.exchange_declare(exchange="exchange", exchange_type="direct")

    # Queue
    queue = channel.queue_declare(queue="statusQueue")
    queue_name = queue.method.queue

    # Binding
    channel.queue_bind(
        exchange="exchange", queue=queue_name, routing_key="randomStatus"
    )

    return connection, channel, queue_name


def close_channel(connection):
    connection.close()
