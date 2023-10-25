from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_parquet import *

router = APIRouter()

@router.post('/parquet', response_class=PlainTextResponse)
async def remove_data(date: str, time: str):
    return update_parquet(date, time)