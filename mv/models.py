from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=83, primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    
    def __str__(self):
        return(self.title)