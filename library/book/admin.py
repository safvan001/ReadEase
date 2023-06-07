from django.contrib import admin

from book.models import book
from book.models import student
#to register table name in admin
admin.site.register(book)
admin.site.register(student)