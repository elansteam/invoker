from loguru import logger


def basic_submission_callback(ch, method, properties, body):
    logger.info(f" [x] Received {body}")
