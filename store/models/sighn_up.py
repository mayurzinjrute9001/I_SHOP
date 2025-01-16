from django.db import models

class Sighn_up(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.name
