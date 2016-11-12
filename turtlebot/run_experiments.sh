#!/bin/bash
# Script to run the experiments across multiple machines. The commands are send in parallel and will terminate
# executing once all machines have completed running the experiments. You need to pass a ```password```, ```hosts```,
# and ```executions``` to run this script. The number of executions are the number of experiments each machine will run.

hosts=$1
password=$2
executions=$3

fab -P -f ../turtlebot.py -p ${password} set_hosts:${hosts} run_experiments_single_host:${executions},/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization