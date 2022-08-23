from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.admin import AdminSite
class MyAdminSite(admin.AdminSite):
    site_header = ' administration'
    site_title  = 'My Project Title Administration'
    index_title = 'My Project Title Administration'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)


# Register your models here.
