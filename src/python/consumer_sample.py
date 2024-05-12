import pika

user_name = "username"
password = "password"
host = "localhost"
port = 5672
virtual_host = "/"
queue_name = "hello"


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


# Connect to RabbitMQ server
credentials = pika.PlainCredentials(user_name, password)

parameters = pika.ConnectionParameters(host, port, virtual_host, credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Create queue if it does not exist
channel.queue_declare(queue=queue_name)

# Listen to the message
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
