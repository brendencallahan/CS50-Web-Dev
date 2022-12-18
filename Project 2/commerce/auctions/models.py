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
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)


class Bids(models.Model):
    bid = models.IntegerField()

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

class Category(models.Model):
    # Add a list to choose from
    pass