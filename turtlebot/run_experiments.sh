#!/bin/bash

password=$1

fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-1 run_experiments_single_host:1000,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization