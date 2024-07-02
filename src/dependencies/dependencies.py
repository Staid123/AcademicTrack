from fastapi import HTTPException, Path, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Callable, Annotated
from core import db_helper
from crud import (
    students_crud, semesters_crud,
    groups_crud, teachers_crud, 
    subjects_crud, lessons_crud, 
    daily_schedules_crud, weekly_schedules_crud, 
    grades_crud
)
from exceptions import (
    semester_not_found, student_not_found, 
    group_not_found, teacher_not_found, 
    subject_not_found, lesson_not_found, 
    daily_schedule_not_found, weekly_schedule_not_found,
    grade_not_found
)

def create_get_by_id_function(
    crud_getter: Callable[[AsyncSession, int], any], 
    not_found_exception: Callable[[int], HTTPException]
):
    async def get_by_id(
        entity_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.session_getter)
    ):
        entity = await crud_getter(session=session, entity_id=entity_id)
        if entity is not None:
            return entity
        raise not_found_exception(entity_id)
    return get_by_id


student_by_id = create_get_by_id_function(
    students_crud.get_student, 
    student_not_found
)

semester_by_id = create_get_by_id_function( 
    semesters_crud.get_semester, 
    semester_not_found
)

group_by_id = create_get_by_id_function(
    groups_crud.get_group, 
    group_not_found
)


teacher_by_id = create_get_by_id_function(
    teachers_crud.get_teacher,
    teacher_not_found
)


subject_by_id = create_get_by_id_function(
    subjects_crud.get_subject,
    subject_not_found
)


lesson_by_id = create_get_by_id_function(
    lessons_crud.get_lesson,
    lesson_not_found
)


daily_schedule_by_id = create_get_by_id_function(
    daily_schedules_crud.get_daily_schedule,
    daily_schedule_not_found
)


weekly_schedule_by_id = create_get_by_id_function(
    weekly_schedules_crud.get_weekly_schedule,
    weekly_schedule_not_found
)


grade_by_id = create_get_by_id_function(
    grades_crud.get_grade,
    grade_not_found
)