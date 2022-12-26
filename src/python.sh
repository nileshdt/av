#!/bin/bash

python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpclib_python_out=. protos/user/user.proto


# if [[ $(uname -s) == Darwin* ]];
# then
#     # sed -i '' 's/from article import/from . import/1' gateway/proto/article/article_pb2_grpc.py
#     sed -i '' 's/from user import/from . import/1' gateway/proto/user/user_grpc.py
#     sed -i '' 's/from user import/from . import/1' gateway/proto/user/user_pb2.py
#     sed -i '' 's/from user import/from . import/1' gateway/proto/user/user_pb2.pyi
# else
#     # sed -i 's/from article import/from . import/1' gateway/proto/article/article_pb2_grpc.py
#     sed -i 's/from user import/from . import/1' gateway/proto/user/user_grpc.py
#     sed -i 's/from user import/from . import/1' gateway/proto/user/user_pb2.py
#     sed -i 's/from user import/from . import/1' gateway/proto/user/user_pb2.pyi
# fi

cp -r ./protos/user/*.py* ./gateway/proto/user/
cp -r ./protos/user/*.py* ./user/proto/user/
