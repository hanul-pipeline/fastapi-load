from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_data import *
from datetime import datetime


nowdate = datetime.now().strftime("%Y-%m-%d")

router = APIRouter()

@router.post('/update/100', response_class=PlainTextResponse)
async def receive_data_100(data_received: dict):
    location_id = 7
    return update_data(data_received, nowdate, location_id)

@router.post('/update/200', response_class=PlainTextResponse)
async def receive_data_200(data_received: dict):
    location_id = 8
    return update_data(data_received, nowdate, location_id)

@router.post('/update/300', response_class=PlainTextResponse)
async def receive_data_300(data_received: dict):
    location_id = 10
    return update_data(data_received, nowdate, location_id)

@router.post('/update/400', response_class=PlainTextResponse)
async def receive_data_400(data_received: dict):
    location_id = 11
    return update_data(data_received, nowdate, location_id)

@router.post('/update/500', response_class=PlainTextResponse)
async def receive_data_500(data_received: dict):
    location_id = 7
    return update_data(data_received, nowdate, location_id)