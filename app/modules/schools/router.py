from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.core.database import get_db
from app.modules.schools.schemas import SchoolRegisterIn, SchoolRequestOut
from app.modules.schools.service import SchoolService
from app.modules.schools.repository import SchoolRepository

router = APIRouter(prefix="/schools", tags=["Schools"])

service = SchoolService(SchoolRepository())


@router.post("/register", response_model=SchoolRequestOut)
async def register_school(
    data: SchoolRegisterIn,
    db: AsyncSession = Depends(get_db)
):
    return await service.register(db, data)


@router.get("/requests", response_model=list[SchoolRequestOut])
async def list_requests(db: AsyncSession = Depends(get_db)):
    return await service.pending_requests(db)


@router.post("/approve/{request_id}")
async def approve_school(
    request_id: UUID,
    db: AsyncSession = Depends(get_db)
):
    return await service.approve(db, request_id)


@router.post("/reject/{request_id}")
async def reject_school(
    request_id: UUID,
    reason: str,
    db: AsyncSession = Depends(get_db)
):
    return await service.reject(db, request_id, reason)
