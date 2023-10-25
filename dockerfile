FROM python:3.11.5

WORKDIR /api

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD python3 main.py

