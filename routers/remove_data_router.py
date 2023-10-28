from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.remove_data import *


router = APIRouter()

@router.post('/remove', response_class=PlainTextResponse)
async def remove_data(date: str):
    return remove_mysql(date)