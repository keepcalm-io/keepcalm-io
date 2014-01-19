from django.contrib import admin
from .models import Signal


class SignalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'max_retries', 'expires_on')
    list_filter = ('user__username',)
    search_fields = ['name']

admin.site.register(Signal, SignalAdmin)
