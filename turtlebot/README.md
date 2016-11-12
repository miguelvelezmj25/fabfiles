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

* xorg.conf

  Configuration file for running the simulator headless. It must be copied to the ```$HOME``` folder in both 
  the TurtleBot and Simulator machines.
  
## Additional Files

The following files contain sensitive data that is unique to each individual who uses this
repo. Therefore, they are not provided in this repo and must be copied in the machines running
the TurtleBot and Simulator. You have to place them int the ```/files``` directory in order for
them to be copied. Read the ```/files/TODO``` file for more information.

* .dbconfig. **NOT INCLUDED** 

  This file is used to connect to the database that stores the jobs and saves the data from
the executions. It must have the following structure:

        [server]
        hostname = hostname
        user = user
        password = password
        database = database

* .serverconfig. **NOT INCLUDED** 

  This file is used to configure the communication between the TurtleBot and Simulator machines.
It mus have the following structure:

        [serverX]
        simulator = serverY
        username = username
        password = password
  
  This means that ```serverX``` will act as the TurtleBot machine and will communicate with ```serverY```
  to run the simulator in that machine. **WARNING: Machines cannot run TurtleBot code and the simulator
  at the same time**.

## Scripts

* run-cp1.sh
  
  Script to start the headless server. It must be copied to the ```$HOME``` folder in both 
  the TurtleBot and Simulator machines and executed on both machines.

* clone_infrastructure.sh

  Script to recursively clone the [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
  repo. It clones the ```master``` branch. You need to pass a ```password``` 
  and ```hosts``` to run this script.

* set_bash_profile.sh

  Script to write to the ```.bash_profile``` of the TurtleBot and Simulator machines. This script
  will delete and override your ```.bash_profile```. You need to pass a ```password``` 
  and ```hosts``` to run this script.

* git_pull.sh

  Script to recursively pull the [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
  repo. It pulls from the ```master``` branch. You need to pass a ```password``` 
  and ```hosts``` to run this script.

* run_experiments.sh

  Script to run the experiments across multiple machines. The commands are send in parallel and will terminate 
  executing once all machines have completed running the experiments. You need to pass a ```password```, ```hosts```, 
  and ```iterations``` to run this script. The number of executions are the number of experiments each machine 
  will run.

## Running Experiments

The following instructions are the ones we followed to get the [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
cloned and ready to run experiments. You can use a different approach besides this project to set up and update the 
[turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure).
However, you must execute and follow the same logic that the scripts that use the fabfiles execute. You have
to check the [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
repo for instructions on how to complete some of the following steps.

1. Install and clone the require software, files, and projects in your master machine and your servers. This 
project must be cloned in your master machine. The [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
project must be cloned and setup in your servers. You can do so by running

        clone_infrastructure.sh {hosts} {password}
        set_bash_profile.sh {hosts} {password}

  from the master machine. They will setup the [turtlebot-monitoring-infrastructure](https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure) 
  project, the necessary files used by it, and the ```.bash_profile``` in your servers. 
  Remember that you must provide the ```.dbconfig``` and ```.serverconfig``` files in this 
  project to be copied to your servers.

2. Run the headless server in your server machines. 

3. Add configurations and jobs to the database.

4. Execute the experiment you stored in the database. You can do so by running

        run_experiments.sh {hosts} {password} {iterations}
        
  from the master machine.