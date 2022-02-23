from django.contrib import admin

from .models import Leave


class LeaveAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'leavestart', 'leaveend',
                    'reason', 'availibilty', 'approval','submitted')
    list_filter = ('submitted',)



admin.site.register(Leave, LeaveAdmin)
