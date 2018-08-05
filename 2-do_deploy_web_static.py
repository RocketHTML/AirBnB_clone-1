#!/usr/bin/python3
"""
    Deploy web_static on servers
"""
from fabric.api import *
from datetime import datetime
import os

web1 = "35.237.187.19"
web2 = "35.196.245.228"
lb = "104.196.146.126"
loc = "localhost"

env.hosts = [web1, web2]
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/id_rsa'

@runs_once
def do_pack():
    ''' compress local new release to tar'''
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

def do_deploy(archive_path):
    ''' add new release from tar and point symlink at it '''
    put(archive_path, '/tmp/')
    no_ext = re.sub('.tgz$', '', archive_path)
    no_pre = re.sub('^.*/', '', archive_path) 
    fn = re.sub('^.*/', '', no_ext)

    web = 'web_static'
    webdir = '/data/{}'.format(web)
    releases = '{}/releases'.format(webdir)
    new_rel = '{}/{}'.format(releases, fn)
    run('mkdir -p {}/'.format(new_rel))
    run('tar -xzf /tmp/{} -C {}/'.format(no_pre, new_rel))
    run('rm /tmp/{}'.format(no_pre))
    run('mv {0}/web_static/* {0}'.format(new_rel))
    run('rm -rf {}/web_static'.format(new_rel))

    run('rm -rf {}/current'.format(webdir))
    run('ln -s {} {}/current'.format(new_rel, webdir))

    print("new version deployed!")