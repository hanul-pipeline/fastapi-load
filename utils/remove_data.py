import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
sys.path.append(lib_dir)

from modules import *


# confirmed
def remove_mysql(date:str):
    conn = db_conn()
    cursor = conn.cursor()
    
    query = "DELETE FROM measurement WHERE date = %s"
    val = (date,)
    
    cursor.execute(query,val)
    conn.commit()
    conn.close()


# TEST
if __name__ == "__main__":
    date = '2023-10-28'
    remove_mysql(date)