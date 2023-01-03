import asyncio
import jwt
import os
import datetime
from grpclib.utils import graceful_exit
from grpclib.server import Server, Stream
import pymysql.connections

# generated by protoc
from user_pb2 import LoginReq, LoginRsp, RegisterReq, RegisterRsp, ValidateReq, ValidateRsp
from user_grpc import UsersBase


# MYSQL_HOST = 'localhost'
# MYSQL_DB = 'auth'
# MYSQL_USER = 'auth_user'
# MYSQL_PASSWORD = 'Auth123'
# MYSQL_PORT = '3306'
MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
MYSQL_USER = os.environ.get("MYSQL_USER", "auth_user")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "Auth123")
MYSQL_DB = os.environ.get("MYSQL_DB", "auth")
MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
# MYSQL_PORT = int(MYSQL_PORT)

conn = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    db=MYSQL_DB,
    port=3306,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

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


class Users(UsersBase):

    async def Login(self, stream: Stream[LoginReq, LoginRsp]) -> None:
        request = await stream.recv_message()
        assert request is not None
        message = f'Hello, {request.username}!'
        if request.username == "" or request.password == "":
            await stream.send_message(LoginRsp(jwt_token="",
                                               expiration="2020-01-01", status=401, message="Invalid credentials"))
        print("Login request received")
        print(request.username)
        try:
            with conn.cursor() as cur:
                res = cur.execute(
                    "select email, password from user where email=%s",
                    (request.username,))
                if res > 0:
                    user_row = cur.fetchone()
                    email = user_row['email']
                    password = user_row['password']
                    print(email, password)
                    print(request.username, request.password)
                    if request.username != email or request.password != password:
                        await stream.send_message(LoginRsp(status=401, message="Invalid credentials"
                                                           ))
                    else:
                        jwt_token = createJWT(request.username,
                                              "sarcasm", True)
                print(jwt_token)
        except Exception as e:
            print(e)

        # with server.app_context():
        #     cur = mysql.connection.cursor()

        #     res = cur.execute(
        #         "select email, password from user where email=%s",
        #         (request.username,))
        #     if res > 0:
        #         user_row = cur.fetchone()
        #         email = user_row[0]
        #         password = user_row[1]
        #         print(email, password)
        #         print(request.username, request.password)
        #         if request.username != email or request.password != password:
        #             await stream.send_message(LoginRsp(status=401, message="Invalid credentials"
        #                                                ))
        #         else:
        #             jwt_token = createJWT(request.username,
        #                                   "sarcasm", True)
        #     print(jwt_token)

        await stream.send_message(LoginRsp(jwt_token=jwt_token, status=200, message="Login successful",
                                           expiration="2020-01-01"))

    async def Register(self, stream: Stream[RegisterReq, RegisterRsp]) -> None:
        print("Register request received")
        request = await stream.recv_message()
        assert request is not None
        message = f'Hello, {request.username}!'
        print(request.username, request.password)

        if request.username == "" or request.password == "":
            await stream.send_message(RegisterRsp(status=400, message="Username or password cannot be empty"))
        with conn.cursor() as cur:
            print("Connected to DB")

            res = cur.execute(
                "select email, password from user where email=%s",
                (request.username,))
            print("Query executed")
            if res > 0:
                print("User already exists")
                await stream.send_message(RegisterRsp(status=409, message="User already exists"))
            else:
                print("Inserting user")
                cur.execute(
                    "insert into user(email, password) values(%s, %s)",
                    (request.username, request.password))
                conn.commit()
                print("User inserted")
                cur.close()
                return await stream.send_message(RegisterRsp(status=200, message="User created"))

    async def Validate(self, stream: Stream[ValidateReq, ValidateRsp]) -> None:
        request = await stream.recv_message()
        assert request is not None
        print("Validate request received")
        print(request.jwt_token)
        try:
            jwt_token = jwt.decode(
                request.jwt_token, "sarcasm", algorithms=["HS256"])
            print(jwt_token)
            await stream.send_message(ValidateRsp(status=200, message="Valid token"))
        except jwt.ExpiredSignatureError:
            await stream.send_message(ValidateRsp(status=401, message="Token expired"))
        except jwt.InvalidTokenError:
            await stream.send_message(ValidateRsp(status=401, message="Invalid token"))


def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.utcnow(),
            "admin": authz,
        },
        secret,
        algorithm="HS256",
    )


async def main(*, host: str = '127.0.0.1', port: int = 50052) -> None:
    server = Server([Users()])
    # Note: graceful_exit isn't supported in Windows
    with graceful_exit([server]):
        await server.start(host, port)
        print(f'Serving on {host}:{port}')
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
