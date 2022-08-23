from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
 

class HomeConfig(AdminConfig):
    default_site = 'django.db.models.BigAutoField'
    name = 'Home'
