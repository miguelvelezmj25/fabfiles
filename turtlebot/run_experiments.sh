#!/bin/bash

hosts=$1
password=$2
executions=$3

fab -P -f ../turtlebot.py -p ${password} set_hosts:${hosts} run_experiments_single_host:${executions},/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization