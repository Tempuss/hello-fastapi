#
# domain API에 대한 응답값 모델
#
# @author       Tempuss (ben3787@gmail.com)
# @date         2022/02/25 00:00 created.
# @copyright    Tempuss All rights reserved.
#

from pydantic import BaseModel
from typing import (
    Optional,
    List
)
from model.domain import Domain


class DomainPagination(BaseModel):
    offset: Optional[int]
    limit: Optional[int]
    data: List[dict]

    class Config:
        # notes.
        #   from을 처리할 수가 없기 때문에 kwargs로 페이지네이션에 필요한 값을 다시 넣어준다
        #   파이썬에서 from은 reserved word이기 때문이다
        fields = {
            "from_": "from"
        }
        schema_extra = {
            "example": {
                "offset": 0,
                "limit": 10,
                "data": [
                    dict.fromkeys(Domain.__props__, "")
                ],
            }
        }


class DomainCreateResponse(BaseModel):
    id: int
    message: str

    class Config:
        # notes.
        #   from을 처리할 수가 없기 때문에 kwargs로 페이지네이션에 필요한 값을 다시 넣어준다
        #   파이썬에서 from은 reserved word이기 때문이다
        fields = {
            "from_": "from"
        }
        schema_extra = {
            "example": {
                "code": 0,
                "message": "",
            }
        }


class DomainCreateParams(BaseModel):
    domain: str

    id : Optional[str]
    sha256: Optional[str] = ""
    first_request_time: Optional[int] = 0
    last_request_time: Optional[int] = 0



