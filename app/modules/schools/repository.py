from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.sql import func
from uuid import UUID

from app.modules.schools.models import SchoolRequest, School


class SchoolRepository:

    async def create_request(self, db: AsyncSession, req: SchoolRequest):
        db.add(req)
        await db.commit()
        await db.refresh(req)
        return req

    async def list_pending(self, db: AsyncSession):
        result = await db.execute(
            select(SchoolRequest).where(SchoolRequest.status == "pending")
        )
        return result.scalars().all()

    async def get_request(self, db: AsyncSession, request_id: UUID):
        result = await db.execute(
            select(SchoolRequest).where(SchoolRequest.request_id == request_id)
        )
        return result.scalar_one_or_none()

    async def delete_request(self, db: AsyncSession, request_id: UUID):
        await db.execute(
            delete(SchoolRequest).where(SchoolRequest.request_id == request_id)
        )

    async def create_school(self, db: AsyncSession, req: SchoolRequest):
        school = School(
            school_name=req.school_name,
            education_board=req.education_board,
            school_type=req.school_type,
            status="active",
            subscription_plan="free",
            created_at=func.now(),
            updated_at=func.now()
        )
        db.add(school)
