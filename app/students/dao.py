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
    x = [
        {
            "student_id": 1,
            "first_name": "\u0418\u0432\u0430\u043d",
            "last_name": "\u0418\u0432\u0430\u043d\u043e\u0432",
            "date_of_birth": "1998-05-15",
            "email": "ivan.ivanov@example.com",
            "phone_number": "+71234567890",
            "address": "\u0433. \u041c\u043e\u0441\u043a\u0432\u0430, \u0443\u043b. \u041f\u0443\u0448\u043a\u0438\u043d\u0430, \u0434. 10, \u043a\u0432. 5",
            "enrollment_year": 2040,
            "major_id": 1,
            "course": 6,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 2,
            "first_name": "\u0415\u043b\u0435\u043d\u0430",
            "last_name": "\u041f\u0435\u0442\u0440\u043e\u0432\u0430",
            "date_of_birth": "1999-08-20",
            "email": "elena.petrova@example.com",
            "phone_number": "+72345678901",
            "address": "\u0433. \u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433, \u0443\u043b. \u041b\u0435\u043d\u0438\u043d\u0430, \u0434. 5, \u043a\u0432. 8",
            "enrollment_year": 2018,
            "major_id": 1,
            "course": 2,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 3,
            "first_name": "\u0410\u043b\u0435\u043a\u0441\u0435\u0439",
            "last_name": "\u0421\u043c\u0438\u0440\u043d\u043e\u0432",
            "date_of_birth": "2000-03-10",
            "email": "alexey.smirnov@example.com",
            "phone_number": "+73456789012",
            "address": "\u0433. \u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a, \u0443\u043b. \u0413\u0430\u0433\u0430\u0440\u0438\u043d\u0430, \u0434. 15, \u043a\u0432. 12",
            "enrollment_year": 2019,
            "major_id": 2,
            "course": 1,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 4,
            "first_name": "\u041c\u0430\u0440\u0438\u044f",
            "last_name": "\u041a\u043e\u0437\u043b\u043e\u0432\u0430",
            "date_of_birth": "1997-11-25",
            "email": "maria.kozlova@example.com",
            "phone_number": "+74567890123",
            "address": 2,
            "enrollment_year": 2016,
            "major_id": "\u0418\u0441\u0442\u043e\u0440\u0438\u044f",
            "course": 4,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 5,
            "first_name": "\u0414\u043c\u0438\u0442\u0440\u0438\u0439",
            "last_name": "\u0421\u043e\u043a\u043e\u043b\u043e\u0432",
            "date_of_birth": "1999-04-03",
            "email": "dmitry.sokolov@example.com",
            "phone_number": "+75678901234",
            "address": "\u0433. \u041a\u0430\u0437\u0430\u043d\u044c, \u0443\u043b. \u041c\u0430\u044f\u043a\u043e\u0432\u0441\u043a\u043e\u0433\u043e, \u0434. 25, \u043a\u0432. 7",
            "enrollment_year": 2018,
            "major_id": 3,
            "course": 3,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 6,
            "first_name": "\u0410\u043d\u043d\u0430",
            "last_name": "\u0418\u0433\u043d\u0430\u0442\u044c\u0435\u0432\u0430",
            "date_of_birth": "2001-07-18",
            "email": "anna.ignatyeva@example.com",
            "phone_number": "+76789012345",
            "address": 3 ,
            "enrollment_year": 2020,
            "major_id": "\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f",
            "course": 2,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 7,
            "first_name": "\u041f\u0430\u0432\u0435\u043b",
            "last_name": "\u041a\u0443\u0437\u043d\u0435\u0446\u043e\u0432",
            "date_of_birth": "1998-09-12",
            "email": "pavel.kuznetsov@example.com",
            "phone_number": "+77890123456",
            "address": "\u0433. \u0420\u043e\u0441\u0442\u043e\u0432-\u043d\u0430-\u0414\u043e\u043d\u0443, \u0443\u043b. \u0413\u0430\u0433\u0430\u0440\u0438\u043d\u0430, \u0434. 40, \u043a\u0432. 22",
            "enrollment_year": 2017,
            "major_id": "\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f",
            "course": 4,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 8,
            "first_name": "\u0421\u0432\u0435\u0442\u043b\u0430\u043d\u0430",
            "last_name": "\u041c\u043e\u0440\u043e\u0437\u043e\u0432\u0430",
            "date_of_birth": "2000-01-30",
            "email": "svetlana.morozova@example.com",
            "phone_number": "+78901234567",
            "address": "\u0433. \u0427\u0435\u043b\u044f\u0431\u0438\u043d\u0441\u043a, \u0443\u043b. \u041a\u0438\u0440\u043e\u0432\u0430, \u0434. 35, \u043a\u0432. 2",
            "enrollment_year": 2019,
            "major_id": "\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0438\u044f",
            "course": 1,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 9,
            "first_name": "\u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0438\u043d",
            "last_name": "\u0424\u0435\u0434\u043e\u0440\u043e\u0432",
            "date_of_birth": "1997-12-05",
            "email": "konstantin.fedorov@example.com",
            "phone_number": "+79012345678",
            "address": "\u0433. \u0423\u0444\u0430, \u0443\u043b. \u0421\u043e\u0432\u0435\u0442\u0441\u043a\u0430\u044f, \u0434. 50, \u043a\u0432. 10",
            "enrollment_year": 2016,
            "major_id": "\u0411\u0438\u043e\u043b\u043e\u0433\u0438\u044f",
            "course": 4,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 10,
            "first_name": "\u041e\u043b\u044c\u0433\u0430",
            "last_name": "\u041d\u0438\u043a\u0438\u0442\u0438\u043d\u0430",
            "date_of_birth": "1999-06-20",
            "email": "olga.nikitina@example.com",
            "phone_number": "+70123456789",
            "address": "\u0433. \u0422\u043e\u043c\u0441\u043a, \u0443\u043b. \u041b\u0435\u043d\u0438\u043d\u0430, \u0434. 60, \u043a\u0432. 18",
            "enrollment_year": 2018,
            "major_id": "\u042d\u043a\u043e\u043d\u043e\u043c\u0438\u043a\u0430",
            "course": 5,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 11,
            "first_name": "\u041e\u043b\u044c\u0433\u0430",
            "last_name": "\u041d\u0438\u043a\u0438\u0442\u0438\u043d\u0430",
            "date_of_birth": "1999-06-20",
            "email": "olga.nikitina@example.com",
            "phone_number": "+70123456789",
            "address": "\u0433. \u0422\u043e\u043c\u0441\u043a, \u0443\u043b. \u041b\u0435\u043d\u0438\u043d\u0430, \u0434. 60, \u043a\u0432. 18",
            "enrollment_year": 2018,
            "major_id": "\u042d\u043a\u043e\u043b\u043e\u0433\u0438\u044f",
            "course": 3,
            "special_notes": "\u0411\u0435\u0437 \u043e\u0441\u043e\u0431\u044b\u0445 \u043f\u0440\u0438\u043c\u0435\u0442"
        },
        {
            "student_id": 20,
            "phone_number": "+8888888",
            "first_name": "\u0410\u043b\u0435\u043a\u0441\u0435\u0439",
            "last_name": "\u042f\u043a\u043e\u0432\u0435\u043d\u043a\u043e",
            "date_of_birth": "2000-07-07",
            "email": "user@example.com",
            "address": "stringstri",
            "enrollment_year": 2020,
            "major_id": "\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430",
            "course": 2,
            "special_notes": "string"
        }
    ]
    await StudentDAO.add_many(x)


asyncio.run(add_data())
