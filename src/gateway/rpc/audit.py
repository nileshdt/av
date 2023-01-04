import os
from grpclib.client import Channel
from audit_pb2 import (
    CreateAuditRequest, CreateAuditResponse,
    GetAuditRequest, GetAuditResponse,
    UpdateAuditRequest, UpdateAuditResponse,
    DeleteAuditRequest, DeleteAuditResponse,
    GetAuditsRequest, GetAuditsResponse
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
        self.host = os.environ.get('AUDIT_HOST', 'localhost')
        self.port = os.environ.get('AUDIT_PORT', '50053')
        self.stub = AuditsStub(channel)

    async def addAudit(self, name, description, status, type, data, userid) -> CreateAuditResponse:
        """
        Add new audit by using audit name, description, status, type, data and user id
        :param str name: audit name
        :param str description: audit description
        :param str status: audit status
        :param str type: audit type
        :param str data: audit data
        :param str userid: user id
        :return: sign up response
        :rtype: SignUpResponse
        """
        return await self.stub.CreateAudit(
            CreateAuditRequest(name=name,
                               description=description,  type=type, status=status, data=data, created_by=userid
                               ))

    async def getAudit(self, auditid) -> GetAuditResponse:
        """
        Get audit details by using audit id

        :param str username: audit id
        :return: Get audit response
        :rtype: GetAuditResponse
        """

        print("get audit 1" + auditid)
        res = await self.stub.GetAudit(
            GetAuditRequest(_id=auditid
                            ))
        print(res.status, res.message, res.audit)
        return res

    async def getAudits(self, userid) -> GetAuditsResponse:
        """
        Get audit details by using user id

        :param str username: user id
        :return: Get audit response
        :rtype: GetAuditsResponse
        """
        return await self.stub.GetAudits(
            GetAuditsRequest(created_by=userid
                             ))

    async def updateAudit(self, auditid, name, description, status, type, data, userid) -> UpdateAuditResponse:
        """
        update audit by using audit id, name, description, status, type, data and user id

        :param str auditid: audit id
        :param str name: audit name
        :param str description: audit description
        :param str status: audit status
        :param str type: audit type
        :param str data: audit data
        :param str userid: user id
        :return: sign up response
        """
        return await self.stub.UpdateAudit(
            UpdateAuditRequest(_id=auditid, name=name,
                               description=description, status=status, type=type, created_by=userid
                               ))

    async def deleteAudit(self, auditid) -> DeleteAuditResponse:
        """
        Delete audit by using audit id

        :param str auditid: audit id
        :return DeleteAuditResponse
        :rtype: DeleteAuditResponse
        """
        # send request to grpc server
        # async with Channel(self.host, self.port) as channel:
        #     self.stub = UsersStub(channel)
        return await self.stub.DeleteAudit(
            DeleteAuditRequest(_id=auditid
                               ))
