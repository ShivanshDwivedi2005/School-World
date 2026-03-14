from .repository import StudentRepository
from .models import Student
from app.common.exceptions import BadRequestException

class StudentService:

    def __init__(self, repo: StudentRepository):
        self.repo = repo

    async def register_student(self, db, school_id, data):
        if data.admission_no:
            exists = await self.repo.admission_exists(
                db, school_id, data.admission_no
            )
            if exists:
                raise BadRequestException("Admission number already exists")

        student = Student(
            school_id=school_id,
            admission_no=data.admission_no,
            full_name=data.full_name,
            class_name=data.class_name,
            section=data.section,
            dob=data.dob,
            gender=data.gender
        )

        return await self.repo.create(db, student)
