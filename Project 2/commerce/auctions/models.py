from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1200)
    bids = models.ForeignKey(Bids, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category, on_delete=models.PROTECT)
    picture = models.URLField(max_length=200)


class Bids(models.Model):
    bid = models.IntegerField()

class Comments(models.Model):
    pass

class Category(models.Model):
    pass