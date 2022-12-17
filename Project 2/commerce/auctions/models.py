from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    pass

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass
