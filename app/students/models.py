<<<<<<< HEAD
from sqlalchemy import ForeignKey, Text, event
from sqlalchemy.orm import Mapped, mapped_column, relationship
=======
from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import Mapped, mapped_column
>>>>>>> 636186fdd21748303fc4b2e7cf90c39fa906fba0
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date


# создаем модель таблицы студентов
class Student(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    date_of_birth: Mapped[date]
    email: Mapped[str_uniq]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]
    course: Mapped[int]
    special_notes: Mapped[str_null_true]
    major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)
<<<<<<< HEAD

    # Определяем отношения: один студент имеет один факультет
    major: Mapped["Major"] = relationship("Major", back_populates="students")
=======
>>>>>>> 636186fdd21748303fc4b2e7cf90c39fa906fba0

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)

<<<<<<< HEAD
    def to_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "email": self.email,
            "address": self.address,
            "enrollment_year": self.enrollment_year,
            "course": self.course,
            "special_notes": self.special_notes,
            "major_id": self.major_id
        }
=======

# создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int_pk]
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)
>>>>>>> 636186fdd21748303fc4b2e7cf90c39fa906fba0
