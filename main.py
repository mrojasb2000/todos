"""Import dependencies"""
import uvicorn
from fastapi import FastAPI
from todo import todo_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    """welcome function"""
    return {"message": "Hello World"}


app.include_router(todo_router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
