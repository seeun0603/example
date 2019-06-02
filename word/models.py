from django.db import models

# Create your models here.
class Upload(models.Model):
    word = models.TextField(max_length =20) 
    mean = models.TextField()
    def __str__(self):
        return self.word