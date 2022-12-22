import os
import grpc
import asyncio
import contextlib
from proto.user import (
    UsersStub, LoginReq, LoginRsp, RegisterReq, RegisterRsp, ValidateReq, ValidateRsp
)


class UserService:
    def _init_(self):  # initializing the object
        self.host = host = os.environ.get('USER_HOST', 'localhost:50055')

    async def _aenter_(self):  # setting up a connection
        self.conn = await grpc.insecure_channel(self.host)
        return self.conn

    async def _aexit_(self, exc_type, exc, tb):  # closing the connection
        await self.conn.close()

    @contextlib.asynccontextmanager
    async def sign_up(self, username, password) -> RegisterRsp:
        """
        Create new user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign up response
        :rtype: SignUpResponse
        """

        r = RegisterReq(username=username, password=password)
        # send request to grpc server
        return await self.stub.Register(r)

    @contextlib.asynccontextmanager
    async def sign_in(self, username, password) -> LoginRsp:
        """
        Sign in to user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign in response
        :rtype: SignInResponse
        """
        host = os.environ.get('USER_HOST', 'localhost:50055')
        async with grpc.insecure_channel(host) as channel:
            self.stub = UsersStub(channel)

            r = LoginReq(username=username, password=password)

        # send request to grpc server
        return await self.stub.Login(r)

    @contextlib.asynccontextmanager
    async def validate(self, token) -> ValidateRsp:
        """
        Validate token

        :param str token: jwt token
        :return: validate response
        :rtype: ValidateRsp
        """
        host = os.environ.get('USER_HOST', 'localhost:50055')
        async with grpc.insecure_channel(host) as channel:
            self.stub = UsersStub(channel)

        r = ValidateReq(jwt_token=token)

        # send request to grpc server
        return await self.stub.Validate(r)
