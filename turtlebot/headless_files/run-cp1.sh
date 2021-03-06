#!/bin/bash

#Start the headless XServer
Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./1.log -config ./xorg.conf :1 & export X_PID=$!

# Method to kill the X-Server when Ctrl-C is pressed
killX() {
  echo "Ctrl-C pressed - killing headless server with pid $X_PID";
  kill -9 $X_PID
  exit 1
}

trap killX INT
