from django.db import models


class Dados(models.Model):
    pcName = models.CharField(max_length=50)
    ip = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    htmlURL = models.CharField(max_length=200)
    isLocked = models.BooleanField()

    def __str__(self):
        return self.pcName