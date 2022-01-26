from django.contrib import admin
from .models import Tracking
# Register your models here.
@admin.register(Tracking)
class TrackingAdmin(admin.ModelAdmin):
    list_display = ['TrackingId','CarID','CurrentLocation']
    