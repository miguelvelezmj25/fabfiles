#!/bin/bash

password=$1

fab -P -f ../git.py -p ${password} set_hosts:turtlebot_hosts git_checkout:'-- .',./catkin_ws git_pull:./catkin_ws git_submodule:'update --remote',./catkin_ws