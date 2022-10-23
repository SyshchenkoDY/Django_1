from django.db import models
from datetime import datetime
from os import listdir


def time_now():
    return datetime.now()


def list_dirs():
    return listdir()
