
# from concurrent import futures
# import logging
# import datetime
# import jwt
# import os
# from flask import Flask, request
# from flask_mysqldb import MySQL
# import grpc
# import user_pb2
# import user_pb2_grpc
# import asyncio
# from grpclib.utils import graceful_exit
# from grpclib.server import Server

# server = Flask(__name__)

# # config
# # os.environ.get("MYSQL_HOST")
# server.config["MYSQL_HOST"] = "localhost"
# # os.environ.get("MYSQL_USER")
# server.config["MYSQL_USER"] = "auth_user"
# # os.environ.get("MYSQL_PASSWORD")
# server.config["MYSQL_PASSWORD"] = "Auth123"
# server.config["MYSQL_DB"] = "auth"  # os.environ.get("MYSQL_DB")
# server.config["MYSQL_PORT"] = "3306"  # os.environ.get("MYSQL_PORT")

# server.config["MYSQL_PORT"] = int(server.config["MYSQL_PORT"])

# mysql = MySQL(server)


# class Users(user_pb2_grpc.UsersServicer):

#     async def Login(self, request, context):
#         if request.username == "" or request.password == "":
#             return await user_pb2.LoginRsp(jwt_token="",
#                                            expiration="2020-01-01", status=401, message="Invalid credentials")
#         print("Login request received")
#         print(request.username)
#         with server.app_context():
#             cur = mysql.connection.cursor()

#             res = cur.execute(
#                 "select email, password from user where email=%s",
#                 (request.username,))
#             if res > 0:
#                 user_row = await cur.fetchone()
#                 email = user_row[0]
#                 password = user_row[1]
#                 print(email, password)
#                 print(request.username, request.password)
#                 if request.username != email or request.password != password:
#                     return await user_pb2.LoginRsp(status=401, message="Invalid credentials"
#                                                    )
#                 else:
#                     jwt_token = createJWT(request.username,
#                                           "sarcasm", True)

#             print(jwt_token)
#         return await user_pb2.LoginRsp(jwt_token=jwt_token, status=200, message="Login successful",
#                                        expiration="2020-01-01")

#     async def Register(self, request, context):

#         print("Register request received")
#         print(request.username, request.password)
#         if request.username == "" or request.password == "":
#             return await user_pb2.RegisterRsp(status=400, message="Username or password cannot be empty")
#         with server.app_context():
#             cur = mysql.connection.cursor()
#             print("Connected to DB")

#             res = await cur.execute(
#                 "select email, password from user where email=%s",
#                 (request.username,))
#             print("Query executed")
#             if res > 0:
#                 print("User already exists")
#                 return await user_pb2.RegisterRsp(status=409, message="User already exists")
#             else:
#                 print("Inserting user")
#                 await cur.execute(
#                     "insert into user(email, password) values(%s, %s)",
#                     (request.username, request.password))
#                 mysql.connection.commit()
#                 print("User inserted")
#                 cur.close()
#         return await user_pb2.RegisterRsp(status=200, message="User created"
#                                           )

#     async def Validate(self, request, context):

#         print("Validate request received")
#         print(request.jwt_token)
#         with server.app_context():
#             try:
#                 jwt_token = jwt.decode(
#                     request.jwt_token, "sarcasm", algorithms=["HS256"])
#                 print(jwt_token)
#             except jwt.ExpiredSignatureError:
#                 return await user_pb2.ValidateRsp(status=401, message="Token expired")
#             except jwt.InvalidTokenError:
#                 return await user_pb2.ValidateRsp(status=401, message="Invalid token")
#         return await user_pb2.ValidateRsp(status=200, message="Valid token",)


# def createJWT(username, secret, authz):
#     return jwt.encode(
#         {
#             "username": username,
#             "exp": datetime.datetime.now(tz=datetime.timezone.utc)
#             + datetime.timedelta(days=1),
#             "iat": datetime.datetime.utcnow(),
#             "admin": authz,
#         },
#         secret,
#         algorithm="HS256",
#     )


# async def serve(*, host='127.0.0.1', port=50055):
#     server = Server([Users()])
#     # server = grpc.aio.server()
#     # user_pb2_grpc.add_UsersServicer_to_server(Users(), server)
#     listen_addr = '[::]:50055'
#     with graceful_exit([server]):
#         # await server.add_insecure_port(listen_addr)
#         logging.info("Starting server on %s", listen_addr)
#         await server.start(host, port)
#         # await server.wait_for_termination()
#         await server.wait_closed()

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     asyncio.run(serve())
