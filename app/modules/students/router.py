from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.dependencies import get_current_school
from .schemas import StudentCreate, StudentResponse
from .service import StudentService
from .repository import StudentRepository

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=StudentResponse)
async def register_student(
    payload: StudentCreate,
    db: AsyncSession = Depends(get_db),
    school = Depends(get_current_school)
):
    service = StudentService(StudentRepository())
    return await service.register_student(db, school.school_id, payload)
