import configparser
import mysql.connector
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, '../config/config.ini')


# config 값 불러오기
def get_config(group, req_var):
    config = configparser.ConfigParser()
    config.read(config_dir)
    result = config.get(group, req_var)
    
    return result


# db 연결하기
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


# 딕셔너리 펼치기
def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        if k in ['데이터', '연결']:  # 이러한 키를 무시하고 그 아래의 항목만 처리
            items.update(flatten_dict(v, parent_key, sep=sep))
        else:
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, dict):
                items.update(flatten_dict(v, new_key, sep=sep))
            elif isinstance(v, tuple) and len(v) == 2:
                items[new_key + '명'] = v[0]
                items[new_key + 'ID'] = v[1]
            else:
                items[new_key] = v
    return items


# parquet_dir = "1/100/22"
# hdfs_mkdir(parquet_dir)
def hdfs_mkdir(parquet_dir):
    from hdfs import InsecureClient

    hdfs_url = 'http://localhost:9870'
    user = 'hadoop'
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
def hdfs_input(parquet_dir):
    import subprocess

    passwd = get_config("localhost", "passwd")
    command = f"hdfs dfs -put /opt/data/parquet/{parquet_dir}   /hanul/measurement/"
    cmd = f'echo {passwd} | sudo -S docker exec fastapi-load-namenode-1 {command}'

    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    print(stdout)
    print(stderr)