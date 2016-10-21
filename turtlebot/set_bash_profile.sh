#!/bin/bash

password=$1

fab -P -f ../turtlebot.py -p ${password} set_hosts:turtlebot-hosts set_bash_profile