from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Order(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_placed = models.DateTimeField(default=timezone.now)
    customer = models.CharField(max_length=100)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)
    tags = TaggableManager()

    def __str__(self):               # used to tell what we want to see in the query set
        return self.title
    
    def get_absolute_url(self):
        return reverse("order-detail", kwargs={"pk": self.pk})
    
    

