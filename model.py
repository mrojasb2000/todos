"""Pydantic dependencies"""
from pydantic import BaseModel


class Item(BaseModel):
    """Item pydantic model"""

    item: str
    status: str


class Todo(BaseModel):
    """Todo pydantic model"""

    id: int = None
    item: Item = None
