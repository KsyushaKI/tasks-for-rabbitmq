import os
import json
import pika
import time

host = 'localhost'
queue = 'generate_files'
dir = f"{os.getcwd()}/tasks_for_rabbitmq/data/"
result_dir = f"{os.getcwd()}/tasks_for_rabbitmq/result/"
timeout = 35


def rmq_receiver_messages():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host)
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue, on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    connection.close()


def callback(ch, method, properties, body):
    files = json.loads(body)
    filename = str(files['message_id']) + '.txt'
    print(" [x] Received %r" % body)

    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    with open(result_dir + filename, 'w') as f:
        for file in files['files']:
            if os.path.exists(dir + file):
                with open(dir + file) as f2:
                    content = f2.read()
                    f.write(content + '\n')
                    os.remove(dir + file)
    time.sleep(timeout)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)
