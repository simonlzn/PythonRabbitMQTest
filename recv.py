import pika
import time
import json

from send import *

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='queue2')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    data = json.loads(body)
    print data
    time.sleep(1)
    sender = Sender()
    sender.send(body)

channel.queue_bind(exchange='python', queue="queue2", routing_key='#')
channel.basic_consume(callback,
                      queue='queue2',
                      no_ack=True)

channel.start_consuming()
