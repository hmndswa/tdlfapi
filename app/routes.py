from fastapi import APIRouter

api_router = APIRouter()

from app.user.router import router as user_router
from app.auth.router import router as auth_router
from app.todo.router import router as todo_router

api_router.include_router(user_router, prefix="/users", tags=["users"])
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
api_router.include_router(todo_router, prefix="/todo", tags=["todo"])
