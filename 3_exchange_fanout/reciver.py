import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='logs', exchange_type='fanout')
result = ch.queue_declare(queue='', exclusive=True)


qname = result.method.queue

ch.queue_bind(queue=qname, exchange='logs')
print('waiting..')


def callback(ch, method, properties, body):
    print(f'Received: {body}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_consume(queue=qname, on_message_callback=callback)

ch.start_consuming()