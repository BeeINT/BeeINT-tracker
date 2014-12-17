#!/bin/bash
PROJECT_NAME="beeint"
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/vagrant
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME



ESC_SEQ="\x1b["
COL_RESET=$ESC_SEQ"39;49;00m"
COL_RED=$ESC_SEQ"31;01m"
COL_GREEN=$ESC_SEQ"32;01m"
COL_YELLOW=$ESC_SEQ"33;01m"
COL_BLUE=$ESC_SEQ"34;01m"
COL_MAGENTA=$ESC_SEQ"35;01m"
COL_CYAN=$ESC_SEQ"36;01m"


# have to restart because the configurations are not linked on bootup
sudo service nginx restart

echo " * Starting runserver"
su - vagrant -c "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && screen -S 'beeint_run' -d -m invoke server; sleep 1"

echo -e "$COL_YELLOW-------------WHAT NOW?-------------------------------------------------- $COL_RESET"
echo -e "$COL_YELLOW runserver:                 http://localhost:8000 $COL_RESET"
echo -e "$COL_YELLOW nginx:                     http://localhost:8001 $COL_RESET"
echo -e "$COL_YELLOW nginx für debug=False:     http://localhost:8002 $COL_RESET"
echo -e "$COL_YELLOW------------------------------------------------------------------------ $COL_RESET"
