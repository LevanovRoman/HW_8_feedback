from django import forms
from .models import *

class FeedbackForm(forms.Form):
    CHOICES = [('1', '*'), ('2', '**'), ('3', '***'),
               ('4', '****'), ('5', '*****'), ]
    name = forms.CharField(max_length=10, label='Ник')
    email = forms.EmailField(label='Почта')
    stars = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES,
                              label='Количество звёзд для приложения ')
    description = forms.CharField(widget=forms.Textarea,
                            label='Описание вашего опыта использования приложения')


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=10, label='Ник')
    rating = forms.IntegerField(max_value=100, min_value=0, label='Ваш рейтинг книги (от нуля до ста)')
    review = forms.CharField(widget=forms.Textarea, label='Рецензия на книгу')
    spoiler = forms.BooleanField(required=False, label='Содержит ли ваша рецензия спойлеры?')


class SearchForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'


