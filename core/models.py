from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

class Item(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='items')
    what = models.CharField(max_length=150)
    where = models.CharField(max_length=150)
    passed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def remove_url(self):
        return reverse('remove',kwargs={'id':self.id})
    def edit_url(self):
        return reverse('edit',kwargs={'id':self.id})
    class Meta:
        ordering = ('-created_date',)
    def __str__(self):
        return f'{self.owner}- {self.id}'
    
    