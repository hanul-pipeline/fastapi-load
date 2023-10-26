FROM apache/hadoop:3

# Install required packages
RUN sudo yum install -y python3 python3-pip libmysqlclient-dev

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r /app/requirements.txt

EXPOSE 80

# ENV NAME World

CMD ["python3", "/app/main.py"]
