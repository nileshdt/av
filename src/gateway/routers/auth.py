
from fastapi import APIRouter, Depends, HTTPException, status
from ..rpc import UserService
from ..server.message import Message
import asyncio
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from ..dependencies import get_token_header

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

us = UserService()


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
    # auth = request.authorization
    print(form_data.username)
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

    # sign in by using username and password
    res = await us.sign_in(username, password)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
        m.token = res.jwt_token

    return m.json()


# @app.get("/users/me")
# async def read_users_me(*, authorization: str = Depends(oauth2_scheme)):
#     try:
#         payload = verify_token(authorization)
#     except TokenExpiredError:
#         return {"error": "Token has expired"}
#     user = get_current_user(payload)
#     return user