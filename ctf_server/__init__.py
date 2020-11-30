from flask import Flask, g
app = Flask(__name__)

# Read setting from a config module
app.config.from_object('ctf_server.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/config/
app.config.from_envvar('CTF_SERVER_SETTINGS', silent=True)

import ctf_server.views
import ctf_server.db