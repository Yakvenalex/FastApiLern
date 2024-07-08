from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent, SUpdateFilter, SStudentUpdate, SDeleteFilter
from utils import json_to_dict_list, add_student, upd_student, dell_student

router = APIRouter(prefix='/students', tags=['Работа со студентами'])


@router.get("")
async def get_all_students(course: Optional[int] = None) -> List[SStudent]:
    if course:
        rez = await StudentDAO.find_all(course=course)
    else:
        rez = await StudentDAO.find_all()

    return rez


@router.get("/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> List[SStudent]:
    students = json_to_dict_list()
    filtered_students = []
    for student in students:
        if student["course"] == request_body.course:
            filtered_students.append(student)

    if request_body.major:
        filtered_students = [student for student in filtered_students if
                             student['major'].lower() == request_body.major.lower()]

    if request_body.enrollment_year:
        filtered_students = [student for student in filtered_students if
                             student['enrollment_year'] == request_body.enrollment_year]

    return filtered_students


@router.get("/{student_id}")
def get_student_from_id(student_id: int):
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student


@router.get("/student")
def get_student_from_param_id(student_id: int) -> SStudent:
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student


@router.post("/add_student")
def add_student_handler(student: SStudent):
    check = add_student(student.dict())
    if check:
        return {"message": "Студент успешно добавлен!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")


@router.put("/update_student")
def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
    check = upd_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Информация о студенте успешно обновлена!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")


@router.delete("/delete_student")
def delete_student_handler(filter_student: SDeleteFilter):
    check = dell_student(filter_student.key, filter_student.value)
    if check:
        return {"message": "Студент успешно удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")
