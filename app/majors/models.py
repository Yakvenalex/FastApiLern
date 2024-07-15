from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk, str_null_true


# создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int_pk]
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    # Определяем отношения: один факультет может иметь много студентов
    students: Mapped[list["Student"]] = relationship("Student", back_populates="major")
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)
