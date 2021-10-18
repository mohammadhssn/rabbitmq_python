import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
ch2 = connection.channel()

ch2.queue_declare(queue='hello')


def call_back(ch, method, properties, body):
    print(f'Received: {body}')


ch2.basic_consume(queue='hello', on_message_callback=call_back, auto_ack=True)
print('Waiting for message.../ Exit (CTRL C)')

ch2.start_consuming()