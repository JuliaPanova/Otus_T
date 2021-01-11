import asyncio
from aiohttp import ClientSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Task_3.model import base, Post

db_string = "postgres://Julia:OtusOtus@localhost:5432/OtusJulia"
db = create_engine(db_string)

base.metadata.create_all(db)

Session = sessionmaker(db)
sql_session = Session()


BASE_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch(session: ClientSession, url: str) -> dict:
    """
    Fetching data from URL
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_post(base_url, id):
    """
    Fetching post using base_url and id
    :param base_url:
    :param id:
    :return:
    """

    async with ClientSession() as session:
        result = await fetch(session, f'{base_url}/{id}')
    return result


async def get_posts():
    """
    Getting posts from API and writing them to database
    :return:
    """
    done, pending = await asyncio.wait(
        [fetch_post(BASE_URL, id) for id in range(1, 25)],
        timeout=5,
        return_when=asyncio.ALL_COMPLETED
    )
    for task in done:
        post_data = task.result()
        post = Post(**post_data)
        if sql_session.query(Post).filter_by(id=post.id).scalar() is None:
            sql_session.add(post)

    sql_session.commit()
    sql_session.close()

    print('done.')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(get_posts())
        loop.run_until_complete(asyncio.sleep(2.0))
    finally:
        loop.close()

