# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.sql import func
# from uuid import UUID
# from app.modules.schools.repository import SchoolRepository
# from app.modules.schools.models import SchoolRequest
# from app.modules.schools.schemas import SchoolRegisterIn


# class SchoolService:

#     def __init__(self, repo: SchoolRepository):
#         self.repo = repo

#     async def register(self, db: AsyncSession, data: SchoolRegisterIn):
#         req = SchoolRequest(
#             school_name=data.school_name,
#             education_board=data.education_board,
#             school_type=data.school_type,
#             udise=data.udise,
#             official_email=data.official_email,
#             official_phone=data.official_phone,
#             city=data.city,
#             state=data.state,
#             status="pending",
#             created_at=func.now()
#         )
#         return await self.repo.create_request(db, req)

#     async def pending_requests(self, db: AsyncSession):
#         return await self.repo.list_pending(db)

#     async def approve(self, db: AsyncSession, request_id: UUID):
#         req = await self.repo.get_request(db, request_id)
#         if not req:
#             raise ValueError("Request not found")
        
#         await self.repo.create_school(db, req)
#         await self.repo.delete_request(db, request_id)
#         await db.commit()

#         return {"status": "approved"}

#     async def reject(self, db: AsyncSession, request_id: UUID, reason: str):
#         req = await self.repo.get_request(db, request_id)
#         if not req:
#             raise ValueError("Request not found")

#         req.status = "rejected"
#         req.rejection_reason = reason
#         req.reviewed_at = func.now()
#         await db.commit()

#         return {"status": "rejected"}


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import func
from uuid import UUID

from app.modules.schools.repository import SchoolRepository
from app.modules.schools.models import SchoolRequest
from app.modules.schools.schemas import SchoolRegisterIn
from app.core.security import create_access_token
from app.common.exceptions import BadRequestException


class SchoolService:

    def __init__(self, repo: SchoolRepository):
        self.repo = repo

    async def register(self, db: AsyncSession, data: SchoolRegisterIn):
        req = SchoolRequest(
            school_name=data.school_name,
            education_board=data.education_board,
            school_type=data.school_type,
            udise=data.udise,
            official_email=data.official_email,
            official_phone=data.official_phone,
            city=data.city,
            state=data.state,
            status="pending",
            created_at=func.now()
        )

        return await self.repo.create_request(db, req)

    async def pending_requests(self, db: AsyncSession):
        return await self.repo.list_pending(db)

    async def approve(self, db: AsyncSession, request_id: UUID):
        req = await self.repo.get_request(db, request_id)
        if not req:
            raise BadRequestException("Request not found")

        # 1️⃣ Create school (NO commit inside repository)
        school = await self.repo.create_school(db, req)

        # 2️⃣ Delete request
        await self.repo.delete_request(db, request_id)

        # 3️⃣ Single atomic commit
        await db.commit()
        await db.refresh(school)

        # 4️⃣ Issue JWT token (CRITICAL)
        access_token = create_access_token({
            "school_id": str(school.school_id),
            "role": "school_admin"
        })

        return {
            "status": "approved",
            "school_id": school.school_id,
            "access_token": access_token
        }

    async def reject(self, db: AsyncSession, request_id: UUID, reason: str):
        req = await self.repo.get_request(db, request_id)
        if not req:
            raise BadRequestException("Request not found")

        req.status = "rejected"
        req.rejection_reason = reason
        req.reviewed_at = func.now()

        await db.commit()

        return {"status": "rejected"}
