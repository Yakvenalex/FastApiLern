from fastapi import APIRouter, Request, Depends, UploadFile
from fastapi.templating import Jinja2Templates
import shutil

from app.students.router import get_all_students

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/students')
async def get_students_html(request: Request, student=Depends(get_all_students)):
    return templates.TemplateResponse(name='students.html',
                                      context={'request': request, 'students': student})


@router.post('/add_photo')
async def add_student_photo(file: UploadFile, image_name: int):
    with open(f"app/static/images/{image_name}.webp", "wb+") as photo_obj:
        shutil.copyfileobj(file.file, photo_obj)
