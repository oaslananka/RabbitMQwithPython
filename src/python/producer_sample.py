import pika

user_name = "username"
password = "password"
host = "localhost"
port = 5672
virtual_host = "/"
queue_name = "hello"


# Connect to RabbitMQ server
credentials = pika.PlainCredentials(user_name, password)

parameters = pika.ConnectionParameters(host, port, virtual_host, credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Create queue if it does not exist
channel.queue_declare(queue=queue_name)


# Send message
channel.basic_publish(exchange='', routing_key=queue_name, body='Hello RabbitMQ!')


print("Message sent: 'Hello RabbitMQ!'")

# Close the connection
connection.close()
