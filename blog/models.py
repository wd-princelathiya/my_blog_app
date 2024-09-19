from django.db import models
from django.contrib.auth.models import User  #all the user names 
from django.db.models import CASCADE


# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=CASCADE)  #user ID 
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title