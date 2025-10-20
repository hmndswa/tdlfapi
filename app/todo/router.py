from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def todos():
    return {"message": "Todo Hello World"}