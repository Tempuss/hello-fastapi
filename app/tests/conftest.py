import pytest
from _pytest.config import Config

from typing import Generator
from fastapi.testclient import TestClient

from main import app

@pytest.fixture(scope="module", autouse=True)
def client() -> Generator:
	""" FastAPI의 테스트 클라이언트
	"""
	with TestClient(app) as c:
		yield c