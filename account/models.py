from django.db import models

# Create your models here.
class ScRegisteration(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
