from sqlalchemy import (
	BigInteger,
	Column,
	Text,
)

from sqlalchemy.dialects.postgresql import UUID
from db.base_class import Base


class Post(Base):
	id = Column(
		UUID(as_uuid=True),
		primary_key=True,
		unique=True,
		nullable=False,
	)
	title = Column(Text, nullable=False)
	content = Column(Text, nullable=False)
	create_time = Column(BigInteger, nullable=False)
	modify_time = Column(BigInteger, nullable=False)
	user = Column(Text, nullable=False)
