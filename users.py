from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

users_list = [
    User(id=1, name="John Doe", email="asd@asd.com"),
    User(id=2, name="Jane Doe", email="asdasd@asd.com"),
    User(id=3, name="Jim Doe", email="asdasd@asd.com")
]

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = next((u for u in users_list if u.id == user_id), None)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
