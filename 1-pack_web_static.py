#!/usr/bin/python3
"""Generates a .tgz arhcive from the files in web_static"""

import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """ Generates a .tgz archive from the contents of the
    web_static folder
    """
    now = datetime.today()
    file = f"versions/web_static_{now.year}{now.month}{now.day}{now.hour}\
    {now.minute}{now.second}.tgz"

    print(f"Packing web_static to {file}")
    if not os.path.exists("versions/"):
        local("mkdir versions/")

    res = local(f"tar -cvzf {file} web_static/")
    if res.failed:
        return None
    else:
        archive_size = os.path.getsize(file)
        print(f"web_static packed: {file} -> {archive_size}Bytes")
        return file
