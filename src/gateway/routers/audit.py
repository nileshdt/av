
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
        res = await us.getAudits(user_id)

        audits = []
        for audit in res.audits:
            audits.append({"_id": audit._id,
                           "name": audit.name,
                           "description": audit.description,
                           "type": audit.type,
                           "data": audit.data,
                           "status": audit.status,
                           "created_at": audit.created_at,
                           "updated_at": audit.updated_at})
        d_audits = dict(audits=audits)
        m = Message(200,
                    res.message, None, **d_audits)
    return m.json()


@router.get("/{audit_id}")
async def read_audit(audit_id: str):
    if not audit_id:
        raise HTTPException(status_code=404, detail="Please provide audit id")
    async with auManager.open_channel() as usc:
        us = AuditService(usc)

    res = await us.getAudit(audit_id)
    aud = {"_id": res.audit._id,
           "name": res.audit.name,
           "description": res.audit.description,
           "type": res.audit.type,
           "data": res.audit.data,
           "status": res.audit.status,
           "created_at": res.audit.created_at,
           "created_by": res.audit.created_by,
           "updated_at": res.audit.updated_at,
           "updated_by": res.audit.updated_by}
    m = Message(200,
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
