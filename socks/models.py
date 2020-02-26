from django.db import models

# Create your models here.
class Sock(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True)
    title = models.TextField(max_length=200, default = None)
    isLeft = models.BooleanField(default=True)
    isNew = models.BooleanField(default=False)
    isShort = models.BooleanField(default=True)
    isHot = models.BooleanField(default=False)
    price = models.IntegerField(default=20000)

    def __str__(self):
        return self.name