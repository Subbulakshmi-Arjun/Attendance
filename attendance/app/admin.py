from django.contrib import admin
from .models import Attendance

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display=["Staffid","Date","punch_in_time","punch_out_time"]
    list_filter=["Date",]
    search_fields=["Staffid",]
admin.site.register(Attendance,AttendanceAdmin)

