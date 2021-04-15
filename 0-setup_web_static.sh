#!/usr/bin/env bash
# sets up web server for deployment
dpkg -s nginx &> /dev/null
if [ $? -ne 0 ]; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi
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
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
new_string="location /hbnb_static {alias /data/web_static/current/;}"
sudo sed -i "/listen \[::\]:80 default_server;/a $new_string" /etc/nginx/sites-available/default
sudo service nginx restart
