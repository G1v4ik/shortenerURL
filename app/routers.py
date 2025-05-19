
from fastapi import FastAPI, APIRouter
from app.schemas import URLPOSTschames, URLGETschemas
from app.crud import create_url_db, get_url_db_by_key


router = APIRouter(
    prefix="/urls",
    tags=["URLS"],
)


@router.post("/")
async def create_urls(url: URLPOSTschames):
    new_url_db = await create_url_db(url=url)
    return new_url_db

@router.get("/{url_key}", status_code=307)
async def get_url_by_url_key(url_key: str):
    get_url_by_key = await get_url_db_by_key(key=url_key)
    return get_url_by_key