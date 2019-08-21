from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
     title = models.CharField(max_length=200)
     slug = models.CharField(max_length=200)
     body = models.TextField()
     pub_date = models.DateTimeField(default=timezone.now)

     class Meta:
         ordering = ('-pub_date',)
    
     def __str__(self):
         return self.title

class upload_file(models.Model):
     user_id = models.CharField(max_length=200)
     file_name = models.CharField(max_length=200)
     file_path = models.CharField(max_length=200)
     upload_time = models.DateTimeField(default=timezone.now)
     class Meta:
         ordering = ('-upload_time',)
     def __return__(self):
         return self.user_id
