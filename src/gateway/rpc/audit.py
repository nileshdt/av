import os
from grpclib.client import Channel
from audit_pb2 import (
    CreateAuditRequest, CreateAuditResponse, GetAuditRequest, GetAuditResponse
)
from audit_grpc import AuditsBase, AuditsStub
import asyncio
import contextlib


class AuditServiceManager:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def __aenter__(self):  # setting up a connection
        print("Setting up a connection")

    async def __aexit__(self):  # setting up a connection
        print("Closing the connection")

    @contextlib.asynccontextmanager
    async def open_channel(self):
        c = Channel(self.host, self.port)
        try:
            yield c
        finally:
            c.close()


class AuditService:
    def __init__(self, channel):
        print("Initializing the user service")
        self.host = os.environ.get('USER_HOST', 'localhost')
        self.port = os.environ.get('USER_PORT', '50053')
        self.stub = AuditsStub(channel)

    async def addAudit(self, name, description, status, type, userid) -> CreateAuditResponse:
        """
        Create new user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign up response
        :rtype: SignUpResponse
        """
        # send request to grpc server
        # async with Channel(self.host, self.port) as channel:
        #     self.stub = UsersStub(channel)
        return await self.stub.CreateAudit(CreateAuditRequest(name=name, description=description, status=status, type=type, userid=userid))
