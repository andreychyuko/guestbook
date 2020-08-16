from django import forms
from .models import News
import re # импорт регулярных выражений 
from django.core.exceptions import ValidationError # импорт валидатора обработки ошибок


class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields = ['title', 'content', 'is_published', 'category']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    #валидатор для названия что бы не начиналось с цифры
    def clean_title(self):
        # получаем очищенные данные славоря по ключу title
         title = self.cleaned_data['title']
          # условие не начинается ли эта строка с цифры
         if re.match(r'\d', title):
             # если начинается то выходит исключение 
          raise ValidationError('Название не должно начинаться с цифры')
            # если мы прошли данную проверку тогда мы возвращаем title
         return title