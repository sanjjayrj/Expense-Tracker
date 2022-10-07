from django.contrib import admin
# Register your models here.
from django.contrib.sessions.models import Session

from .models import Addexpense_info
from .models import UserProfile

class Addexpense_infoAdmin(admin.ModelAdmin):
    list_display=("user","quantity","Date","Category","add_expense")
admin.site.register(Addexpense_info,Addexpense_infoAdmin)
admin.site.register(Session)
admin.site.register(UserProfile)
