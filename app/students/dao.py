from sqlalchemy import insert, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.majors.models import Major
from app.students.models import Student
from app.database import async_session_maker


class StudentDAO(BaseDAO):
    model = Student

    @classmethod
    async def find_full_data(cls, student_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о студенте вместе с информацией о факультете
            query = select(cls.model).options(joinedload(cls.model.major)).filter_by(id=student_id)
            result = await session.execute(query)
            student_info = result.scalar_one_or_none()

            # Если студент не найден, возвращаем None
            if not student_info:
                return None

            student_data = student_info.to_dict()
            student_data['major'] = student_info.major.major_name
            return student_data

    @classmethod
    async def add_student(cls, student_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                # Вставка нового студента
                stmt = insert(cls.model).values(**student_data).returning(cls.model.id, cls.model.major_id)
                result = await session.execute(stmt)
                new_student_id, major_id = result.fetchone()

                # Увеличение счетчика студентов в таблице major
                update_major = update(Major).where(Major.id == major_id).values(student_count=Major.count_students + 1)
                await session.execute(update_major)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e

                return new_student_id