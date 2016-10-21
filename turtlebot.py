from git import *


def run_experiments_single_host(iterations, dir="."):
    dot('.bash_profile')
    execute('./setup.sh', dir)
    execute('echo $ROS_MASTER_URI')
    dot('.bash_profile')
    execute('./run_experiments.sh ' + iterations, dir)


def set_bash_profile():
    execute('echo "source $HOME/.bashrc" > $HOME/.bash_profile')
    execute('echo " " >> $HOME/.bash_profile')
    execute('echo "source /opt/ros/indigo/setup.bash" >> $HOME/.bash_profile')
    execute('echo "source /home/mvelezce/catkin_ws/devel/setup.bash" >> $HOME/.bash_profile')
    execute('echo "export ROS_IP=$(hostname -I)" >> $HOME/.bash_profile')
    execute('echo "export DISPLAY=:1" >> $HOME/.bash_profile')
    execute('echo " " >> $HOME/.bash_profile')


def remove_last_line_bash_profile():
    execute("sed '$d' $HOME/.bash_profile > $HOME/.bash_profile-new")
    execute("rm $HOME/.bash_profile")
    execute("mv $HOME/.bash_profile-new $HOME/.bash_profile")



