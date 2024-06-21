from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from config import settings
from core.models import db_helper



@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()



app = FastAPI(
    title="Academic Track",
    lifespan=lifespan)


@app.get("/")
def hello_world():
    return {"status": 200}



if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)