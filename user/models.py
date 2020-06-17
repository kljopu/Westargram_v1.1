from django.db import models
import json

class Account(models.Model):
    email = models.CharField(max_length = 150)
    password = models.CharField(max_length=100000)
    created_at = models.DateField(auto_now_add=True)


    class Meta:
        db_table = "Accounts"
