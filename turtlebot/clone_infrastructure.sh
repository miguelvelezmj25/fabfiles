#!/bin/bash

password=$1

fab -f ../turtlebot.py -p ${password} set_hosts:hosts-placeholder clone_measuring_infrastructure