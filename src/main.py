import pika
import callbacks
from loguru import logger
from config import Config



def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="localhost"
    ))

    channel = connection.channel()

    channel.queue_declare(queue=Config.QUEUE_NAME)

    channel.basic_consume(
        Config.QUEUE_NAME,
        callbacks.basic_submission_callback,
        auto_ack=True
    )
    logger.info("Starting consuming, press Ctrl + C to quit")

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        logger.info("Stopping consuming")


if __name__ == "__main__":
    main()
