from celery import shared_task
from time import sleep

from django.contrib.auth.models import User

from .models import *
from .serializers import *

