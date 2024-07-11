from app.dao.base import BaseDAO
from app.majors.models import Major


class MajorsDAO(BaseDAO):
    model = Major