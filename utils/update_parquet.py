import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
data_dir = os.path.join(current_dir, '../data')
sys.path.append(lib_dir)

from modules import *


# confirmed: divided
def update_parquet_local(table_name:str, location_id:int, sensor_id:int, date:str, time:int):
    import pandas as pd
    
    # open connector
    conn = db_conn()

    # read datas & create dataframe
    query = "SELECT date, DATE_FORMAT(time, %s) as hour, DATE_FORMAT(time, %s) as time, location_id, sensor_id, value_type, value, unit "
    query += f"FROM {table_name} "
    query += """
                WHERE date = %s 
                AND location_id = %s
                AND sensor_id = %s
                AND time BETWEEN %s AND %s"""
    params = ('%H', '%H:%i:%s', date, location_id, sensor_id, f"{time}:00:00", f"{time+1}:00:00")
    df = pd.read_sql(query, conn, params=params)
    print(df)

    # close connector
    conn.close()

    # create folder
    DIR = f'{data_dir}/parquet/{table_name}'
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    df.sort_values(['date', 'time', 'sensor_id'], inplace=True)
    df.to_parquet(DIR, engine='pyarrow', index=False, partition_cols=['location_id', 'sensor_id', 'date', 'hour'])


# confirmed: divided
def update_parquet_hdfs(table_name, location_id, sensor_id, date, hour:int):
    parquet_dir = f"{data_dir}/parquet/{table_name}/location_id={location_id}/sensor_id={sensor_id}/date={date}/hour={hour}"
    hdfs_dir = f"{table_name}/location_id={location_id}/sensor_id={sensor_id}/date={date}"
    
    hdfs_mkdir(parquet_dir)
    hdfs_input(parquet_dir, hdfs_dir)


# test
if __name__ == "__main__":
    update_parquet_local('matrix', 8, 200, '2023-10-29', 21)
    update_parquet_hdfs (8, 200, '2023-10-29', 21)