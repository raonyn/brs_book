from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brsbook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=False)
    category = models.TextField()
    content = models.TextField()
    cost = models.IntegerField()
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return self.title