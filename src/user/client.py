import asyncio

from grpclib.client import Channel

# generated by protoc
from user_pb2 import LoginReq, LoginRsp, RegisterReq, RegisterRsp, ValidateReq, ValidateRsp
from user_grpc import UsersStub


async def main() -> None:
    async with Channel('127.0.0.1', 50052) as channel:
        user = UsersStub(channel)

        reply = await user.Register(RegisterReq(username="nileshdt@gmail.com", password="Welcome.123"))
        print(reply.message)
        reply = await user.Login(LoginReq(username="nileshdt@gmail.com", password="Welcome.123"))
        token = reply.jwt_token
        print(token)
        print(reply.message)
        reply = await user.Validate(ValidateReq(jwt_token=token))
        print(reply.message)


if __name__ == '__main__':
    asyncio.run(main())
