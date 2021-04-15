#!/usr/bin/python3
"""Full Deplpoyment"""
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy


def deploy():
    """packs and desploys webstatic"""
    archpath = do_pack()
    if not archpath:
        return False
    return do_deploy(archpath)
