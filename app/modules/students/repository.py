from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import Student

class StudentRepository:

    async def create(self, db: AsyncSession, student: Student):
        db.add(student)
        await db.commit()
        await db.refresh(student)
        return student

    async def admission_exists(
        self, db: AsyncSession, school_id, admission_no
    ):
        if not admission_no:
            return False

        q = select(Student).where(
            Student.school_id == school_id,
            Student.admission_no == admission_no
        )
        res = await db.execute(q)
        return res.scalar_one_or_none()
