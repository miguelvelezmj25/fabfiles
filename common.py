from fabric.api import run


def pwd():
    run('pwd')


def whoami():
    run('whoami')


def mkdir(dir):
    run('mkdir {0}'.format(dir))
