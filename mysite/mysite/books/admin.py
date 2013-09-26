from django.contrib import admin
from mysite.books.models import Author, Publisher

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

admin.site.register(Publisher, PublisherAdmin)
