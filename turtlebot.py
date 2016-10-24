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


def run_run_cp1():
    # execute("chmod 751 ./run-cp1.sh")
    execute('./run-cp1.sh')


def set_gazebo_headless():
    execute('sudo apt-get install xserver-xorg-video-dummy')
    execute('echo "source /home/mvelezce/catkin_ws/devel/setup.bash" >> $HOME/.bashrc')
    execute('echo "export ROS_IP=$(hostname -I)" >> $HOME/.bashrc')
    execute('echo "export DISPLAY=:1" >> $HOME/.bashrc')
    execute('echo "export ROS_MASTER_URI=http://$(hostname):11311" >> $HOME/.bashrc')


def remove_last_line_bash_profile():
    execute("sed '$d' $HOME/.bash_profile > $HOME/.bash_profile-new")
    execute("rm $HOME/.bash_profile")
    execute("mv $HOME/.bash_profile-new $HOME/.bash_profile")



