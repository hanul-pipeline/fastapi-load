import configparser, mysql.connector

# config 값 불러오기
def get_config(group, req_var):
    config = configparser.ConfigParser()
    config.read('../config/config.ini')
    result = config.get(group, req_var)
    
    return result

# db 연결하기
def db_conn(charset=True):
    host = get_config('MYSQL', 'MYSQL_HOST')
    user = get_config('MYSQL', 'MYSQL_USER')
    password = get_config('MYSQL', 'MYSQL_PWD')
    database = get_config('MYSQL', 'MYSQL_DB')
    port = get_config('MYSQL', 'MYSQL_PORT')
    
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
