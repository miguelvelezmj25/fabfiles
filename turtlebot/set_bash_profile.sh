#!/bin/bash

password=$1

fab -P -f ../turtlebot.py -p ${password} set_hosts:turtlebot_hosts set_hosts:turtlebot_hosts set_bash_profile