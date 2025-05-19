from sqlalchemy import select

from .database import new_session
from .models import URLModel
from .schemas import URLPOSTschames
from .keygen import create_random_key




async def create_url_db(url: URLPOSTschames) -> URLModel:
    async with new_session() as session:

        db = URLModel(
            url_target = url.url_target,
            url_key = create_random_key()
        )

        session.add(db)
        await session.flush()
        await session.commit()
        return db


async def get_url_db_by_key(key: str) -> URLModel:
    async with new_session() as session:
        query = select(URLModel).where(URLModel.url_key == key)
        result = await session.execute(query)
        return result.scalar()