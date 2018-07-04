FROM ubuntu:latest

#install redis
RUN \
  apt-get update && \
  apt-get install -y redis-server && \
  sed -i 's/^\(bind .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(daemonize .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf

#set default environment parameters
ENV SERVER_PORT 6379
ENV MEM_LIMIT   2048000

#copy the script to start the redis server
COPY start.sh .
RUN chmod ug+x start.sh

# Define default command.
CMD ["./start.sh"]

# Expose ports.
EXPOSE ${SERVER_PORT}
