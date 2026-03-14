from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import decode_access_token
from app.modules.schools.models import School


async def get_current_school(
    token: str = Depends(decode_access_token),
    db: AsyncSession = Depends(get_db)
):
    school_id = token.get("school_id")

    if not school_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid school token"
        )

    school = await db.get(School, school_id)

    if not school:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="School not found"
        )

    return school
