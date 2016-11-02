#!/bin/bash

password=$1

fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-placeholder run_experiments_single_host:110,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization