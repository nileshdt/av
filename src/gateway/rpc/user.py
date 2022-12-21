import os
import grpc
from proto.user import (
    UsersStub, LoginReq, LoginRsp, RegisterReq, RegisterRsp, ValidateReq, ValidateRsp
)


class UserService:
    def __init__(self):
        host = os.environ.get('USER_HOST', 'localhost:50055')
        channel = grpc.insecure_channel(host)

        self.stub = UsersStub(channel)

    def sign_up(self, username, password) -> RegisterRsp:
        """
        Create new user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign up response
        :rtype: SignUpResponse
        """
        r = RegisterReq(username=username, password=password)

        # send request to grpc server
        return self.stub.Register(r)

    def sign_in(self, username, password) -> LoginRsp:
        """
        Sign in to user account by using username and password

        :param str username: user name
        :param str password: password
        :return: sign in response
        :rtype: SignInResponse
        """
        r = LoginReq(username=username, password=password)

        # send request to grpc server
        return self.stub.Login(r)

    def validate(self, token) -> ValidateRsp:
        """
        Validate token

        :param str token: jwt token
        :return: validate response
        :rtype: ValidateRsp
        """
        r = ValidateReq(token=token)

        # send request to grpc server
        return self.stub.Validate(r)
