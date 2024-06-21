from fastapi import FastAPI
import uvicorn
from config import settings

app = FastAPI(title="Academic Track")


@app.get("/")
def hello_world():
    return {"status": 200}



if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)