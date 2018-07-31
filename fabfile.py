#!/usr/bin/python3
"""
    Setup and Deploy on servers
"""
from fabric.api import *


web1 = "35.237.187.19"
web2 = "35.196.245.228"
lb = "104.196.146.126 lb"

env.hosts = [web1, web2]
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'


def configure_nginx():
    """ 
        Push and execute either bash or puppet file.
        They'll create /data/webstatic/[releases|shared] dirs.
            As well as install nginx and point it at a default index.html
    """
    put('./0-setup_web_static.sh', '/tmp/server_setup.sh', mode=744)
    run('sudo /tmp/server_setup.sh')
