import logging
import os
import time

import asyncio
from grpclib.utils import graceful_exit
from grpclib.server import Server, Stream
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
import api
import model

load_dotenv(verbose=True)
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
engine = create_engine(os.getenv("DB_URI"), echo=False)
Session = sessionmaker(bind=engine)
session = Session()

print(os.getenv("DB_URI"))
i = 0


async def connect_db():
    global i
    if i > 10:
        quit()
    try:
        conn = engine.connect()
    except OperationalError:
        time.sleep(1)
        i = i + 1
        await connect_db()
    except Exception as e:
        logging.error(e)
        print(e)
        quit()


async def main(*, host: str = HOST, port: int = PORT) -> None:
    print("Starting server")
    await connect_db()
    print("Connected to DB")
    model.create_tables()
    print("Created tables")
    server = Server([api.API()])
    print("Created server")
    # Note: graceful_exit isn't supported in Windows
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
