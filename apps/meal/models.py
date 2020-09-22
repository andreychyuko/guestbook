from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=60, verbose_name='Твое любимое блюдо?')
    
    
    def __str__(self):
        return self.title


