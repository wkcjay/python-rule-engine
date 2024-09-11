from fastapi import FastAPI, APIRouter
from api.routes import hello_world_router

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

router = APIRouter(prefix="/api")
router.include_router(hello_world_router.router)
app.include_router(router)
