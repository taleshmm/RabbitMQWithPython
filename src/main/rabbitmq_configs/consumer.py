import pika
import json


def on_message_callback(ch, method, properties, body):
    message_formated = json.loads(body.decode("utf-8"))
    print(f"Received message: {message_formated}")

class RabbitMQConsumer:
    def __init__(self) -> None:
        self.__host = "localhost"
        self.__port = "5672"
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "minha_queue"
        self.__channel = self.create_channel()
        
    def create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username, 
                password=self.__password)
        )
        channel = pika.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
      
        channel.basic_consume(
            queue=self.__queue,
            on_message_callback=on_message_callback,
            auto_ack=True
            )
        return channel
    
   
    
    def start(self):
        print("Sistema conectado ao rabbitMQ")
        self.__channel.start_consuming()
     