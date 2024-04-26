#Still a work in progress
from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    verified_buyer = models.BooleanField(default=False)
    review_date = models.DateField()
    location = models.CharField(max_length=255, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    product = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    scrape_date = models.DateField()

    def __str__(self):
        return self.title
