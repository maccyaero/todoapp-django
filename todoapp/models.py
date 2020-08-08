from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ListItem(models.Model):
    PRIORITY_LEVELS=[
          ('N','No Priority'),
          ('L', 'Low'),
          ('M','Medium'),
          ('H','High'),
    ]

    name = models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length =1, choices=PRIORITY_LEVELS,default = 'N')
    list_id = models.ForeignKey('List',on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name    