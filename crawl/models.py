from django.db import models

class Moviedata(models.Model):
    title = models.CharField(max_length=200, verbose_name = '검색어')
    review = models.CharField(max_length=500)
    objects = models.Manager()
    
    def __str__(self):
        return self.title