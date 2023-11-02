import configparser
import mysql.connector
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


# read config
def get_config(group, req_var):
    config_dir = os.path.join(current_dir, '../config/config.ini')

    config = configparser.ConfigParser()
    config.read(config_dir)
    result = config.get(group, req_var)
    
    return result


# db connection
def db_conn(charset=True):
    host = get_config('MySQL', 'host')
    user = get_config('MySQL', 'user')
    password = get_config('MySQL', 'passwd')
    database = get_config('MySQL', 'database')
    port = get_config('MySQL', 'port')
    
    if charset:
        conn = mysql.connector.connect(host=host,
                                       user=user,
                                       password=password,
                                       database=database,
                                       port=port)
    else:
        conn = mysql.connector.connect(host=host,
                                       user=user,
                                       password=password,
                                       database=database,
                                       port=port,
                                       charset='utf8mb4')
        
    return conn


# confirmed
def hdfs_mkdir(parquet_dir):
    from hdfs import InsecureClient

    hdfs_url = 'http://localhost:9870'
    user = 'hooniegit'
    hdfs_path = f'/hanul/measurement/{parquet_dir}'

    try:
        client = InsecureClient(hdfs_url, user=user)
        client.makedirs(hdfs_path)
        client.makedirs(hdfs_path)
        print(f"Created HDFS directory: {hdfs_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


# confirmed
def hdfs_input(parquet_dir, hdfs_dir):
    import subprocess

    data_dir = os.path.join(current_dir, '../data')

    command = f"hdfs dfs -put {data_dir}/parquet/{parquet_dir}   /hanul/measurement/{hdfs_dir}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout)
    print(stderr)


# confirmed
def create_check_logs(date, sensor_id, count):
    from datetime import datetime

    # define log dir
    log_dir = os.path.join(current_dir, '../log')

    # create params for check
    day = datetime.strptime(date, "%Y-%m-%d").weekday()
    limit = int((60*60*24)*0.98) if day != 2 else int((60*60*22)*0.98)

    # create params
    if count >= limit:
        result = "PASS"
        status = "CLEAR"
    else:
        result = "FAIL"
        status = f"{limit - count} datas are missing."

    # log messages
    message = f"""
    LOG: CHECK MYSQL
    ====================
    date: {date}
    result: {result}
    total count: {count}
    status: {status}
    """

    # create log
    logname = f"{log_dir}/check/{date}_{sensor_id}_{result}.log"
    with open(logname, "w") as file:
        file.write(message)

    return result


# confirmed
def create_remove_logs(date, sensor_id, status, add):
    # define log_dir
    log_dir = os.path.join(current_dir, '../log')

    # log messages
    message = f"""
    LOG: REMOVE MYSQL
    ====================
    date: {date}
    status: {status}
    add: {add}
    """

    # create log
    logname = f"{log_dir}/remove/{date}_{sensor_id}_{status}.log"
    with open(logname, "w") as file:
        file.write(message)


# TEST
if __name__ == "__main__":
    date = "2023-11-02"
    sensor_id = 100
    count = int(3600*24*0.99)

    # result = create_check_logs(date, sensor_id, count)
    # print(result)

    status = "SUCCEED"
    add = "Clear"

    create_remove_logs(date=date, sensor_id=sensor_id, status=status, add=add)