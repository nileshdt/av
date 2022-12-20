# FROM ubuntu:disco

# RUN apt-get update \
#   && apt-get install --no-install-recommends -y \
#   git \
#   build-essential \
#   python3 \
#   python3-pip \
#   && rm -rf /var/lib/apt/lists/*

# WORKDIR /home/app

# COPY requirements.txt .

# RUN pip3 install --upgrade pip \
#   && pip3 install --upgrade setuptools \
#   && pip3 install -r requirements.txt

# COPY . .

# ENTRYPOINT ["python3", "user/main.py"]
FROM python:3.10-slim-bullseye

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential default-libmysqlclient-dev \
  && pip install --no-cache-dir --upgrade pip

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

EXPOSE 50053

CMD ["python3", "server.py"]