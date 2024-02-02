from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length = 250)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.name
  
    
class Task(models.Model):
    category = models.ForeignKey(category,on_delete = models.CASCADE)
    description = models.CharField(max_length = 250)
    date = models.DateField(default = date.today,blank = True,null = True)
    time = models.TimeField(null = True,blank = True,)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,null = True,blank = True)


    

