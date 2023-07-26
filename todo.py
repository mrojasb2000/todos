"""Import dependencies"""
from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    """Add function"""
    todo_list.append(todo)
    return {"message": "Todo added seccessfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    """List function"""
    return {"todos": todo_list}
