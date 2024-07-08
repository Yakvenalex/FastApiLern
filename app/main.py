from fastapi import FastAPI, Depends, HTTPException
from utils import json_to_dict_list, add_student, upd_student, dell_student
from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime
from typing import Optional, List, Any
import re


class Major(str, Enum):
    informatics = "Информатика"
    economics = "Экономика"
    law = "Право"
    medicine = "Медицина"
    engineering = "Инженерия"
    languages = "Языки"


class SStudent(BaseModel):
    student_id: int
    phone_number: str = Field(..., description="Номер телефона в международном формате, начинающийся с '+'")
    first_name: str = Field(..., min_length=1, max_length=50, description="Имя студента, от 1 до 50 символов")
    last_name: str = Field(..., min_length=1, max_length=50,
                           description="Фамилия студента, от 1 до 50 символов")
    date_of_birth: date = Field(..., description="Дата рождения студента в формате ГГГГ-ММ-ДД")
    email: EmailStr = Field(..., description="Электронная почта студента")
    address: str = Field(..., min_length=10, max_length=200,
                         description="Адрес студента, не более 200 символов")
    enrollment_year: int = Field(..., ge=2002, description="Год поступления должен быть не меньше 2002")
    major: Major = Field(..., description="Специальность студента")
    course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(None, max_length=500,
                                         description="Дополнительные заметки, не более 500 символов")

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
        return values

    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


@app.get("/students")
def get_all_students(course: Optional[int] = None):
    students = json_to_dict_list()
    if course is None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list


class RBStudent:
    def __init__(self, course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
        self.course: int = course
        self.major: Optional[str] = major
        self.enrollment_year: Optional[int] = enrollment_year


@app.get("/students/{course}")
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


@app.get("/student/{student_id}")
def get_student_from_id(student_id: int):
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.get("/student")
def get_student_from_param_id(student_id: int) -> SStudent:
    students = json_to_dict_list()
    for student in students:
        if student["student_id"] == student_id:
            return student


@app.post("/add_student")
def add_student_handler(student: SStudent):
    check = add_student(student.dict())
    if check:
        return {"message": "Студент успешно добавлен!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")


# Определение модели для фильтра обновления
class SUpdateFilter(BaseModel):
    student_id: int


# Определение модели для новых данных студента
class SStudentUpdate(BaseModel):
    course: int = Field(..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    major: Optional[Major] = Field(..., description="Специальность студента")


@app.put("/update_student")
def update_student_handler(filter_student: SUpdateFilter, new_data: SStudentUpdate):
    check = upd_student(filter_student.dict(), new_data.dict())
    if check:
        return {"message": "Информация о студенте успешно обновлена!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при обновлении информации о студенте")


class SDeleteFilter(BaseModel):
    key: str
    value: Any


@app.delete("/delete_student")
def delete_student_handler(filter_student: SDeleteFilter):
    check = dell_student(filter_student.key, filter_student.value)
    if check:
        return {"message": "Студент успешно удален!"}
    else:
        raise HTTPException(status_code=400, detail="Ошибка при удалении студента")
