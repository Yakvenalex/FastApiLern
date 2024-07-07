import httpx


def get_all_students():
    url = "http://127.0.0.1:8000/students"
    response = httpx.get(url)
    return response.json()


def get_students_with_param_requests(course: int):
    url = "http://127.0.0.1:8000/students"
    response = httpx.get(url, params={"course": course})
    return response.json()


def get_students_with_param_path(course: int):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = httpx.get(url)
    return response.json()


def get_students_with_param_mix(course: int, major: str, enrollment_year: int):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = httpx.get(url, params={"major": major, "enrollment_year": enrollment_year})
    return response.json()