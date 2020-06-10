from time import sleep
from json import dumps
from kafka import KafkaProducer

# kafka producer class
class Producer(object):
    def __init__(self, topic_name, server_address):
        self.topic_name = topic_name
        self.server_address = server_address

    # publishing massage with kafka producer
    def producer_fn(self, json_paragraphs):
        producer = KafkaProducer(bootstrap_servers = [self.server_address], value_serializer = lambda x:dumps(x).encode('utf-8'))
        producer.send(self.topic_name, value = json_paragraphs)
        producer.flush()