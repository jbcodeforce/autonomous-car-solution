#!/bin/bash
echo "##########################################################"
echo " A docker image for python  development: "
echo
name="jbcodeforce/jbpython"
port=5000
if [[ $# != 0 ]]
then
    name=$1
    port=$2
fi
if [[ -z "$IPADDR" ]]
then
    export IPADDR=$(ifconfig en0 |grep "inet " | awk '{ print $2}')
fi

docker run --rm -e DISPLAY=$IPADDR:0 -v /tmp/.X11-unix:/tmp/.X11-unix  -v $(pwd)/..:/app -it  -p $port:$port $name bash 
