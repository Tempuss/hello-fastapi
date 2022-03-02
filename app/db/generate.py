from typing import Generator
from db.session import Session


def get_db_session() -> Generator:
	try:
		db = Session()
		yield db
	finally:
		db.close()
