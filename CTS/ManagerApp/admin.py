from django.contrib import admin
from .models import Manager
# Register your models here.
@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['ManagerId','ManagerName','ManagerPassword']
    

