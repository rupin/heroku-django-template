from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
