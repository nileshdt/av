
from fastapi import APIRouter, Depends, HTTPException, status
from rpc import AuditService,  AuditServiceManager
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

auManager = AuditServiceManager("localhost", '50053')


@router.get("/")
async def read_audits(user_id: str):
    async with auManager.open_channel() as usc:
        us = AuditService(usc)
        print("get audits")
    return us.getAudits(user_id)


@router.get("/{audit_id}")
async def read_audit(audit_id: str):
    async with auManager.open_channel() as usc:
        us = AuditService(usc)
    return us.getAudits(audit_id)


@router.post("/")
async def create(*, name: str, description: str,  type: str, status: str, data: str, user_id: str):
    if not name:
        return {"error": "Unsupported grant type"}
    m = Message()
    print("sign in")
    async with auManager.open_channel() as usc:
        us = AuditService(usc)

    res = await us.addAudit(name, description, type, status, data, user_id)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
    return m.json()


@router.put("/")
async def update(*, id: str, name: str, description: str, type: str, status: str, data: str, user_id: str):
    if not name:
        return {"error": "Unsupported grant type"}
    m = Message()
    print("sign in")
    async with auManager.open_channel() as usc:
        us = AuditService(usc)

    res = await us.updateAudit(id, name, description, type, status, data, user_id)
    m.statusid = res.status
    m.message = res.message
    if res.status == 200:
        m.status = True
    return m.json()
