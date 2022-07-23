
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class products(models.Model):
    adder=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    brief=models.TextField()
    image=models.ImageField()
    price=models.IntegerField(default=0)
    timeadd=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-timeadd']
    def __str__(self):
        return self.name

class comments(models.Model):
    product=models.ForeignKey(products, on_delete=models.CASCADE,related_name='comments')
    adder=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.CharField(max_length=5000)
    timeadd=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['timeadd']

    def __str__(self):
       return self.text


