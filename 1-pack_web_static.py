#!/usr/bin/python3
"""Generates a .tgz arhcive from the files in web_static"""

import os.path
from datetime import datetime
from fabric.api import local

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
