import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
sys.path.append(lib_dir)

from modules import *

# MYSQL 데이터 삭제
def remove_mysql(date:str):
    conn = db_conn()
    cursor = conn.cursor()
    
    query = "DELETE FROM measurements WHERE `날짜` = %s"
    val = (date,)
    
    cursor.execute(query,val)
    conn.commit()
    conn.close()

# date = '2023-10-21'

# remove_mysql(date)