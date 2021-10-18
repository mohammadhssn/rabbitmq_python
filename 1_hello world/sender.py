import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch1 = connection.channel()

ch1.queue_declare(queue='hello')

ch1.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print('Send Message.')

connection.close()
