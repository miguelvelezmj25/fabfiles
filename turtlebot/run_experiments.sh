#!/bin/bash

password=$1

fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-1 run_experiments_single_host:740,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization
fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-2 run_experiments_single_host:740,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization
fab -P -f ../turtlebot.py -p ${password} set_hosts:hosts-3 run_experiments_single_host:740,/home/mvelezce/catkin_ws/src/cp1_gazebo/instructions/localization
