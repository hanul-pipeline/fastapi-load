import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
data_dir = os.path.join(current_dir, '../data')
sys.path.append(lib_dir)

from modules import *


# confirmed
def update_parquet_local(table:str, location_id:int, sensor_id:int, date:str, time:int):
    import pandas as pd
    
    # open connector
    conn = db_conn()

    # read datas & create dataframe
    query = """SELECT date, DATE_FORMAT(time, %s) as hour, DATE_FORMAT(time, %s) as time, location_id, type_name, sensor_id, measurement 
                FROM %s
                WHERE date = %s 
                AND location_id = %s
                AND sensor_id = %s
                AND time BETWEEN %s AND %s"""
    params = ('%H', '%H:%i:%s', table, date, location_id, sensor_id, f"{time}:00:00", f"{time+1}:00:00")
    df = pd.read_sql(query, conn, params=params)

    # close connector
    conn.close()

    # create folder
    DIR = f'{data_dir}/parquet'
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    df.sort_values(['date', 'time', 'sensor_id'], inplace=True)
    df.to_parquet(DIR, engine='pyarrow', index=False, partition_cols=['location_id', 'sensor_id', 'date', 'hour'])


# confirmed
def update_parquet_hdfs(location_id, sensor_id, date, hour:int):
    parquet_dir = f"location_id={location_id}/sensor_id={sensor_id}/date={date}/hour={hour}"
    hdfs_dir = f"location_id={location_id}/sensor_id={sensor_id}/date={date}"
    hdfs_mkdir(parquet_dir)
    hdfs_input(parquet_dir, hdfs_dir)


# test
if __name__ == "__main__":
    update_parquet_local('matrix', 1, 100, '2023-10-26', 11)
    update_parquet_hdfs(1, 100, '2023-10-26', 11)