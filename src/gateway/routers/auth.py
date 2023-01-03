
from fastapi import APIRouter, Depends, HTTPException, status
from rpc import UserService, UserServiceManager
from server.message import Message
import asyncio
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from dependencies import get_token_header
from oauthlib.oauth2 import TokenExpiredError

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}
usManager = UserServiceManager("localhost", '50051')


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


@router.post("/signup")
async def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    print("sign up")
    m = Message()
    print(form_data.username)
    async with usManager.open_channel() as usc:
        us = UserService(usc)
        res = await us.sign_up(form_data.username, form_data.password)

    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True

    return m.json()


@router.post("/token")
async def signin(*, username: str, password: str, grant_type: str):
    if grant_type != "password":
        return {"error": "Unsupported grant type"}
    m = Message()
    print("sign in")
    print(username)
    print(password)

    async with usManager.open_channel() as usc:
        us = UserService(usc)
    # sign in by using username and password
        res = await us.sign_in(username, password)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
        m.token = res.jwt_token

    return m.json()


@router.post("/me")
async def read_me(*, authorization: str = Depends(oauth2_scheme)):

    m = Message()

    # validate token
    try:
        async with usManager.open_channel() as usc:
            us = UserService(usc)
            res = await us.validate(authorization)
    except TokenExpiredError:
        return {"error": "Token has expired"}
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
    return m.json()
