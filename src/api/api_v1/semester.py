from typing import Annotated, TYPE_CHECKING
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from core import db_helper
from core.models import Semester
from core.schemas import SemesterRead


router = APIRouter(prefix="/semester", tags=["Semester"])


@router.get("/get/")
async def get_semesters(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1),
):
    stmt = select(Semester).offset(skip).limit(limit)
    result = await session.scalars(stmt)
    return result.all()
