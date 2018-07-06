# coding: UTF-8
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))

FLASK_PORT = int(os.environ.get('FLASK_PORT'))

INCOMING_WEBHOOK_URL = os.environ.get('INCOMING_WEBHOOK_URL')
