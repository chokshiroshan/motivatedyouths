from django.db import models
from django.utils import timezone
from django.urls import reverse

class Article(models.Model):
    author = models.ForeignKey(
    'auth.User',
    on_delete = models.CASCADE,
    )
    background = models.ImageField(upload_to='media',blank=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='media',blank=True)
    text = models.TextField()
    secondtitle = models.CharField(max_length=100,blank=True)
    image2 = models.ImageField(upload_to='media',blank=True)
    secondtext = models.TextField(blank=True)
    thirdtitle = models.CharField(max_length=100,blank=True)
    image3 = models.ImageField(upload_to='media',blank=True)
    thirdtext = models.TextField(blank=True)
    date_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("home")
