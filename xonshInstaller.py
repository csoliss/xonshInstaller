#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import socket
import pip
import distutils
import re

__version__ = '1.0.0'

app_install = 'Xonsh'
principal_package = 'xonsh'
packages = ('prompt-toolkit', 'PLY', 'Jupyter', 'setproctitle', 'distro')


def check_root():
    """Checking if the user has root privileges. If is True return True"""
    if os.getuid() == 0:
        print("User has root privileges...\n")
        return True  # Return if user is root
    else:
        print("I cannot run as a mortal... Sorry...")
        print(('Run: sudo python3 {}\n'.format(sys.argv[0])))
        exit(1)  # Return if user is not root


def is_connected():
    IS = "www.google.com"
    try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(IS)
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection((host, 80), 2)
        print('System has internet connection...\n')
        return True
    except:
        print('System has not internet connection.')
        print('Connect the system to internet...\n')
        return False


def help_app(_message=False):
    if _message:
        print(('Error: {} \n'.format(_message)))
    print('Usage:')
    print(('    sudo python3 {}\n'.format(sys.argv[0])))
    exit(1)


def install_app():
    print(('\nInstalling {}...\n'.format(app_install)))
    pip.main(['install', principal_package, '-q'])
    for p in packages:
        print(('\nInstalling {}...\n'.format(p)))
        pip.main(['install', p, '-q'])
    exist_line = False
    with open('/etc/shells', "r") as applist:
        executable = distutils.spawn.find_executable('xonsh')
        for line in applist:
            if re.findall('xonsh', line):
                exist_line = True
    if not exist_line:
        with open('/etc/shells', "a") as applist:
            executable = distutils.spawn.find_executable('xonsh')
            applist.write(executable)
    print('\nTo change shells, run:')
    print('chsh -s $(which xonsh)\n')


if __name__ == '__main__':
    print(('Running xonsh Installer\n    Version: {}'.format(__version__)))
    try:
        if check_root():
            if is_connected():
                install_app()
    except KeyboardInterrupt:
        print('\nExit by the user by pressing "Ctrl + c"...\n')

