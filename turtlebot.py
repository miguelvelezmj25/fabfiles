from git import *


def run_experiments_single_host(iterations, dir="."):
    dot('.bash_profile')
    execute('./setup.sh', dir)
    run('echo $ROS_MASTER_URI')
    dot('.bash_profile')
    execute('./run_experiments.sh ' + iterations, dir)


def clone_measuring_infrastructure():
    rm('catkin_ws', options='-rf')
    git_clone('https://github.com/miguelvelezmj25/turtlebot-monitoring-infrastructure.git',
              options='-b master --recursive', name='catkin_ws')
    catkin_make('./catkin_ws')
    # You need to have the following files for these commands to work
    scp('./files/.dbconfig', '.dbconfig', './catkin_ws/src/measurement/localization')
    scp('./files/.serverconfig', '.serverconfig', './catkin_ws/src/measurement/localization')


def catkin_make(dir="."):
    execute('catkin_make', dir)


def set_bash_profile():
    run('echo "source $HOME/.bashrc" > $HOME/.bash_profile')
    run('echo " " >> $HOME/.bash_profile')
    run('echo "source /opt/ros/indigo/setup.bash" >> $HOME/.bash_profile')
    run('echo "source $HOME/catkin_ws/devel/setup.bash" >> $HOME/.bash_profile')
    run('echo "export ROS_IP=$(hostname -I)" >> $HOME/.bash_profile')
    run('echo "export DISPLAY=:1" >> $HOME/.bash_profile')
    run('echo " " >> $HOME/.bash_profile')


def set_gazebo_headless():
    run('sudo apt-get install xserver-xorg-video-dummy')
    run('echo "source $HOME/catkin_ws/devel/setup.bash" >> $HOME/.bashrc')
    run('echo "export ROS_IP=$(hostname -I)" >> $HOME/.bashrc')
    run('echo "export DISPLAY=:1" >> $HOME/.bashrc')
    run('echo "export ROS_MASTER_URI=http://$(hostname):11311" >> $HOME/.bashrc')


def remove_last_line_bash_profile():
    execute("sed '$d' $HOME/.bash_profile > $HOME/.bash_profile-new")
    execute("rm $HOME/.bash_profile")
    execute("mv $HOME/.bash_profile-new $HOME/.bash_profile")



