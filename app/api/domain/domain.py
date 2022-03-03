import logging
from starlette.requests import Request
from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    Depends,
    status,
    Query,
)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import (
    JSONResponse,
)
from typing import (
    Optional,
)
from datetime import datetime
from crud.crud_domain import domain

from response import (
    CreateResponse,
    DomainPagination,
    DomainCreateResponse,
    DomainCreateParams,
)
from db.generate import get_db_session
from hashlib import sha256
from core.kafka.connect import (
    get_kafka_producer,
    acked,
)
from core.config.settings import settings
from json import (
    dumps,
)

router = APIRouter()
logger = logging.getLogger("fastapi")


@router.get(
    path="",
    response_model=DomainPagination,
)
async def get_domain(
        request: Request,
        db: Session = Depends(get_db_session),
        offset: Optional[int] = Query(default=0),
        limit: Optional[int] = Query(default=100, lte=100)
):
    data = domain.get(
        db=db,
        offset=offset,
        limit=limit,
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(
            DomainPagination(
                data=jsonable_encoder(data),
                offset=offset,
                limit=limit
            )
        )
    )


@router.post(
    path="",
    response_model=DomainPagination,
)
async def create_domain(
        request: Request,
        db: Session = Depends(get_db_session),
        producer=Depends(get_kafka_producer),
        params: DomainCreateParams = None,
):
    params.sha256 = sha256(params.domain.encode()).hexdigest().upper()
    params.first_request_time = int(datetime.timestamp(datetime.now()))
    params.last_request_time = int(datetime.timestamp(datetime.now()))

    if domain.exists_domain(
            db=db,
            params=params,
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": "Already created."
            }
        )

    data = domain.create(
        db=db,
        obj_in=DomainCreateParams.parse_obj(obj=params)
    )

    producer.produce(
        topic=settings.KAFKA_TOPIC,
        value=dumps(
            {
                "domain": params.domain,
                "id": str(data.id)
            }
        ).encode('utf-8'),
        callback=acked
    )
    producer.flush()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            CreateResponse(
                id=str(data.id),
                message="Domain Successed",
            )
        )
    )
