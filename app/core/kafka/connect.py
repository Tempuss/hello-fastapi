import logging
from typing import Generator
from core.config.settings import settings

from confluent_kafka import (
    Producer,
    KafkaError,
    KafkaException,
)

logger = logging.getLogger("fastapi")


async def get_kafka_producer():
    return Producer(**settings.KAFKA_PRODUCER_CONF)

def acked(err, msg):
    if err is not None:
        logger.error("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        logger.info(f"Produce Success offset: {msg.offset()}")
