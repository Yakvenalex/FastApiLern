from sqlalchemy import update, delete, event
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.majors.models import Major
from app.students.models import Student
from app.database import async_session_maker


@event.listens_for(Student, 'after_insert')
def receive_after_insert(mapper, connection, target):
    major_id = target.major_id
    connection.execute(
        update(Major)
        .where(Major.id == major_id)
        .values(count_students=Major.count_students + 1)
    )


@event.listens_for(Student, 'after_delete')
def receive_after_delete(mapper, connection, target):
    major_id = target.major_id
    connection.execute(
        update(Major)
        .where(Major.id == major_id)
        .values(count_students=Major.count_students - 1)
    )


class StudentDAO(BaseDAO):
    model = Student

    @classmethod
    async def find_full_data(cls, student_id: int):
        async with async_session_maker() as session:
            # Query to get student info along with major info
            query = select(cls.model).options(joinedload(cls.model.major)).filter_by(id=student_id)
            result = await session.execute(query)
            student_info = result.scalar_one_or_none()

            # If student is not found, return None
            if not student_info:
                return None

            student_data = student_info.to_dict()
            student_data['major'] = student_info.major.major_name
            return student_data

    @classmethod
    async def add_student(cls, **student_data: dict):
        async with async_session_maker() as session:
            async with session.begin():
                new_student = cls.model(**student_data)
                session.add(new_student)
                await session.flush()
                new_student_id = new_student.id
                await session.commit()
                return new_student_id

    @classmethod
    async def delete_student(cls, student_id: int):
        async with async_session_maker() as session:
            async with session.begin():
                # Query to find the student by ID
                query = select(cls.model).filter_by(id=student_id)
                result = await session.execute(query)
                student_info = result.scalar_one_or_none()

                # If student is found, delete the student
                if student_info:
                    # await session.delete(student_info)
                    await session.commit()
                    return True
                else:
                    return False
