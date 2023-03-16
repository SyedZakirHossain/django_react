from django.db import models


class Plan(models.Model):
    items = models.CharField(max_length=100)
   
    def __str__(self):
          return self.items 
