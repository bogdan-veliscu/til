import pika, json

connection = pika.BlockingConnection(pika.ConnectionParameters('docker.for.mac.localhost'))

channel = connection.channel()


def publish(method, body):
    properties = pika.Properties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
