from django.contrib import admin
from django.urls import path, include
from webapp.views import home_view,user_create,user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts', include('webapp.urls')),
    path('accounts/home', home_view, name='home'),
    path('accounts/user_create', user_create, name='user_create'),
    path('accounts/user_list', user_list, name='user_list')
]
