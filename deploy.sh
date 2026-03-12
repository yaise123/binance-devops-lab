#!/bin/bash

IMG_NAME="binance-web"
CON_NAME="web-server"
PORT="8080"

echo ">>> 正在停止舊的容器..."
docker stop $CON_NAME || true
docker rm $CON_NAME || true

echo ">>> 正在重新打包 Image..."
docker build -t $IMG_NAME .

echo ">>> 正在啟動新的容器並掛載到 $PORT 埠..."
docker run -d -p 8080:80 --name $CON_NAME $IMG_NAME

echo ">>> 部署成功!目前狀態:"
docker ps | grep $CON_NAME
