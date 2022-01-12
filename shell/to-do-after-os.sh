#!/bin/bash

AWS envirment
NLB + EC2 + RDS + S3

#things to do after installing os 
subdomain + AWS ACM

#check and install package update
sudo apt-get update && sudo apt-get dist-upgrade

sudo apt -y install vim bash-completion wget
sudo apt-get install -y python3 python3-pip nginx python3-setuptools git
sudo pip3 install uwsgi virtualenv Flask flask-restful gunicorn

#conifg postgresql://postgres:6NqLTvFAjJLJPKxo@database-dev.ci68ranogp85.ap-northeast-1.rds.amazonaws.com/topyl_dev

nginx config
dev-api
dev-m
dev-www


#admin: topyl-admin master
clone 
h5 : topyl-h5 master
pc : topyl-pc master
backend api: topyl-backend master

clone backend api
cd ./folder
python3 -m pip install -r requirements.txt
gunicorn -b 127.0.0.1:5000 -w 4 app:app &


sudo apt update -y
sudo curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs npm
sudo node -v && npm -v

clone h5
cd ./folder
# install dependencies
$ npm install

# build for production and launch server
#npm run build:dev
npm run build:uat
#npm run build:prod
npm run start & 



clone pc
cd ./folder
# install dependencies
$ npm install

# build for production and launch server
#npm run build:dev
npm run build:uat
#npm run build:prod
npm run start & 