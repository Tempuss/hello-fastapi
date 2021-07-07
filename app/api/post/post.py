from fastapi import APIRouter
from starlette.requests import Request
from sqlalchemy.orm import Session

from fastapi import (
	APIRouter,
	Depends,
	status,
	Query,
	encoders,
)
from fastapi.responses import (
	JSONResponse,
)
from typing import (
	Any,
	Optional,
)
from crud.crud_post import post
from db.generate import get_db_session
from schema import PolicyListSchema

router = APIRouter()


@router.get("")
def get_post(
		request: Request,
		db: Session = Depends(get_db_session),
		page: Optional[int] = Query(
			title="page Number",
			default=1,
			ge=1
		),
		per_page: Optional[int] = Query(
			title="per_page Number",
			default=10,
			ge=0
		),
):
	data = post.get(
		db=db,
		skip=(page - 1) * per_page,
		limit=per_page,
	)
	return JSONResponse(
		status_code=status.HTTP_200_OK,
		content=encoders.jsonable_encoder(
			PolicyListSchema(
				data=encoders.jsonable_encoder(data),
			)
		)
	)
