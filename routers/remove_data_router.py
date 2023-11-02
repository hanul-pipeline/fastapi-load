from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.remove_data import *


router = APIRouter()

# curl 'http://{host}:{port}/check/100?date=2023-11-01'
@router.get('/check/100', response_class=PlainTextResponse)
async def check_data_100(date: str):
    database = "matrix"
    sensor_id = 100
    return check_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/check/200', response_class=PlainTextResponse)
async def check_data_200(date: str):
    database = "matrix"
    sensor_id = 200
    return check_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/check/300', response_class=PlainTextResponse)
async def check_data_300(date: str):
    database = "single"
    sensor_id = 300
    return check_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/check/400', response_class=PlainTextResponse)
async def check_data_400(date: str):
    database = "single"
    sensor_id = 400
    return check_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/check/500', response_class=PlainTextResponse)
async def check_data_500(date: str):
    database = "single"
    sensor_id = 500
    return check_mysql(database=database, sensor_id=sensor_id, date=date)


# curl 'http://{host}:{port}/remove/100?date=2023-11-01'
@router.get('/remove/100', response_class=PlainTextResponse)
async def remove_data_100(date: str):
    database = "matrix"
    sensor_id = 100
    return remove_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/remove/200', response_class=PlainTextResponse)
async def remove_data_200(date: str):
    database = "matrix"
    sensor_id = 200
    return remove_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/remove/300', response_class=PlainTextResponse)
async def remove_data_300(date: str):
    database = "single"
    sensor_id = 300
    return remove_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/remove/400', response_class=PlainTextResponse)
async def remove_data_400(date: str):
    database = "single"
    sensor_id = 400
    return remove_mysql(database=database, sensor_id=sensor_id, date=date)

@router.get('/remove/500', response_class=PlainTextResponse)
async def remove_data_500(date: str):
    database = "single"
    sensor_id = 500
    return remove_mysql(database=database, sensor_id=sensor_id, date=date)
