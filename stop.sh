#!/bin/sh

PIDS=`ps -ef | grep python | grep -v grep | awk -F' ' '{print $2}'`

for PID in $PIDS;
do
        kill -9 $PID;
done;