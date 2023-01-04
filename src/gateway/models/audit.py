from datetime import datetime
from pydantic import BaseModel


class Audit(BaseModel):
    id: str
    name: str
    description: str
    type: str
    status: str
    data: str
    user_id: str
    created_at: datetime
    modified_at: datetime
    created_by: str
    modified_by: str
