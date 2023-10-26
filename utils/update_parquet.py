import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
data_dir = os.path.join(current_dir, '../data')
sys.path.append(lib_dir)

from modules import *


# 
# MYSQL 데이터 Parquet 변환 (Pandas)
def update_parquet_local(location_id:int, sensor_id:int, date:str, time:int):
    import pandas as pd
    
    # open connector
    conn = db_conn()

    # read datas & create dataframe
    query = """SELECT `날짜`, DATE_FORMAT(`시간`, %s) as `시`, DATE_FORMAT(`시간`, %s) as `시간`, `위치ID`, `분류`, `센서ID`, `측정값` 
                FROM measurement 
                WHERE `날짜` = %s 
                AND `위치ID` = %s
                AND `센서ID` = %s
                AND `시간` BETWEEN %s AND %s"""
    params = ('%H', '%H:%i:%s', date, location_id, sensor_id, f"{time-1}:00:00", f"{time}:00:00")
    df = pd.read_sql(query, conn, params=params)

    # close connector
    conn.close()

    # create folder
    DIR = f'{data_dir}/parquet'
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    df.sort_values(['날짜', '시간', '센서ID'], inplace=True)
    df.to_parquet(DIR, engine='pyarrow', index=False, partition_cols=['위치ID', '센서ID', '날짜', '시'])
    print("job is done")



def update_parquet_hdfs(location_id, sensor_id, date, hour:int):
    parquet_dir = f"위치ID={location_id}/센서ID={sensor_id}/날짜={date}/시={hour}"
    hdfs_mkdir(parquet_dir)
    hdfs_input(parquet_dir)


# 테스트
if __name__ == "__main__":
    # update_parquet_local(1, 100, '2023-10-26', 12)
    update_parquet_hdfs(1, 100, '2023-10-26', 11)