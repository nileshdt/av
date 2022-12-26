import os
import grpc
import asyncio
import contextlib
from grpclib.client import Channel
from ..proto.user import (
    UsersStub, LoginReq, LoginRsp, RegisterReq, RegisterRsp, ValidateReq, ValidateRsp
)


class UserService:
    def __init__(self):
        print("Initializing the user service")
        self.host = os.environ.get('USER_HOST', 'localhost')
        self.port = os.environ.get('USER_PORT', '50051')
        print("host: ", self.host)
        print("port: ", self.port)

   # async def _aenter_(self):  # setting up a connection

   # async def _aexit_(self, exc_type, exc, tb):  # closing the connection
   #     await self.stub.close()
    async def sign_up(self, username, password) -> RegisterRsp:
        """
        Create new user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign up response
        :rtype: SignUpResponse
        """
        # send request to grpc server
        async with Channel(self.host, self.port) as channel:
            self.stub = UsersStub(channel)
        return await self.stub.Register(RegisterReq(username=username, password=password))

    async def sign_in(self, username, password) -> LoginRsp:
        """
        Sign in to user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign in response
        :rtype: SignInResponse
        """
        # host = os.environ.get('USER_HOST', 'localhost:50055')
        # async with grpc.insecure_channel(host) as channel:
        #     self.stub = UsersStub(channel)

        # send request to grpc server
        print("username: ", username)
        print("password: ", password)
        async with Channel(self.host, self.port) as channel:
            self.stub = UsersStub(channel)
        print("stub: ", self.stub)
        return await self.stub.Login(LoginReq(username=username, password=password))

    async def validate(self, token) -> ValidateRsp:
        """
        Validate token

        :param str token: jwt token
        :return: validate response
        :rtype: ValidateRsp
        """
        # host = os.environ.get('USER_HOST', 'localhost:50055')
        # async with grpc.insecure_channel(host) as channel:
        #     self.stub = UsersStub(channel)

        # send request to grpc server
        async with Channel(self.host, self.port) as channel:
            self.stub = UsersStub(channel)
        return await self.stub.Validate(ValidateReq(jwt_token=token))
