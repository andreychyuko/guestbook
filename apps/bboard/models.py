from django.db import models

class Advert(models.Model):
    title = models.CharField(max_length=60, db_index=True, verbose_name='Товар')
    text = models.TextField(verbose_name='Описание')
    phone = models.CharField(max_length=17, verbose_name='Телефон')

    is_active = models.BooleanField(default=True, verbose_name='Выводить в списке?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title

