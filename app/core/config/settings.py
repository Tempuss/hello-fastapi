import os
import socket

from typing import (
    Optional,
    Dict,
    Any,
)
from pydantic import (
    BaseSettings,
    PostgresDsn,
    validator,
)

def error(err):
    raise Exception(err.str())

class Settings(BaseSettings):
    API_PREFIX: str = "/v1"
    SERVICE_NAME: str = "Hello Fast API"
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', "127.0.0.1")
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', "postgres")
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', "postgres")
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', "tempus")

    KAFKA_CONFIG: dict = {
        'bootstrap.servers': "host1:9092,host2:9092",
        'client.id': socket.gethostname()
    }

    BOOTSTRAP_SERVERS : str =  os.environ.get("BOOTSTRAP_SERVERS", "0.0.0.0:29092")

    KAFKA_PRODUCER_CONF = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'broker.address.family': 'v4',
        'retries': 0,
        'error_cb': error,
    }

    KAFKA_CONSUMER_CONF = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'broker.address.family': 'v4',
        'group.id': "1",
        'error_cb': error,
    }

    KAFKA_TOPIC = "DOMAIN_LIST"


settings = Settings()
