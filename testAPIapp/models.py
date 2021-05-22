# basic_api/models.py
from django.db import models

#list
Grade = [
    ('excellent', 1),
    ('average', 0),
    ('bad', -1)
]

# DataFlair
class DRFPost(models.Model):
    name = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    uploaded = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = Grade, default = 'average', max_length = 50)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name




class Product(models.Model):
    title = models.CharField(max_length = 100)
    producer = models.CharField(max_length = 100)
    add_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="pictures/" ,blank = True)
   

    class Meta:
        ordering = ['add_date']
    def __str__(self):
        return self.title


