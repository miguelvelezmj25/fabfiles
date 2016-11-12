# turtlebot

This folder contains fabfiles and scripts useful for the 
[turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
project. In parallel, they set up and update the project to run experiments. They interact directly with
the machines running the TurtleBot.

All of the scripts require the password of the destination machines to be executed. 

## Files

The following files are servers that we use in our project. Nevertheless, they can be
overridden with your servers.

* turtlebot-hosts

  List of all of our servers.

* hosts-1, hosts-2, hosts-3, hosts-placeholder

  List of servers acting as TurtleBot machines. You have to reference to your ```.serverconfig``` file
  from the [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
  project to decide which servers go in each file to avoid unexpected behavior. For example, if this is your ```.serverconfig```
  file:
  
        [serverX]
        simulator = serverY
        username = username
        password = password
        
        [serverY]
        simulator = serverX
        username = username
        password = password
        
  Your hosts file should only contain either serverX or serverY. If you include both in a single file and run 
  the experiments, you would not get any data since the machines would not be able to communicate. **WARNING: 
  Machines cannot run TurtleBot code and the simulator at the same time**.

## Scripts

* clone_infrastructure.sh

  Script to recursively clone the infrastructure repo. It clones the ```master``` branch. You need to pass a ```password``` 
  and ```hosts``` to run this script.

* set_bash_profile.sh

  Script to write to the ```.bash_profile``` of the TurtleBot and Simulator machines. This script
  will delete and override your ```.bash_profile```. You need to pass a ```password``` 
  and ```hosts``` to run this script.

* git_pull.sh

  Script to recursively pull the infrastructure repo. It pulls from the ```master``` branch. You need to pass a ```password``` 
  and ```hosts``` to run this script.

* run_experiments.sh

  Script to run the experiments across multiple machines. The commands are send in parallel and will terminate 
  executing once all machines have completed running the experiments. You need to pass a ```password```, ```hosts```, 
  and ```executions``` to run this script. The number of executions are the number of experiments each machine 
  will run.
