#!/bin/bash
PROJECT_NAME="beeint"
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/vagrant
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME



apt-get update -y
apt-get upgrade -y
apt-get install -y nginx build-essential python python-dev python-setuptools python-pyodbc libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev git vim gettext

apt-get install -y python3-dev libxml2-dev libxslt-dev

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /vagrant/src/vagrant/nginx/default /etc/nginx/sites-enabled/default
sudo rm -f /etc/nginx/sites-enabled/debugfalse
sudo ln -s /vagrant/src/vagrant/nginx/debugfalse /etc/nginx/sites-enabled/debugfalse


sudo service nginx restart


# virtualenv global setup
if ! command -v pip; then
    easy_install -U pip
fi
if [[ ! -f /usr/local/bin/virtualenv ]]; then
    pip install virtualenv virtualenvwrapper
fi

su - vagrant -c "mkdir -p /home/vagrant/.pip_download_cache"


# virtualenv setup for project
su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR -p /usr/bin/python3 && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    PIP_DOWNLOAD_CACHE=/home/vagrant/.pip_download_cache $VIRTUALENV_DIR/bin/pip install -r $PROJECT_DIR/requirements.txt"


rm -f /home/vagrant/.bashrc
ln -s $PROJECT_DIR/src/vagrant/bashrc /home/vagrant/.bashrc