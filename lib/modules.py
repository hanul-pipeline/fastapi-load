import configparser
import mysql.connector
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, '../config/config.ini')
data_dir = os.path.join(current_dir, '../data')

# read config
def get_config(group, req_var):
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
def flatten_dict(dictionary, parent_key='', sep='_'):
    items = {}
    
    for k, v in dictionary.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v

    return items


# confirmed
def return_rows(items):
    item_list = []

    measurement = items["measurement"]
    rest = items
    del rest["measurement"]

    for index in measurement:
        item = {**rest, **index}
        item_list.append(item)

    return item_list


# parquet_dir = "1/100/22"
# hdfs_mkdir(parquet_dir)
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


# parquet_dir = "1/100/22"
# hdfs_mkdir(parquet_dir)
def hdfs_input(parquet_dir, hdfs_dir):
    import subprocess

    command = f"hdfs dfs -put {data_dir}/parquet/{parquet_dir}   /hanul/measurement/{hdfs_dir}"

    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout)
    print(stderr)

