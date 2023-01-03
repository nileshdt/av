
from fastapi import APIRouter, Depends, HTTPException, status
from rpc import UserService, UserServiceManager, AuditServiceManager
from server.message import Message
import asyncio
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from dependencies import get_token_header
from oauthlib.oauth2 import TokenExpiredError

router = APIRouter(
    prefix="/audit",
    tags=["audit"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

auManager = AuditServiceManager("localhost", '50051')


@router.post("/token")
async def signin(*, username: str, password: str, grant_type: str):
    if grant_type != "password":
        return {"error": "Unsupported grant type"}
    m = Message()
    print("sign in")
    print(username)
    print(password)

    async with auManager.open_channel() as usc:
        us = UserService(usc)
    # sign in by using username and password
        res = await us.sign_in(username, password)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
        m.token = res.jwt_token

    return m.json()
