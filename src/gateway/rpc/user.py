import os
from grpclib.client import Channel
from ..proto.user import (
    UsersStub, LoginReq, LoginRsp, RegisterReq, RegisterRsp, ValidateReq, ValidateRsp
)
import asyncio
import contextlib

# @contextmanager
# def db() -> UserServiceChannel:
#     db_session = UserServiceChannel()
#     try:
#         yield db_session.stub
#     finally:
#         db_session.stub.close()


class UserServiceManager:
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


# class UserServiceChannel:
#     # def __init__(self):
#     #     with Channel(self.host, self.port) as channel:
#     #         self.channel = channel
#     #     return self

#     def __enter__(self):  # setting up a connection
#         async with Channel(self.host, self.port) as channel:
#             self.stub = await UsersStub(channel)
#         return self

#     def __exit__(self):  # setting up a connection
#         self.stub.close()
    # async def __aenter__(self):  # setting up a connection
    #     async with Channel(self.host, self.port) as channel:
    #         self.stub = await UsersStub(channel)
    #     return self

    # async def __aexit__(self):  # setting up a connection
    #     self.stub.close()


class UserService:
    def __init__(self, channel):
        print("Initializing the user service")
        self.host = os.environ.get('USER_HOST', 'localhost')
        self.port = os.environ.get('USER_PORT', '50051')
        self.stub = UsersStub(channel)
        # with Channel(self.host, self.port) as channel:
        #     self.stub = UsersStub(channel)
        # print("host: ", self.host)
        # print("port: ", self.port)

    # def __enter__(self):  # setting up a connection
    #     with Channel(self.host, self.port) as channel:
    #         self.stub = UsersStub(channel)

    # def __exit__(self):  # setting up a connection
    #     self.stub.close()

    # async def __aenter__(self):  # setting up a connection
    #     print("Initializing async the user service")
    #     self.host = os.environ.get('USER_HOST', 'localhost')
    #     self.port = os.environ.get('USER_PORT', '50051')
    #     async with Channel(self.host, self.port) as channel:
    #         self.stub = UsersStub(channel)

    # async def __aexit__(self, exc_type, exc, tb):  # closing the connection
    #     # await self.stub.close()
    #     # self.host = ""
    #     print("Closing async the user service")

    async def sign_up(self, username, password) -> RegisterRsp:
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
        # async with Channel(self.host, self.port) as channel:
        #     self.stub = UsersStub(channel)
        # async with Channel(self.host, self.port) as channel:
        #     self.stub = UsersStub(channel)
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
        # async with Channel(self.host, self.port) as channel:
        # self.stub = UsersStub(channel)
        return await self.stub.Validate(ValidateReq(jwt_token=token))
