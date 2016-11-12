#!/bin/bash
# Script to recursively clone the infrastructure repo. It clones the master branch.

hosts=$1
password=$2

fab -f ../turtlebot.py -p ${password} set_hosts:${hosts} clone_measuring_infrastructure
