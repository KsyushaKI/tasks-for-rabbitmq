import os
import json
import pika
import time


host = 'localhost'
queue = 'generate_files'
dir = f"{os.getcwd()}/tasks_for_rabbitmq/data"
time_out = 15


def rmq_send_message(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )

    connection.close()


def publisher():
    if not os.path.exists(dir):
        os.makedirs(dir)

    message_id = 0
    while True:
        time.sleep(time_out)
        message_id += 1
        message = json.dumps(
            {'files': os.listdir(dir),
            'message_id': message_id}
        )
        rmq_send_message(message)
