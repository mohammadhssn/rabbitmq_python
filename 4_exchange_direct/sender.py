import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs', exchange_type='direct')

messages = {
    'INFO': 'this is INFO message',
    'WARNING': 'this is WARNING message',
    'ERROR': 'this is ERROR message',
}

for k, v in messages.items():
    ch.basic_publish(exchange='direct_logs', routing_key=k, body=v)

connection.close()