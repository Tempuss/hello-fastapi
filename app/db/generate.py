from typing import Generator
from db.session import Session


def get_db_session() -> Generator:
	try:
		db = Session()
		yield db
	finally:
		# todo 이 코드 리팩토링 할 예정이었나본데..?
		db.close()
