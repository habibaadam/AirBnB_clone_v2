#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy:"""

from fabric.api import *
import os 
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.205.99.166', '100.26.122.165']


def do_pack():
    """ Generates a .tgz archive from the contents of the
    web_static folder
    """
    now = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                         now.month,
                                                         now.day,
                                                         now.hour,
                                                         now.minute,
                                                         now.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
