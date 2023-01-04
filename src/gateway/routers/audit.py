
from fastapi import APIRouter, Depends, HTTPException, status
from rpc import AuditService,  AuditServiceManager
from server.message import Message
from models.audit import Audit
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
    if not user_id:
        raise HTTPException(status_code=404, detail="Please provide user id")

    async with auManager.open_channel() as usc:
        us = AuditService(usc)
        print("get audits")
    return us.getAudits(user_id)


@router.get("/{audit_id}")
async def read_audit(audit_id: str):
    if not audit_id:
        raise HTTPException(status_code=404, detail="Please provide audit id")
    async with auManager.open_channel() as usc:
        us = AuditService(usc)
    print("get audit"+audit_id)
    res = await us.getAudit(audit_id)
    print(111)
    print(res)
    print(res.status)
    print(res.audit)
    print(res.message)
    print(type(res))
    aud = {"_id": res.audit._id,
           "name": res.audit.name,
           "description": res.audit.description,
           "type": res.audit.type,
           "data": res.audit.data,
           "created_at": res.audit.created_at,
           "updated_at": res.audit.updated_at}
    m = Message(True, 200,
                res.message, None, **aud)

    return m.json()


@ router.post("/")
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


@ router.put("/")
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
