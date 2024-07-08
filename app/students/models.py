from sqlalchemy import Integer, String, Date, ForeignKey, Column
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base
from datetime import date


# создаем модель таблицы студентов
class Student(Base):
    student_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    phone_number: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    enrollment_year: Mapped[int] = mapped_column(Integer, nullable=False)
    course: Mapped[int] = mapped_column(Integer, nullable=False)
    special_notes: Mapped[str] = mapped_column(String, nullable=True)
    major_id: Mapped[int] = mapped_column(Integer, ForeignKey("majors.major_id"), nullable=False)

    major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(student_id={self.student_id}, "
                f"first_name={self.first_name!r}, "
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)


# создаем модель таблицы факультетов (majors)
class Major(Base):
    major_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    major_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    major_description: Mapped[str] = mapped_column(String, nullable=True)

    students: Mapped[list["Student"]] = relationship("Student", back_populates="major")

    def __str__(self):
        return f"{self.__class__.__name__}(major_id={self.major_id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)
