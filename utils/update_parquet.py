import sys, os
sys.path.append('/home/kjh/code/hanul/fastapi-load')
from lib.modules import *

# MYSQL 데이터 Parquet 변환 (Pandas)
def update_parquet(date:str, time:str):
    import pandas as pd
    
    conn = db_conn()
    
    query = """SELECT `날짜`, DATE_FORMAT(`시간`, %s) as `시`, DATE_FORMAT(`시간`, %s) as `시간`, `위치ID`, `분류ID`, `센서ID`, `측정값` 
                FROM measurements 
                WHERE `날짜` = %s AND `시간` BETWEEN SUBTIME(%s, '02:00:00') AND %s"""
    params = ('%H', '%H:%i:%s', date, time, time)
    
    df = pd.read_sql(query, conn, params=params)
    
    df.sort_values(['날짜', '시간', '센서ID'], inplace=True)
    
    print(df)
 
    DIR = '../data/parquet/'
    # DIR = '/home/kjh/code/hanul/fastapi-load/data/parquet/'
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    
    df.to_parquet(DIR, engine='pyarrow', index=False, partition_cols=['위치ID', '센서ID', '날짜', '시'])
    
    conn.close()
    


# date = '2023-10-26'
# time = '18:00:00'

# update_parquet(date, time)
