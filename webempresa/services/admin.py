from django.contrib import admin
from .models import Service
# Register your models here.
# para que este disponible desde el admin
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Service, ServiceAdmin)