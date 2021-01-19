import pika
import json

params = pike.URLParameters('amqp://rabbitmq:5672')

connection = pika.BlockingConnection(params)

channel = connection.channel()

    def publish(method, body):
        properties = pika.BasicProperties(method)
        channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
