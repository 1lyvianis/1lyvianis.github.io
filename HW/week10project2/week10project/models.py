from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    textarea = models.CharField(max_length=200, default='default string')
