from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from core import db_helper, settings
from fastapi.responses import ORJSONResponse
from api import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()



app = FastAPI(
    title="Academic Track",
    default_response_class=ORJSONResponse,
    lifespan=lifespan)


app.include_router(
    prefix="/api",
    router=api_v1_router
)



@app.get("/")
def hello_world():
    return {"status": 200}



if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)