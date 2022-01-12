#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3 python3-pip nginx python3-setuptools git
sudo pip3 install uwsgi virtualenv Flask flask-restful gunicorn

sudo mkdir -p /var/www/
cd /var/www/
echo "<h1>Hello world!</h1>" | tee index.html

sudo mkdir -p ~/app
cd ~/app
touch app.py
echo "
from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {\"hello\": \"world\"}
api.add_resource(HelloWorld, \"/\")
if __name__ == \"__main__\":
    app.run(debug=True, host=\"0.0.0.0\")
" | tee app.py




echo "
server {
        listen 80;
        index index.html;
        server_name gunicorn.topyl666.com;
        location / {
                proxy_pass http://127.0.0.1:5000;
                # Redefine the header fields that NGINX sends to the upstream server
               proxy_set_header Host \$host;
               proxy_set_header X-Real-IP \$remote_addr;
               proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        }
        location /static {
                alias /var/www/;
                autoindex on;
        }
}
" | tee /etc/nginx/sites-available/gunicorn
sudo service nginx reload
sudo service nginx start

cd ~/app/
python3 -m pip install -r requirements.txt
gunicorn -b 127.0.0.1:5000 app:app
