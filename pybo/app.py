"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from os import environ
from pybo import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
