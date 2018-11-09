#!/bin/sh

python -m grpc_tools.protoc -I ./protos --python_out=./generated --grpc_python_out=./generated ./protos/employee_guide.proto
