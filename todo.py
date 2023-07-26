"""Import dependencies"""
from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo", tags=["Todos"])
async def add_todo(todo: Todo) -> dict:
    """Add todo to data bases"""
    todo_list.append(todo)
    return {"message": "Todo added seccessfully"}


@todo_router.get("/todo", tags=["Todos"])
async def retrieve_todos() -> dict:
    """List todos from data bases"""
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}", tags=["Todos"])
async def filter_by_id(todo_id: int = Path(ge=0, le=100)) -> dict:
    """Get todo by id"""
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo with supplied ID doesn't exist."}
