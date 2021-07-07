from typing import (
	Optional,
	List
)
from fastapi import (
	Query,
)


from pydantic import BaseModel


class PolicyListSchema(BaseModel):
	id: str = Query(
		title="primary Key",
		default="UUID String",
	)
	title: str = Query(
		title="primary Key",
		default="title",
	)
	content: str = Query(
		title="primary Key",
		default="content",
	)
	create_time: int = Query(
		title="primary Key",
		default=1234,
	)
	modify_time: int = Query(
		title="primary Key",
		default=1234,
	)
	user: str = Query(
		title="User PK",
		default="UUID",
	)
