
FROM python

# RUN apt-get update \
#   && apt-get install -y --no-install-recommends --no-install-suggests \
#   build-essential default-libmysqlclient-dev git  protobuf-compiler  \
#   && pip install  --no-cache-dir --upgrade pip 

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY ./requirements.txt /app/
# RUN pip install  protobuf grpcio-tools grpcio contextlib3 "grpclib[protobuf]"  --no-cache-dir --requirement /app/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

EXPOSE 50011

CMD ["python3", "server.py"]