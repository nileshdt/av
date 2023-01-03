
FROM python

WORKDIR /app
COPY ./requirements.txt /app/

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential   \
  && pip install  --no-cache-dir --upgrade pip   \
  && pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1


# RUN pip install  protobuf grpcio-tools grpcio contextlib3 "grpclib[protobuf]"  --no-cache-dir --requirement /app/requirements.txt
# RUN python -m pip install --no-cache-dir --upgrade pip
# RUN pip install -r requirements.txt
COPY . /app

EXPOSE 5001

CMD ["python3", "server.py"]