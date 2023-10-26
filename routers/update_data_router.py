from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_data import *

router = APIRouter()

@router.post('/load/100', response_class=PlainTextResponse)
async def receive_data_100(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "../data/100"
    return update_data(data_received, data_DIR)

@router.post('/load/200', response_class=PlainTextResponse)
async def receive_data_200(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "../data/200"
    return update_data(data_received, data_DIR)

@router.post('/load/300', response_class=PlainTextResponse)
async def receive_data_300(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "../data/300"
    return update_data(data_received, data_DIR)

@router.post('/load/400', response_class=PlainTextResponse)
async def receive_data_400(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "../data/400"
    return update_data(data_received, data_DIR)

@router.post('/load/500', response_class=PlainTextResponse)
async def receive_data_500(data_received: dict):
    # <CONTAINER DIR>
    data_DIR = "../data/500"
    return update_data(data_received, data_DIR)