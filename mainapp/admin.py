from django.contrib import admin
from .models import *

class PersonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'patronymic', 'lastname', 'city')


admin.site.register(Persons, PersonsAdmin)

