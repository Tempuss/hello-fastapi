from typing import Any, Type

from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import literal

from crud.base import (
	CrudBase,
	ModelType,
)

from model import Post


class CrudPost(CrudBase[Post]):
	
	def __init__(self, model: Type[ModelType]):
		super().__init__(model)
	
	


post = CrudPost(Post)
