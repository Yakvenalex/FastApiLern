from pydantic import BaseModel, Field


class SMajorsAdd(BaseModel):
    major_name: str = Field(..., description="Название факультета")
    major_description: str = Field(None, description="Описание факультета")
    count_students: int = Field(0, description="Количество студентов")


class SMajorsUpdDesc(BaseModel):
    major_name: str = Field(..., description="Название факультета")
    major_description: str = Field(None, description="Новое описание факультета")