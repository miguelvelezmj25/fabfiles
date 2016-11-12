#!/bin/bash
# Script to recursively pull the infrastructure repo. It pulls from the master branch.

hosts=$1
password=$2

fab -f ../git.py -p ${password} set_hosts:${hosts} git_checkout:'-- .',./catkin_ws git_pull:./catkin_ws git_submodule:'update --remote',./catkin_ws