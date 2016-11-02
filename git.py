from common import *


def git_clone(repo, name=None, dir="."):
    with cd(dir):
        if name is None:
            run('git clone {}'.format(repo))
        else:
            run('git clone {} {}'.format(repo, name))


def git_clone_recursive(repo, name=None, dir="."):
    with cd(dir):
        if name is None:
            run('git clone --recursive {}'.format(repo))
        else:
            run('git clone --recursive {} {}'.format(repo, name))


def git_remote_update(dir='.'):
    with cd(dir):
        run('git remote update')


def git_status(dir='.'):
    with cd(dir):
        run('git status')


def git_pull(dir='.'):
    with cd(dir):
        run('git pull')


def git_checkout(options='', dir='.'):
    with cd(dir):
        run('git checkout {0}'.format(options))


def git_submodule(options='', dir='.'):
    with cd(dir):
        run('git submodule {0}'.format(options))

