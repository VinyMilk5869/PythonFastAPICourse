from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return "Hello World!"


@app.get("/hello")
async def hello():
    return "Hello from FastAPI!"

@app.post("/name")
async def name(name: str):
    return {"name": name}