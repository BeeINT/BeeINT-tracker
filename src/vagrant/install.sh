#!/bin/bash
PROJECT_NAME="equilibeeum"
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/vagrant
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME



apt-get update -y
apt-get install -y build-essential python python-dev python-setuptools python-pyodbc libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev git vim gettext

gem install compass -v 0.13.alpha.4 --pre
gem install compass-blueprint


# virtualenv global setup
if ! command -v pip; then
    easy_install -U pip
fi
if [[ ! -f /usr/local/bin/virtualenv ]]; then
    pip install virtualenv virtualenvwrapper
fi

## bash environment global setup
cp -p $PROJECT_DIR/src/vagrant/bashrc /home/vagrant/.bashrc
su - vagrant -c "mkdir -p /home/vagrant/.pip_download_cache"


# virtualenv setup for project
su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    PIP_DOWNLOAD_CACHE=/home/vagrant/.pip_download_cache $VIRTUALENV_DIR/bin/pip install -r $PROJECT_DIR/requirements.txt"

echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc


# Django project setup
#su - vagrant -c "source $VIRTUALENV_DIR/bin/activate && pip install -r requirements.txt"
