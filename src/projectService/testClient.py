import project_pb2 as message
from project_grpc import ProjectSvcStub
import asyncio
import logging
import grpc
from grpclib.client import Channel


# def run():
#     with grpc.insecure_channel('localhost:8081') as channel:
#         stub = service.ProjectSvcStub(channel)
#         response = stub.getProject(message.GetProjectRequest(
#             user_id="5fafcd60c4bf735022f444a7", project_id="6"))
#         # response = stub.createProject(message.CreateProjectRequest(user_id="5fafcd60c4bf735022f444a7", name="Hello"))
#         # response = stub.createTag(message.CreateTagRequest(user_id="5fafcd60c4bf735022f444a7", name="HelloTag", project_id="6"))
#     print(response)


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     run()


async def main() -> None:
    async with Channel('127.0.0.1', 50052) as channel:
        stub = ProjectSvcStub(channel)

        response = await stub.getProject(message.GetProjectRequest(
            user_id="5fafcd60c4bf735022f444a7", project_id="1"))
        # response = await stub.createProject(message.CreateProjectRequest(
        #     user_id="5fafcd60c4bf735022f444a7", name="Hello"))
        # response = await stub.createTag(message.CreateTagRequest(user_id="5fafcd60c4bf735022f444a7", name="HelloTag", project_id="1"))
    print(response)

if __name__ == '__main__':
    asyncio.run(main())
