import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

binding_key = '*.*.important'

ch.queue_bind(queue='', exchange='topic_logs', routing_key=binding_key)
print('waiting...')


def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as f:
        f.write(f'{str(body)} \n')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_consume(queue=qname, on_message_callback=callback)
ch.start_consuming()
