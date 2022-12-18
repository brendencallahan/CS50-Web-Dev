from django.contrib.auth.models import AbstractUser
from django.db import models


LISTING_CATEGORIES = (
    ("BOOKS", "Books"),
    ("BUSINESS", "Business & Industrial"),
    ("CLOTHES", "Clothing, Shoes & Accessories"),
    ("COLLECTIBLES", "Collectibles"),
    ("ELECTRONICS", "Consumer Electronics"),
    ("CRAFTS", "Crafts"),
    ("DOLLS", "Dolls & Bears"),
    ("HOME", "Home & Garden"),
    ("MOTORS", "Motors"),
    ("PETS", "Pet Supplies"),
    ("SPORTS GOODS", "Sporting Goods"),
    ("SPORTS MEM", "Sports Mem, Cards & Fan Shop"),
    ("TOYS", "Toys & Hobbies"),
    ("ANTIQUES", "Antiques"),
    ("COMPUTERS", "Computers/Tablets & Networking")
)

class User(AbstractUser):
    pass

class Bid(models.Model):
    bid_amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

class Listing(models.Model):
    picture = models.URLField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1200)
    category = models.CharField(max_length=50, choices=LISTING_CATEGORIES, default=None)
    bids = models.ForeignKey(Bid, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="user_listings")