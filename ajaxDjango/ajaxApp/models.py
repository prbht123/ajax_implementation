from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    address= models.CharField(max_length=100)
    contact =  models.CharField(max_length=100)
    def __str__(self):
        return 'Profile for user {}'.format(self.user)


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return 'Profile for user {}'.format(self.name)

