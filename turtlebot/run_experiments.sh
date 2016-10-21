#!/bin/bash

password=$1

fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-1 run_experiments_single_host:30,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization
fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-2 run_experiments_single_host:30,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization
