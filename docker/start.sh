#!/bin/bash

sed -i "s/^\(port .*\)$/port $SERVER_PORT/" /etc/redis/redis.conf
echo "redis server port updated to $SERVER_PORT"
sed -i "s/^\(# maxmemory .*\)$/maxmemory $MEM_LIMIT/" /etc/redis/redis.conf
echo "redis server memory limit updated to $MEM_LIMIT"

echo "Starting redis server"
redis-server /etc/redis/redis.conf