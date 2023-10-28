import csv
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
data_dir = os.path.join(current_dir, '../data')
sys.path.append(lib_dir)

from modules import *


# 
def update_mysql(data_received:dict):

    # open connector
    conn = db_conn()
    cursor = conn.cursor()
    
    # {'date': '2023-10-28', 'time': '16:15:44', 'location': {'id': 10, 'name': '제1 연구실'}, 
    # 'sensor': {'id': 300, 'name': 'MQ-4', 'type': '가연성 가스 센서'}, 
    # 'measurement': [{'value_type': 'CH4', 'value': 0.2, 'unit': 'ppm', 'cnt': 1, 'percentage': 0}], 'network': {'name': "can't find", 'dB': 0}}

    # get datas
    date = data_received["date"]
    time = data_received["time"]
    location_id = data_received["location"]["id"]
    sensor_id = data_received["sensor"]["id"]

    for index in data_received["measurement"]:
        # get datas
        value_type = index["value_type"]
        value = index["value"]
        unit = index["unit"]

        # update table
        QUERY = f"""
            INSERT INTO measurement (date, time, location_id, sensor_id, value_type, value, unit)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s)
        """
        VALUES = (date, time, location_id, sensor_id, value_type, value, unit)
        cursor.execute(QUERY, VALUES)
        conn.commit()

    # close connector
    conn.close()


# 
def update_csv(data_received:dict, data_DIR:str):
    flat_data = flatten_dict(data_received)
    
    with open(f'{data_dir}/{data_DIR}/measurements.csv', mode='a', newline='', encoding='utf-8-sig') as file:
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
