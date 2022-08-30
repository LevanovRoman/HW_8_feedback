from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, FormView, ListView
from .forms import *

menu = [
    {'title': 'Главная страница', 'url_name': 'base'},
    {'title': 'Отзыв о мобильном приложении', 'url_name': 'feedback'},
    {'title': 'Рецензия на книгу', 'url_name': 'review'},
    {'title': 'Поиск информации о человеке', 'url_name': 'search'},
]
class FeedbackApp(FormView):
    template_name = 'mainapp/feedback.html'
    form_class = FeedbackForm
    initial = {'name': " roman", 'description':'Всё понравилось'}
    # success_url = reverse_lazy('try_succ')
    extra_context = {'menu': menu, 'title': 'Отзыв о мобильном приложении'}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            stars = form.cleaned_data.get('stars')
            description = form.cleaned_data.get('description')
            context = {'name': name, 'email': email, 'stars': stars,
                       'description': description, 'title': 'Отзыв о мобильном приложении'}
            return render(request, 'mainapp/try_succ.html', context=context)
        return self.form_invalid(form)


class HomePage(TemplateView):
    template_name = 'mainapp/base.html'
    extra_context = {'menu': menu, 'title':'Главная страница'}

class BookReview(FormView):
    template_name = 'mainapp/review.html'
    form_class = ReviewForm
    extra_context = {'menu': menu, 'title':'Рецензия на книгу'}
    initial = {'name': " roman", 'rating': '88', 'review': 'Прекрасная книга!'}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            name = form.cleaned_data.get('name')
            rating = form.cleaned_data.get('rating')
            review = form.cleaned_data.get('review')
            spoiler = form.cleaned_data.get('spoiler')
            if spoiler:
                text = "Отзыв содержит спойлер"
            else:
                text = "Отзыв не содержит спойлер"
            context = {'name': name, 'rating': rating, 'review': review,
                       'text': text, 'title':'Рецензия на книгу'}
            return render(request, 'mainapp/review_succ.html', context=context)
        return self.form_invalid(form)


class SearchPerson(FormView):
    template_name = 'mainapp/search.html'
    extra_context = {'menu': menu, 'title':'Поиск информации о человеке'}
    form_class = SearchForm
    initial = {'firstname': " Роман", 'patronymic': 'Геннадьевич',
               'lastname': 'Леванов', 'city': 'Краснодар'}
    success_url = reverse_lazy('result')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            patronymic = form.cleaned_data.get('patronymic')
            lastname = form.cleaned_data.get('lastname')
            city = form.cleaned_data.get('city')
            context = {'firstname': firstname, 'patronymic': patronymic, 'lastname': lastname,
                       'city': city, 'title': 'Поиск информации о человеке'}
            return self.form_valid(form)
        return self.form_invalid(form)


class SearchResult(ListView):
    paginate_by = 3
    model = Persons
    template_name = 'mainapp/search_result.html'
    extra_context = {'menu': menu, 'title': 'Поиск информации о человеке'}
    context_object_name = 'posts'
