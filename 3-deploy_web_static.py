#!/usr/bin/python3
"""Full Deplpoyment"""
from fabric.api import local
from datetime import datetime
from fabric.api import put, run, env
import os
env.hosts = ["34.75.67.199", "35.237.13.196"]


def do_pack():
    """compresses the web static folder into an archive"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(now))
    return "versions/web_static_{}".format(now)


def do_deploy(archive_path):
    """deploys archaives to the servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        archfile = archive_path.split('/')[-1]
        arch = archfile.split('.')[0]
        put(archive_path, "/tmp/{}".format(archfile))
        run("mkdir /data/web_static/releases/{}/".format(arch))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archfile, arch))
        run("rm /tmp/{}".format(archfile))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(arch, arch))
        run("rm -rf /data/web_static/releases/{}/web_static".format(arch))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(arch))
        return True
    except Exception as e:
        return False


def deploy():
    """packs and desploys webstatic"""
    archpath = do_pack()
    if not archpath:
        return False
    return do_deploy(archpath)
