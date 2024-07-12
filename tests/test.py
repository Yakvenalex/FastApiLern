import asyncio
import httpx


async def add_major(major_name: str, major_description: str):
    url = 'http://127.0.0.1:8000/majors/add/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "major_name": major_name,
        "major_description": major_description,
        "count_students": 0
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        return response.json()
