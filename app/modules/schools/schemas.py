from pydantic import BaseModel, EmailStr
from uuid import UUID


class SchoolRegisterIn(BaseModel):
    school_name: str
    education_board: str | None = None
    school_type: str | None = None
    udise: str | None = None
    official_email: EmailStr
    official_phone: str
    city: str | None = None
    state: str | None = None


class SchoolRequestOut(BaseModel):
    request_id: UUID
    school_name: str
    status: str

    class Config:
        from_attributes = True
