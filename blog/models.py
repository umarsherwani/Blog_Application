from django.db import models

from datetime import datetime

from django.conf import settings
class Postblog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author