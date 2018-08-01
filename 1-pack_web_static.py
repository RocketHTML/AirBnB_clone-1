#!/usr/bin/python3
"""
    Deploy web_static on servers
"""
from fabric.api import *
from datetime import datetime
import os

web1 = "35.237.187.19"
web2 = "35.196.245.228"
lb = "104.196.146.126 lb"
loc = "localhost"

env.hosts = []
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'


def do_pack():
    web = 'web_static'
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    tar = 'versions/{0}_{1}.tgz'.format(web, time)
    local('mkdir -p versions')
    local('tar cvzf {} {}'.format(tar, web))
    try:
        size = os.path.getsize(tar)
        print('{} packed: {} -> {}Bytes'.format(web, tar, size))
        return tar
    except os.error:
        return None
