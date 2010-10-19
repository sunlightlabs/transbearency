#!/usr/bin/env python
from flup.server.fcgi import WSGIServer
from transbearency import app

socket_path = '/path/to/fcgi.sock'
WSGIServer(app, bindAddress=socket_path).run()