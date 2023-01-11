import logging
import project_pb2 as message
import project_grpc as service
from model import Project, Tag
from datetime import date
from service import session
from grpclib.server import Server, Stream


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
