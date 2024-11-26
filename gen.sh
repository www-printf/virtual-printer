#!/bin/bash

protoc -I. --go_out=client \
    --go-grpc_out=client \
    --go_opt=Mproto/print.proto=proto/ \
    --go_opt=Mproto/print_service.proto=proto/ \
    --go-grpc_opt=Mproto/print.proto=proto/ \
    --go-grpc_opt=Mproto/print_service.proto=proto/ \
    proto/*.proto

python3 -m grpc_tools.protoc -I. --python_out=server --grpc_python_out=server proto/*.proto
