from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reminder, ReminderAdmin)