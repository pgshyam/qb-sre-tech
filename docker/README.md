Docker file which get the latest ubuntu version, install the redis server during build and when container is launched, starts redis with option to configure port and memory limit

Defines 2 environment parameters
  - SERVER_PORT - port used by redis server 
      default : 6379
  - MEM_LIMIT - maxmemory limit to be set (in bytes)
      default : 2MB

- start.sh 
    script file which updates the redis configuration file using the enviornment parameters before starting the redis server.

usage : 
  example : 
      docker run -e SERVER_PORT=8090 -e MEM_LIMIT=4096000 --name redis-server-1 redis-1-image
      starts redis in container listening on port 8090 and maxmemory limit of 4MB