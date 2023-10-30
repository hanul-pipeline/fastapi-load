# fastapi_load
<img width="1371" alt="faspapi-load" src="https://github.com/hanul-pipeline/fastapi-load/assets/130134750/d2d286b2-f146-4df1-8e00-f1e755aa29f4">
fastapi_load 레포지토리는 팀 '한울'에서 설계한 데이터 관리 파이프라인의 일부분입니다. 이 레포에서는 산업 현장에서 동시다발적으로 생성되는 센서 데이터들을 가공 및 적재하는 로직을 포함하고 있습니다. 가공 및 적재된 데이터들은 주기적으로 parquet 형태로 변환되어 hdfs 저장소로 이관됩니다.

# Usage
1. cURL 명령어로 전송되는 request 및 센서 데이터 수신
2. 수신한 센서 데이터의 1차 가공 및 적재: MySQL, csv
3. 적재된 MySQL 데이터의 2차 가공(parquet) 및 적재: hdfs

# Structure
### database: MySQL
<img width="1179" alt="database_mysql" src="https://github.com/hanul-pipeline/fastapi-load/assets/130134750/7b3636ad-3c99-442d-960f-991d21b412b2">
: MySQL에 적재된 데이터는 데이터 적재 디렉토리를 분류하는 과정에서 사용되며, 추후 내부 BI(superset)에서의 데이터 조회 및 경보 로직 구현에 사용됩니다.

### tree
```
.
├── README.md
├── config
│   └── config.ini
├── data
│   └── ...
├── lib
│   └── modules.py
├── main.py
├── routers
│   ├── remove_data_router.py
│   ├── update_data_router.py
│   └── update_parquet_router.py
└── utils
    ├── remove_data.py
    ├── update_data.py
    └── update_parquet.py
```

# Requirements
fastapi_load 레포지토리는 이하의 환경에서 운영되고 있습니다.
### OS
- ubuntu 20.04 LTS
### programs
- python: v3.7.16
- java: openjdk-8-jdk
- hadoop: v3.3.4
### modules
```
pip install -y fastapi "uvicorn[standard]" mysql-connector-python pandas pyarrow numpy
```

# Notification

