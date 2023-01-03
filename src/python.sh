#!/bin/bash

cd protos/user
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpclib_python_out=. user.proto
cd ..
cd email
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpclib_python_out=. email.proto
cd ..
cd audit
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpclib_python_out=. audit.proto
cd ../..

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

cp -r ./protos/user/*.py* ./gateway/
cp -r ./protos/user/*.py* ./user
cp -r ./protos/email/*.py* ./email
cp -r ./protos/email/*.py* ./gateway/
cp -r ./protos/audit/*.py* ./audits
cp -r ./protos/audit/*.py* ./gateway/
