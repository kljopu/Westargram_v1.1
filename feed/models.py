from django.db import models
from user.models import Account

class Feed(models.Model):
    user        = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='feed_user')
    content     = models.CharField(max_length = 300, verbose_name='content')
    like        = models.IntegerField(verbose_name='like', null= True)
    comment     = models.ManyToManyField('')
