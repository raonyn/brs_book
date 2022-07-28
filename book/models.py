from django.db import models
from django.contrib.auth.models import User
from book.models import *

# Create your models here.
'''
class Hobook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title
        '''