from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_data import *

router = APIRouter()
@router.post('/sensors', response_class=PlainTextResponse)
async def receive_data(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "../data/"
    return update_data(data_received, data_DIR)