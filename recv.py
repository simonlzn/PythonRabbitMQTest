import pika
import time
import json

from send import *

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='queue3')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    data = json.loads(body)
    print data["func"]
    print data["abc"]
    time.sleep(5)
    sender = Sender()
    sender.send()

channel.basic_consume(callback,
                      queue='queue3',
                      no_ack=True)

channel.start_consuming()
