from django.db import models
from django.conf import settings

# Create your models here.
class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    beans = models.CharField(max_length=80)
    roast = models.CharField(max_length=30)
    grinder = models.CharField(max_length=80)
    click = models.CharField(max_length=10)
    blooming = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    ratio = models.CharField(max_length=10)
    method = models.CharField(max_length=30)
    descripton = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)