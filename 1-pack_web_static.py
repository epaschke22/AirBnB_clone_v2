#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """compresses the web static folder into an archive"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(now))
    return "versions/web_static_{}".format(now)
