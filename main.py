from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from app.database import create_tables, delete_tables
from app.schemas import URLPOSTschames
from app.crud import create_url_db, get_url_db_by_key

from app.routers import router

import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    # await delete_tables()


app = FastAPI(lifespan=lifespan)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)