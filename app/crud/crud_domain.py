from typing import Any, Type
from crud.base import (
    CrudBase,
    ModelType,
)

from model import Domain
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import literal

from response import DomainCreateParams


class CrudDomain(CrudBase[Domain]):

    def __init__(self, model: Type[ModelType]):
        super().__init__(model)

    def exists_domain(
            self,
            db: Session,
            params: DomainCreateParams,
    ):
        return (
            db.query(literal(True))
                .filter(
                db.query(self.model)
                    .filter(
                    self.model.sha256 == params.sha256,
                )
                    .exists()
            )
                .scalar()
        )


domain = CrudDomain(Domain)
