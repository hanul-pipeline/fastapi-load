import sys, csv
sys.path.append('/home/kjh/code/hanul/fastapi-load')
from lib.modules import *


# MYSQL 업데이트
def update_mysql(data_received:dict):
    conn = db_conn()
    cursor = conn.cursor()
    
    query = "INSERT INTO measurements (`날짜`, `시간`, `위치ID`, `분류ID`, `센서ID`, `측정값`) VALUES (%s, %s, %s, %s, %s, %s)"
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
    


# sensor_dict = {
#     "날짜": "2023-10-26",
#     "시간": "17:34:56",
#     "위치": ("서울", "001"),
#     "분류": ("온도", "01"),
#     "데이터": {
#         "센서": ("DS18B20", "01"),
#         "측정값": 25.3,
#         "단위": "°C",
#         "경과시간(sec)": 60
#     },
#     "연결": {
#         "네트워크명": "MyNetwork",
#         "신호강도(dB)": -70
#     }
# }

# dir = "../data"

# update_data(sensor_dict, dir)