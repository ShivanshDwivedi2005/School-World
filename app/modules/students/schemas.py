from pydantic import BaseModel
from datetime import date

class StudentCreate(BaseModel):
    admission_no: str | None = None
    full_name: str
    class_name: str
    section: str | None = None
    dob: date | None = None
    gender: str | None = None


class StudentResponse(BaseModel):
    student_id: int
    full_name: str
    class_name: str
    section: str | None

    class Config:
        from_attributes = True
