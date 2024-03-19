# receive.py
# Consumer that receives a message from the queue

import pika


# Callback function that is called when a message is received
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# Connection to RabbitMQ server on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

# Subscribe to the queue
channel.basic_consume(queue='hello',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()