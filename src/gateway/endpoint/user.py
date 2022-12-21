from flask import Blueprint, request
from rpc import UserService
from server import app
from server.message import Message

user = Blueprint('user', app.name)


@user.post('/sign-up')
def sign_up():
    """
    Create new user account

    :rtype: flask.Response
    """
    print("sign up")
    m = Message()
    auth = request.authorization
    # username = request.args.get('Username')
    # password = request.args.get('Password')
    print(auth.username)
    us = UserService()

    # sign up by using username and password
    res = us.sign_up(auth.username)

    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True

    return m.json()


@user.post('/sign-in')
def sign_in():
    """
    Sign in to user account

    :rtype: flask.Response
    """
    m = Message()
    print("sign in")
    auth = request.authorization
    # username = request.args.get('Username')
    # password = request.args.get('Password')
    print(auth.username)
    us = UserService()

    # sign in by using username and password
    res = us.sign_in(auth.username, auth.password)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
        m.token = res.jwt_token

    return m.json()


@user.post('/validate')
def validate():
    """
    Validate token

    :rtype: flask.Response
    """
    token = request.headers["Authorization"]
    if not token:
        return "missing credentials", 401
    token = token.split(" ")[1]

    m = Message()
    us = UserService()

    # validate token
    res = us.validate(token)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True

    return m.json()
