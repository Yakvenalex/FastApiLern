from fastapi import APIRouter, Depends
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent

router = APIRouter(prefix='/students', tags=['Работа со студентами'])


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.find_all(**request_body.to_dict())


@router.get("/{id}", summary="Получить одного студента по id")
async def get_all_students(student_id: int) -> SStudent | dict:
    rez = await StudentDAO.find_one_or_none_by_id(student_id)
    if rez is None:
        return {'message': f'Студент с ID {student_id} не найден!'}
    return rez


@router.get("/by_filter", summary="Получить одного студента по фильтру")
async def get_all_students(request_body: RBStudent = Depends()) -> SStudent | dict:
    rez = await StudentDAO.find_one_or_none(**request_body.to_dict())
    if rez is None:
        return {'message': f'Студент с указанными вами параметрами не найден!'}
    return rez
