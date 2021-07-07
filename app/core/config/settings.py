import os

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


class Settings(BaseSettings):
	API_PREFIX: str = "/v1"
	SERVICE_NAME: str = "Hello Fast API"
	POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', "127.0.0.1")
	POSTGRES_USER: str = os.getenv('POSTGRES_USER', "postgres")
	POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', "postgres")
	POSTGRES_DB: str = os.getenv('POSTGRES_DB', "tempus")
	# SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
	#
	# @validator("SQLALCHEMY_DATABASE_URI", pre=True)
	# def assemble_db_connection(
	# 		cls,
	# 		v: Optional[str],
	# 		values: Dict[str, Any]
	# ) -> Any:
	# 	if isinstance(v, str):
	# 		return v
	# 	return PostgresDsn.build(
	# 		scheme="postgresql",
	# 		user=values.get("POSTGRES_USER", "postgres"),
	# 		password=values.get("POSTGRES_PASSWORD", "postgres"),
	# 		host=values.get("POSTGRES_SERVER", "127.0.0.1"),
	# 		port=values.get("POSTGRES_PORT", "5432"),
	# 		path=f"/{values.get('POSTGRES_DB', 'tempus')}",
	# 	)


settings = Settings()
