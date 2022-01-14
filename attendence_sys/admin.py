from django.contrib import admin

from .models import *

# Register your models here.
admin.site.site_header = 'SAMS Administration'
admin.site.site_title = 'SAMS Administration'
admin.site.index_title = 'Welcome to Your Desk :)'
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Attendence)