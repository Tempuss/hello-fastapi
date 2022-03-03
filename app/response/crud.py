from pydantic import BaseModel


class CreateResponse(BaseModel):
    id: str
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
                "id": "",
                "message": "",
            }
        }
