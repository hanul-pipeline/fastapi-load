import csv
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
data_dir = os.path.join(current_dir, '../data')
sys.path.append(lib_dir)

from modules import *


# confirmed
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


# confirmed
def update_csv(data_received:dict, date, location_id):
    folder_dir = f"{data_dir}/csv/location_id={location_id}/date={date}"
    try:
        os.makedirs(folder_dir)
    except FileExistsError:
        print("Folder Exists")

    # def file dir
    file_dir = f"{folder_dir}/measurements.csv"

    # return dict to rows
    flat_data = flatten_dict(data_received)
    returned_rows = return_rows(flat_data)
    
    print(returned_rows)

    # update csv
    with open(file_dir, mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        
        for row in returned_rows:
            if file.tell() == 0:
                header = list(row.keys())
                writer.writerow(header)
                
            data_row = list(row.values())
            writer.writerow(data_row)


# confirmeds
def update_data(data_received:dict, date:str, location_id:int):
    update_mysql(data_received)
    update_csv(data_received, date, location_id)


# TEST
if __name__ == "__main__":

    data_received = {
        "date": "2023-10-28", 
        "time": "16:15:31", 
        "location": {"id": 7, "name": "도장공정"}, 
        "sensor": {"id": 500, "name": "DHT-21", "type": "온습도 센서"}, 
        "measurement": [{"value_type": "temperature", "value": 32, "unit": "°C", "cnt": 1, "percentage": 0}, {"value_type": "moisture", "value": 52, "unit": "%", "cnt": 1, "percentage": 0}], 
        "network": {"name": "can't find", "dB": 0}}

    update_data(data_received, "2023-10-28", 7)