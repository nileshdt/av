#!/bin/bash

# python3 -m grpc_tools.protoc --proto_path=./protos --python_out=./gateway/proto --grpc_python_out=./gateway/proto proto/article/article.proto

# python3 -m grpc_tools.protoc --proto_path=./protos --python_out=./gateway/proto --grpc_python_out=./gateway/proto proto/user/user.proto

python3 -m grpc_tools.protoc --proto_path=./protos --python_out=./gateway/proto/  --pyi_out=./gateway/proto/ --grpc_python_out=./gateway/proto/ ./protos/user/user.proto


if [[ $(uname -s) == Darwin* ]];
then
    sed -i '' 's/from article import/from . import/1' gateway/proto/article/article_pb2_grpc.py
    sed -i '' 's/from user import/from . import/1' gateway/proto/user/user_pb2_grpc.py
else
    sed -i 's/from article import/from . import/1' gateway/proto/article/article_pb2_grpc.py
    sed -i 's/from user import/from . import/1' gateway/proto/user/user_pb2_grpc.py
fi

