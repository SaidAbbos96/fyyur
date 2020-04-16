import os


SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = False
# TODO IMPLEMENT DATABASE URL = done.
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1111@localhost:5432/todoapp'

#MODIFICATIONS status
SQLALCHEMY_TRACK_MODIFICATIONS = False
