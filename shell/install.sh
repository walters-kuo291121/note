#!/usr/bin/env bash

#cat /var/log/apt/history.log
#unzip tree 
#python3 python3-pip python3-setuptools git
#traceroute net-tools
#postgresql-client

＃It has been mentioned that you can add the -y flag to apt-get to answer Yes to all the prompts. This usually only saves you from having to say Yes once, anyways. It's nice to know about the -y flag, but be careful, because it can also automatically remove things that you may not want removed. Typically, I omit the -y flag and manually review all Added or Removed packages to prevent myself from making mistakes that could have horrible affects on my computer. However, apt-get upgrade -y seems to be a good option and less volatile.

all_package = ['unzip', 'tree', 'netstaus']

sudo apt-get install package-x package-y -y
sudo apt-get upgrade package-x package-y -y