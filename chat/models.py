from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    # add user profile picture later

    def __str__(self):
        return f"{self.id} with username: {self.username} and password: {self.password}"