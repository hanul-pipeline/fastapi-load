import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, '../lib')
log_dir = os.path.join(current_dir, "../log")
sys.path.append(lib_dir)

from modules import *


# confirmed
def check_mysql(database:str, sensor_id:int, date:str):
    conn = db_conn()
    cursor = conn.cursor()

    QUERY = f"SELECT COUNT(*) from {database} "
    QUERY += "WHERE sensor_id = %s AND date = %s"
    VALUES = (sensor_id, date)

    cursor.execute(QUERY, VALUES)
    count = cursor.fetchall()[0][0]
    print(count)

    result = create_check_logs(date=date, 
                               sensor_id=sensor_id, 
                               count=count)

    conn.close()

    return(result)



# confirmed
def remove_mysql(database:str, sensor_id:int, date:str):

    try:
        conn = db_conn()
        cursor = conn.cursor()
        
        QUERY = f"DELETE FROM {database} "
        QUERY += "WHERE sensor_id = %s AND date = %s"
        VALUES = (sensor_id, date)
        
        cursor.execute(QUERY, VALUES)
        conn.commit()
        conn.close()
        
        status = "SUCCEED"
        add = "Clear"
    
    except Exception as e:
        status = "FAILED"
        add = f"Error Appeared: {e}"

    create_remove_logs(date=date, sensor_id=sensor_id, status=status, add=add)


# TEST
if __name__ == "__main__":
    database = "matrix"
    sensor_id = 100
    date = "2023-11-01"

    result = check_mysql(database=database, sensor_id=sensor_id, date=date)
    print(result)

    # remove_mysql(database=database, sensor_id=sensor_id, date=date)