from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, str_uniq, int_pk


class User(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str_uniq]
    password: Mapped[str]

    is_user: Mapped[bool] = mapped_column(default=True, server_default=text('true'), nullable=False)
    is_student: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_teacher: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)
    is_super_admin: Mapped[bool] = mapped_column(default=False, server_default=text('false'), nullable=False)

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
