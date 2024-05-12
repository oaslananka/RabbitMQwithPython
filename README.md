# RabbitMQ Sample
RabbitMQ is an open source message queuing software and is used to provide reliable communication between messages. It facilitates asynchronous messaging between components in large and complex systems using the AMQP (Advanced Message Queuing Protocol) protocol. This enables high efficiency and an unbreakable connection between applications.

Basic Components of RabbitMQ

- Producer: It is the component that produces messages.
- Consumer: It is the component that receives and processes messages from the queue.



## Scripts
- RabbitMQ Python Producer (Sender) Script: `src/python/producer_sample.py`
- RabbitMQ Python Consumer (Listener) Script: `src/python/consumer_sample.py`

## Installation

1 - Erlang Installation:
```
sudo apt update
sudo apt install -y erlang
```

2- RabbitMQ Installation:
```
sudo apt install -y rabbitmq-server
```

3 - Starting RabbitMQ Service and Checking the Status:
```
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl status rabbitmq-server
```

4 - Enabling Management Interface (optional):
```
sudo rabbitmq-plugins enable rabbitmq_management
```



## Configuration
1. Checking Available Virtual Servers
	```
	sudo rabbitmqctl list_vhosts
	```

2. Creating a Virtual Server
	```
	sudo rabbitmqctl add_vhost /myvhost
	```

3. Adding User
	```
	sudo rabbitmqctl add_user <username> <password>
	```

4. Assigning a Role to the User
	```
	sudo rabbitmqctl set_user_tags <username> administrator
	```

5. Setting User Permissions
	```
	sudo rabbitmqctl set_permissions -p /myvhost <username> ".*" ".*" ".*"
	```



<!-- - User Management: You can create new users and assign specific roles to them.
	```
	rabbitmqctl add_user <myuser> <mypassword>
	rabbitmqctl set_user_tags <myuser> administrator
	rabbitmqctl set_permissions -p / <myuser> ".*" ".*" ".*"
	``` -->


## Python Usage

You can use the pika library to work with RabbitMQ in Python. You should install this library first:
```
pip install pika
```

