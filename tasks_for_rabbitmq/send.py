import os
import json
import pika
import time
from interruptingcow import timeout


host = 'localhost'
queue = 'generate_files'
dir = 'tasks_for_rabbitmq/data'
time_out = 15
working_time = 135


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
    try:
        with timeout(working_time, exception=RuntimeError):
            while True:
                time.sleep(time_out)
                message = json.dumps(os.listdir(dir))
                rmq_send_message(message)
    except RuntimeError:
        pass
