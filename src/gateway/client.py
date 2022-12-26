
from __future__ import print_function

import logging

import grpc
import user_pb2
import user_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50055') as channel:
        stub = user_pb2_grpc.UsersStub(channel)
        user = "achunilesh@gmail.com"
        pwd = "Welcome.123"

        registerResponse = stub.Register(user_pb2.RegisterReq(
            username=user, password=pwd))
        print("Register Response user client received: " + str(registerResponse.status) + " " +
              registerResponse.message)

        loginResponse = stub.Login(user_pb2.LoginReq(
            username=user, password=pwd))
        print("login Response user client received: " + loginResponse.jwt_token)

        validateResponse = stub.Validate(user_pb2.ValidateReq(
            jwt_token=loginResponse.jwt_token))
        print("Validate Response user client received: " +
              validateResponse.jwt_token + " " + str(validateResponse.status) + " " + validateResponse.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
