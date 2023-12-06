#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy:"""

from fabric.api import *
from os import path
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.205.99.166', '100.26.122.165']
