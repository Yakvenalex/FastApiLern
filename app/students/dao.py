import asyncio
import datetime
from app.dao.base import BaseDAO
from app.students.models import Student


class StudentDAO(BaseDAO):
    model = Student


async def get_data():
    rez = await StudentDAO.find_all()
    for i in rez:
        print(i.__dict__)


async def add_data():
    await StudentDAO.delete()


asyncio.run(add_data())
