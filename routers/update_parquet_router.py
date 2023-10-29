from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_parquet import *


router = APIRouter()

# router: parquet to local
@router.post('/parquet/local/100', response_class=PlainTextResponse)
async def update_parquet_local_100(date: str, time: str):
    location_id = 7
    sensor_id = 100,
    table_name = 'matrix'
    return update_parquet_local(table_name, location_id, sensor_id, date, time)

@router.post('/parquet/local/200', response_class=PlainTextResponse)
async def update_parquet_local_200(date: str, time: str):
    location_id = 8
    sensor_id = 200
    table_name = 'matrix'
    return update_parquet_local(table_name, location_id, sensor_id, date, time)

@router.post('/parquet/local/300', response_class=PlainTextResponse)
async def update_parquet_local_300(date: str, time: str):
    location_id = 10
    sensor_id = 300
    table_name = 'single'
    return update_parquet_local(table_name, location_id, sensor_id, date, time)

@router.post('/parquet/local/400', response_class=PlainTextResponse)
async def update_parquet_local_400(date: str, time: str):
    location_id = 11
    sensor_id = 400
    table_name = 'single'
    return update_parquet_local(table_name, location_id, sensor_id, date, time)

@router.post('/parquet/local/500', response_class=PlainTextResponse)
async def update_parquet_local_500(date: str, time: str):
    location_id = 7
    sensor_id = 500
    table_name = 'single'
    return update_parquet_local(table_name, location_id, sensor_id, date, time)


# router: parquet to hdfs
@router.post('/parquet/hdfs/100', response_class=PlainTextResponse)
async def update_parquet_hdfs_100(date: str, time: str):
    location_id = 7
    sensor_id = 100
    return update_parquet_hdfs(location_id, sensor_id, date, time)

@router.post('/parquet/hdfs/200', response_class=PlainTextResponse)
async def update_parquet_hdfs_200(date: str, time: str):
    location_id = 8
    sensor_id = 200
    return update_parquet_hdfs(location_id, sensor_id, date, time)

@router.post('/parquet/hdfs/300', response_class=PlainTextResponse)
async def update_parquet_hdfs_300(date: str, time: str):
    location_id = 10
    sensor_id = 300
    return update_parquet_hdfs(location_id, sensor_id, date, time)

@router.post('/parquet/hdfs/400', response_class=PlainTextResponse)
async def update_parquet_hdfs_400(date: str, time: str):
    location_id = 11
    sensor_id = 400
    return update_parquet_hdfs(location_id, sensor_id, date, time)

@router.post('/parquet/hdfs/500', response_class=PlainTextResponse)
async def update_parquet_hdfs_100(date: str, time: str):
    location_id = 7
    sensor_id = 500
    return update_parquet_hdfs(location_id, sensor_id, date, time)