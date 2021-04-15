#!/usr/bin/env bash
# sets up web server for deployment
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo printf '%s\n' \
'<html>' \
'  <head>' \
'  </head>' \
'  <body>' \
'    Holberton School' \
'  </body>' \
'</html>' \
| sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
new_string="location /hbnb_static {alias /data/web_static/current/;}"
sudo sed -i "/listen \[::\]:80 default_server;/a $new_string" /etc/nginx/sites-enabled/default
sudo service nginx restart
