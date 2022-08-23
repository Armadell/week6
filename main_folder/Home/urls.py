from importlib.resources import path
from django.urls import path
from django.contrib import admin
from main_folder.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('',views.home,name='main_home'),
    path('register/',views.register,name='Home'),
    path('login/',views.login_form,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('library/',views.index,name='library'),
    path('upload/',views.upload,name='upload'),
    path('update/<int:book_id>',views.update_book),
    path('delete/<int:book_id',views.delete_book,name='delete'),
]
