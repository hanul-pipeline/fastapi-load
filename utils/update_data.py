import csv
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
sys.path.append(lib_dir)

from modules import *


# MYSQL 업데이트
def update_mysql(data_received:dict):
    conn = db_conn()
    cursor = conn.cursor()
    
    query = "INSERT INTO measurement (`날짜`, `시간`, `위치ID`, `분류ID`, `센서ID`, `측정값`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (f"{data_received['날짜']}", f"{data_received['시간']}", f"{data_received['위치'][1]}", f"{data_received['분류'][1]}", f"{data_received['데이터']['센서'][1]}", f"{data_received['데이터']['측정값']}")
    
    cursor.execute(query,val)
    conn.commit()
    conn.close()


# CSV 업데이트
def update_csv(data_received:dict, data_DIR:str):
    flat_data = flatten_dict(data_received)
    
    with open(f'{data_DIR}/measurements.csv', mode='a', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
        if file.tell() == 0:
            header = list(flat_data.keys())
            writer.writerow(header)
            
        data_row = list(flat_data.values())
        writer.writerow(data_row)


# 업데이트 실행
def update_data(data_received:dict, data_DIR:str):
    update_mysql(data_received)
    update_csv(data_received, data_DIR)
