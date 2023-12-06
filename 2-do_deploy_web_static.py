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
    now = datetime.today()
    file = f"versions/web_static_{now.year}{now.month:02d}{now.day:02d}{now.hour:02d}" \
           f"{now.minute:02d}{now.second:02d}.tgz"

    print(f"Packing web_static to {file}")
    if not os.path.exists("versions/"):
        local("mkdir versions/")

    res = local(f"tar -cvzf {file} web_static/")
    if res.failed:
        return None
    else:
        archive_size = os.path.getsize(file)
        print(f"web_static packed: {file} -> {archive_size} Bytes")
        return file

def do_deploy(archive_p):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_p):
        return False

    path = archive_p.split('/')
    archive_file = path[1]
    splitted_arhive = archive_file.split('.')

    server_archive_path = f'/tmp/{archive_file}'
    xarch_path = f'/data/web_static/releases/{splitted_arhive[0]}'

    if put(archive_p, '/tmp/').failed:
        return False
    if run(f'mkdir -p {xarch_path}').failed:
        return False
    if run(f'tar -xzf {server_archive_path} -C {xarch_path}').failed:
        return False
    if run(f'rm {server_archive_path}').failed:
        return False
    if run(f'mv {xarch_path}/web_static/* {xarch_path}').failed:
        return False
    if run(f'rm -rf {xarch_path}/web_static').failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run(f'ln -s {xarch_path} /data/web_static/current').failed:
        return False

    print('New version deployed!')
    return True
