import sys
sys.path.append('/home/kjh/code/hanul/fastapi-load')
from lib.modules import *

# MYSQL 데이터 삭제
def remove_mysql(date:str):
    conn = db_conn()
    cursor = conn.cursor()
    
    query = "DELETE FROM measurements WHERE `날짜` = %s"
    val = (date,)
    
    cursor.execute(query,val)
    conn.commit()
    conn.close()

