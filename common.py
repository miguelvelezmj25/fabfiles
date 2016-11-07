from fabric.api import run, put
from fabric.context_managers import cd
from fabric.state import env
from fabric.contrib.project import rsync_project


def set_hosts(hosts_file):
    env.hosts = []
    with open(hosts_file, 'r') as hosts:
        for host in hosts:
            env.hosts.append(host)


def pwd(dir='.'):
    with cd(dir):
        run('pwd')


def rm(file, options=None, dir="."):
    with cd(dir):
        command = 'rm '

        if options is not None:
            command += '{} '.format(options)

        command += '{}'.format(file)
        run(command)


def reboot():
    run('sudo reboot')


def whoami():
    run('whoami')


def mkdir(dir):
    run('mkdir {}'.format(dir))


def sleep(time):
    run('sleep {}'.format(time))


def dot(file, dir='.'):
    with cd(dir):
        run('. {}'.format(file))


def execute(command, dir='.'):
    with cd(dir):
        run(command)


def scp(local, remote, dir='.'):
    with cd(dir):
        put(local, remote)


def rsync(local, remote, dir='.'):
    with cd(dir):
        rsync_project(local_dir=local, remote_dir=remote)
