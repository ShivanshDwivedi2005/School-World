from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
from sqlalchemy.sql import func

class SchoolRequest(Base):
    __tablename__ = "school_requests"
    __table_args__ = {"schema": "core"}

    request_id = Column(UUID(as_uuid=True), primary_key=True,server_default=func.gen_random_uuid())

    school_name = Column(String(255), nullable=False)
    education_board = Column(String(50))
    school_type = Column(String(50))
    udise = Column(String(11))

    official_email = Column(String(255), nullable=False)
    official_phone = Column(String(20), nullable=False)

    city = Column(String(100))
    state = Column(String(100))

    status = Column(String(20))
    rejection_reason = Column(Text)

    created_at = Column(TIMESTAMP)
    reviewed_at = Column(TIMESTAMP)


class School(Base):
    __tablename__ = "schools"
    __table_args__ = {"schema": "core"}

    school_id = Column(UUID(as_uuid=True), primary_key=True,server_default=func.gen_random_uuid())

    school_name = Column(String(255), nullable=False)
    education_board = Column(String(50))
    school_type = Column(String(50))

    status = Column(String(20))
    subscription_plan = Column(String(20))

    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
