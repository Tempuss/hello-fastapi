from typing import Generic, Optional, Type, TypeVar, List

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db.base_class import Base
from sqlalchemy.sql.expression import literal

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CrudBase(Generic[ModelType]):
    def __init__(
            self,
            model: Type[ModelType]
    ):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def __getitem__(self, key):
        return getattr(self, key)

    def get(
            self,
            *,
            db: Session,
            offset: int = 0,
            limit: int = 10
    ) -> Optional[ModelType]:
        return db.query(self.model).filter(
        ).offset(offset).limit(limit).all()

    def get_by_obj_id(
            self,
            *,
            db: Session,
            pk: str = None
    ) -> Optional[ModelType]:
        return db.query(self.model).filter(
            self.model.id == pk,
        ).first()

    def create(
            self,
            *,
            db: Session,
            obj_in: CreateSchemaType
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(
            self,
            *,
            db: Session,
            pk: str,
    ) -> ModelType:
        obj = db.query(self.model).filter(
            self.model.id == pk,
        ).first()
        if obj is None:
            return None

        db.delete(obj)
        db.commit()
        return obj
    #
    # def exists(
    #         self,
    #         *,
    #         db: Session,
    #         key: str,
    #         value: str,
    # ) -> ModelType:
    #     return (
    #         db.query(literal(True))
    #             .filter(
    #             db.query(self.model)
    #                 .filter(
    #                 self.model[key] == value,
    #             )
    #                 .exists()
    #         )
    #             .scalar()
    #     )
