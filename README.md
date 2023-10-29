# fastapi_load
image
fastapi_load 레포지토리는 팀 '한울'에서 설계한 데이터 관리 파이프라인의 일부분입니다. 이 레포에서는 산업 현장에서 동시다발적으로 생성되는 센서 데이터들을 가공 및 적재하는 로직을 포함하고 있습니다. 가공 및 적재된 데이터들은 주기적으로 parquet 형태로 변환되어 hdfs 저장소로 이관됩니다.

# Usage
1. cURL 명령어로 전송되는 request 및 센서 데이터 수신
2. 수신한 센서 데이터의 1차 가공 및 적재 => MySQL, csv
3. 적재된 MySQL 데이터의 2차 가공(parquet) 및 적재 => hdfs

# Structure
### database: MySQL
image
### database: SQLite
image
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
1. 