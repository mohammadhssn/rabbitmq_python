import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs', exchange_type='direct')
result = ch.queue_declare(queue='', exclusive=True)
qname = result.method.queue

severity = 'ERROR'
ch.queue_bind(queue='', exchange='direct_logs', routing_key=severity)
print('waiting...')


def callback(ch, method, properties, body):
    with open('error_log.log', 'a') as f:
        f.write(f'str({body}) \n')
    ch.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_consume(queue=qname, on_message_callback=callback)
ch.start_consuming()
