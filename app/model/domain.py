import uuid
from sqlalchemy import (
    BigInteger,
    Column,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from db.base_class import Base


class Domain(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    domain = Column(Text, nullable=False)
    sha256 = Column(Text, nullable=False, index=True)
    first_request_time = Column(BigInteger, nullable=False)
    last_request_time = Column(BigInteger, nullable=False)

