from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    type = models.IntegerField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    colour = models.CharField(max_length=10)
    reportable = models.BooleanField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reportable = models.BooleanField()
    account = models.ForeignKey(Account)
    category = models.ForeignKey(Category, blank=True, null=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.description