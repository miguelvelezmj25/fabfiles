from common import *


def git_clone(repo, options=None, name=None, dir="."):
    with cd(dir):
        command = 'git clone '

        if options is not None:
            command += '{} '.format(options)

        command += '{} '.format(repo)

        if name is not None:
            command += '{} '.format(name)

        run(command)


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
        run('git checkout {}'.format(options))


def git_submodule(options='', dir='.'):
    with cd(dir):
        run('git submodule {}'.format(options))
