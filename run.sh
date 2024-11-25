#!/bin/bash

NUMS=4

docker build -t printer-machine .

for i in $(seq 1 $NUMS); do
    PORT=50$(printf "%03d" "$i") docker run --rm --name printer-machine-$i -d -p 50$(printf "%03d" "$i"):50051 printer-machine
done
