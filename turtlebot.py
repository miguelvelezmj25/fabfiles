from git import *


def run_experiments_single_host(iterations, dir="."):
    dot('.bash_profile')
    execute('./setup.sh', dir)
    execute('echo $ROS_MASTER_URI')
    dot('.bash_profile')
    execute('./run_experiments.sh ' + iterations, dir)
    # execute('python -c "import latest_config_to_csv as m; m.save_host()"', dir)


def fix():
    execute("sed '$d' $HOME/.bash_profile > $HOME/.bash_profile-new")
    execute("rm $HOME/.bash_profile")
    execute("mv $HOME/.bash_profile-new $HOME/.bash_profile")