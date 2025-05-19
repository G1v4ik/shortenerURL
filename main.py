from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import create_tables


from app.routers import router

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=False)