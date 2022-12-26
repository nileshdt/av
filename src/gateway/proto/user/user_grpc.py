# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: protos/user/user.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import protos.user.user_pb2


class UsersBase(abc.ABC):

    @abc.abstractmethod
    async def Login(self, stream: 'grpclib.server.Stream[protos.user.user_pb2.LoginReq, protos.user.user_pb2.LoginRsp]') -> None:
        pass

    @abc.abstractmethod
    async def Register(self, stream: 'grpclib.server.Stream[protos.user.user_pb2.RegisterReq, protos.user.user_pb2.RegisterRsp]') -> None:
        pass

    @abc.abstractmethod
    async def Validate(self, stream: 'grpclib.server.Stream[protos.user.user_pb2.ValidateReq, protos.user.user_pb2.ValidateRsp]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/users.Users/Login': grpclib.const.Handler(
                self.Login,
                grpclib.const.Cardinality.UNARY_UNARY,
                protos.user.user_pb2.LoginReq,
                protos.user.user_pb2.LoginRsp,
            ),
            '/users.Users/Register': grpclib.const.Handler(
                self.Register,
                grpclib.const.Cardinality.UNARY_UNARY,
                protos.user.user_pb2.RegisterReq,
                protos.user.user_pb2.RegisterRsp,
            ),
            '/users.Users/Validate': grpclib.const.Handler(
                self.Validate,
                grpclib.const.Cardinality.UNARY_UNARY,
                protos.user.user_pb2.ValidateReq,
                protos.user.user_pb2.ValidateRsp,
            ),
        }


class UsersStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Login = grpclib.client.UnaryUnaryMethod(
            channel,
            '/users.Users/Login',
            protos.user.user_pb2.LoginReq,
            protos.user.user_pb2.LoginRsp,
        )
        self.Register = grpclib.client.UnaryUnaryMethod(
            channel,
            '/users.Users/Register',
            protos.user.user_pb2.RegisterReq,
            protos.user.user_pb2.RegisterRsp,
        )
        self.Validate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/users.Users/Validate',
            protos.user.user_pb2.ValidateReq,
            protos.user.user_pb2.ValidateRsp,
        )
