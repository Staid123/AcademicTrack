from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Semester
from core import db_helper
from crud import semesters_crud


async def semester_by_id(
    semester_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_getter),
) -> Semester:
    semester = await semesters_crud.get_semester(session=session, semester_id=semester_id)
    if semester is not None:
        return semester
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Semester {semester_id} not found!",
    )