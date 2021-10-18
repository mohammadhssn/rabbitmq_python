import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

severities = ('INFO', 'WARNING', 'ERROR')

for severity in severities:
    ch.queue_bind(queue=qname, exchange='direct_logs', routing_key=severity)
print('waiting...')


def callback(ch, method, properties, body):
    print(f'{method.routing_key}: {body}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_consume(queue=qname, on_message_callback=callback)

ch.start_consuming()