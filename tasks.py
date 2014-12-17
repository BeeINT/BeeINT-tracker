from invoke import task
from invoke import run 
import os

PROJECT_DIR = os.path.join(os.path.dirname(__file__), 'src/beetracker')



def local(command):
	run("cd {0} && {1}".format(PROJECT_DIR, command), echo=True, pty=True)

@task
def server():
    """run the dev server"""
    local('python manage.py runserver 0:8000')

@task
def celery():
    """start the celery server"""
    local('python manage.py celeryd -E -B --concurrency=1')
   
@task
def translations():
    """make and compile translations

      .. note:: restricted usage
      """
    make_translations()
    compile_translations()

@task
def make_translations():
    """make translations

      .. note:: restricted usage
      """
    local('python manage.py makemessages --all --no-wrap --no-location')

@task
def compile_translations():
    """compile translations
      .. note:: restricted usage
      """
    local('python manage.py compilemessages')


@task
def docs_presentation():
    run("hovercraft docs/presentation/overview.rst docs/_build/pres_over/", echo=True, pty=True)
    run("hovercraft docs/presentation/ia.rst docs/_build/pres_ia/", echo=True, pty=True)


@task
def docs():
    run("cd docs && make html", echo=True, pty=True)
