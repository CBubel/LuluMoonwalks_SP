from django.db import models


# Defining admin and user required credentials and their arguments.

class Admin(models.Model):
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=20)


class User(models.Model):
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=20)
