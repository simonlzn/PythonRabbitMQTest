import pika

class Sender(object):

    def send(self):
	connection = pika.BlockingConnection(pika.ConnectionParameters(
        	host='localhost'))
	channel = connection.channel()


	channel.queue_declare(queue='queue1')

	channel.basic_publish(exchange='',
        	              routing_key='queue1',
                	      body='test from python')
	print(" [x] Sent 'test'")
	connection.close()
