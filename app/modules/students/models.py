from sqlalchemy import Column, BigInteger, String, Date, CHAR, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"
    __table_args__ = {"schema": "academics"}

    student_id = Column(BigInteger, primary_key=True, index=True)
    school_id = Column(ForeignKey("core.schools.school_id"), nullable=False)

    admission_no = Column(String(50))
    full_name = Column(String(255), nullable=False)

    class_name = Column("class", String(20))
    section = Column(String(10))

    dob = Column(Date)
    gender = Column(CHAR(1))

    status = Column(String(20), default="active")
    created_at = Column(TIMESTAMP, server_default=func.now())
