from django.contrib import admin

from models import Route, Incoming


@admin.register(Route)
class RouterAdmin(admin.ModelAdmin):
    pass


@admin.register(Incoming)
class IncomingAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'route', 'date_start', 'date_end')


