from django.contrib import admin
from .models import Rental


class RentalAdmin(admin.ModelAdmin):
    search_fields = ['who']
    list_display = ['who', 'what']

admin.site.register(Rental, RentalAdmin)
