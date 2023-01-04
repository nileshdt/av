from fastapi import Header, HTTPException
import os
# from rpc import UserService, UserServiceManager
USER_HOST = os.environ.get("USER_HOST", "localhost")
USER_PORT = os.environ.get("USER_PORT", "50051")
# usManager = UserServiceManager(USER_HOST, USER_PORT)


async def get_token_header(x_token: str = Header()):
    if x_token != "faketoken":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(
            status_code=400, detail="No Jessica token provided")


# async def validate_token(token: str):
#     if not token:
#         raise HTTPException(
#             status_code=400, detail="No token provided")
#     try:
#         async with usManager.open_channel() as usc:
#             us = UserService(usc)
#             res = await us.validate(token)
#     except TokenExpiredError:
#         raise HTTPException(
#             status_code=400, detail="Token has expired")
