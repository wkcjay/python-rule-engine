from fastapi import APIRouter, status, Response, Request
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/hello-world", tags=["Hello World"], status_code=status.HTTP_200_OK, description="Hello World")
async def hello_world(request: Request, response: Response):
    try:
        return "hello world"
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return jsonable_encoder({'Exception': str(e)})