from fabric import api
import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__), 'src/beetracker')


@api.task
def run():
    """run the dev server"""
    with api.lcd(PROJECT_DIR):
        api.local('python manage.py runserver 0:8000')

@api.task
def celery():
    """start the celery server"""
    with api.lcd(PROJECT_DIR):
        api.local('python manage.py celeryd -E -B --concurrency=1')
   
@api.task
def translations():
    """make and compile translations

      .. note:: restricted usage
      """
    make_translations()
    compile_translations()

@api.task
def make_translations():
    """make translations

      .. note:: restricted usage
      """
    with api.lcd(PROJECT_DIR):
        api.local('python manage.py makemessages --all --no-wrap --no-location')

@api.task
def compile_translations():
    """compile translations
      .. note:: restricted usage
      """
    with api.lcd(PROJECT_DIR):
        api.local('python manage.py compilemessages')
