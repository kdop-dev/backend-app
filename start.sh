#!/bin/bash
docker build -t kdop/mydb:0.0.1 .
#docker push kdop/mydb:0.0.1
docker run --rm -p 5000:5000 --name=back-app kdop/mydb:0.0.1