from django.db import models

class Persons(models.Model):
    firstname = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия')
    city = models.CharField(max_length=30, verbose_name='Город')

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
        ordering = ['id']

