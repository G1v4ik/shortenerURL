from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .models import Model

engine = create_async_engine('sqlite+aiosqlite:///shortenerurl.db')

new_session = async_sessionmaker(
    engine, 
    expire_on_commit=False
)

async def get_session():
    async with new_session() as session:
        yield session


async def create_tables():
    async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Model.metadata.drop_all)