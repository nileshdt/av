import logging
import os
import time
from concurrent import futures
import project_pb2 as message
import project_grpc as service
from datetime import date

import asyncio
from grpclib.utils import graceful_exit
from grpclib.server import Server, Stream
import grpc
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Date, exc, ForeignKey


load_dotenv(verbose=True)
engine = create_engine(os.getenv("DB_URI"), echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
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


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    user_id = Column(String(50))
    created_at = Column(Date)

    def __repr__(self):
        return "<Project(id='%s', name='%s', user_id='%s')>" % (self.id, self.name, self.user_id)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    user_id = Column(String(50))
    created_at = Column(Date)

    def __repr__(self):
        return "<Tag(id='%s', name='%s', user_id='%s', project_id='%s')>" % (self.id, self.name, self.user_id, self.project_id)


def create_tables():
    try:
        Project.__table__.create(engine)
    except exc.OperationalError:
        logging.info("Projects table already created")

    try:
        Tag.__table__.create(engine)
    except exc.OperationalError:
        logging.info("Tags table already created")
    Project.tags = relationship(Tag, backref='tags')


class API(service.ProjectSvcBase):

    async def createProject(self, stream: Stream[message.CreateProjectRequest, message.ProjectResponse]):
        request = await stream.recv_message()
        assert request is not None
        print("Validate request received")
        project = Project(name=request.name,
                          user_id=request.user_id, created_at=date.today())
        session.add(project)
        session.commit()
        db_project = session.query(Project).filter_by(
            name=request.name).first()
        return await stream.send_message(message.ProjectResponse(id=str(db_project.id), name=db_project.name))

    async def createTag(self, stream: Stream[message.CreateTagRequest, message.TagResponse]):
        request = await stream.recv_message()
        assert request is not None
        db_project = session.query(Project).filter_by(
            id=request.project_id).first()
        tag = Tag(name=request.name, project_id=db_project.id,
                  user_id=request.user_id, created_at=date.today())
        session.add(tag)
        session.commit()

        db_tag = session.query(Tag).filter_by(
            name=request.name, project_id=request.project_id).first()
        res = message.TagResponse(
            id=str(db_tag.id), name=db_tag.name, project_id=str(db_tag.project_id))
        return await stream.send_message(res)

    async def getProject(self, stream: Stream[message.GetProjectRequest, message.ProjectResponse]):
        request = await stream.recv_message()
        assert request is not None
        db_project = session.query(Project).filter_by(
            id=request.project_id).first()
        db_tags = session.query(Tag).filter_by(
            project_id=request.project_id).all()

        list_tags_resp = []
        for tag in db_tags:
            tag_message = message.TagResponse(
                id=str(tag.id), name=tag.name, project_id=str(tag.project_id))
            list_tags_resp.append(tag_message)

        project = message.ProjectResponse(
            id=str(db_project.id), name=db_project.name, tags=list_tags_resp)
        return await stream.send_message(project)


async def main(*, host: str = '127.0.0.1', port: int = 50072) -> None:
    print("Starting server")
    await connect_db()
    print("Connected to DB")
    create_tables()
    print("Created tables")
    server = Server([API()])
    print("Created server")
    # Note: graceful_exit isn't supported in Windows
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
