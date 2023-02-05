#!/home/a/an/antoniomolteni/calttc_django/venv/bin/python
import os
import sys

sys.path.insert(0, os.path.expanduser('~/calttc_django'))
from flup.server.fcgi import WSGIServer

from calttc_project import wsgi
if __name__ == '__main__':
    WSGIServer(wsgi.application).run()