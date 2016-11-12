#!/bin/bash
# Script to write to the .bash_profile of the TurtleBot and Simulator machines. This script will delete and override
# your ```.bash_profile```

hosts=$1
password=$2

fab -P -f ../turtlebot.py -p ${password} set_hosts:${hosts} set_bash_profile
