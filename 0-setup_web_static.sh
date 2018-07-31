#!/usr/bin/env bash
# Configured nginx server for custom header
location="location /hbnb_static {\n alias /data/web_static/current; \n}\n"
file=/etc/nginx/sites-available/default

sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
curl dockerhearts.online > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
cp ${file}.bak $file
sudo sed -i*.bak "/^\tlocation/i $location" $file
sudo service nginx restart
