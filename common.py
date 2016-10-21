from fabric.api import run
from fabric.context_managers import cd
from fabric.state import env


def set_hosts(hosts_file):
    env.hosts = []
    with open(hosts_file, 'r') as hosts:
        for host in hosts:
            env.hosts.append(host)


def pwd(dir='.'):
    with cd(dir):
        run('pwd')


def reboot():
    execute('sudo reboot')


def whoami():
    run('whoami')


def mkdir(dir):
    run('mkdir {0}'.format(dir))


def sleep(time):
    run('sleep {0}'.format(time))


def dot(file, dir='.'):
    with cd(dir):
        run('. {0}'.format(file))


def execute(command, dir='.'):
    with cd(dir):
        run(command)
