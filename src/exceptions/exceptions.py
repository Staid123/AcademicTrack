from fastapi import HTTPException, status

def create_not_found_exception(entity: str):
    def not_found(entity_id: int):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{entity} {entity_id} not found!",
        )
    return not_found


student_not_found = create_not_found_exception("Student")
semester_not_found = create_not_found_exception("Semester")
group_not_found = create_not_found_exception("Group")
teacher_not_found = create_not_found_exception("Teacher")
subject_not_found = create_not_found_exception("Subject")
lesson_not_found = create_not_found_exception("Lesson")