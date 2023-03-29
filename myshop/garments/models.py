from django.db import models


class FormalShirt(models.Model):
    name=models.CharField(max_length=100)
    photo=models.FileField(blank=True)
    desc=models.TextField(max_length=500,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' %self.name
