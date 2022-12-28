# FROM python:3.10-slim-bullseye

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends --no-install-suggests protobuf-compiler \
#     build-essential  \
#     && pip install grpcio-tools && \
#     && pip install --no-cache-dir --upgrade pip

# WORKDIR /app
# COPY ./requirements.txt /app/
# RUN pip install --no-cache-dir --requirement /app/requirements.txt
# COPY . /app

# EXPOSE 8080
# ENV PYTHONUNBUFFERED=1
# CMD ["python3", "server.py"]


FROM python:3.10-slim-bullseye

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app


RUN apt-get -y update && apt-get install -y protobuf-compiler && \
    pip install grpcio-tools git && \
    pip install -r requirements.txt && \
    bash python.sh

ENTRYPOINT python main.py