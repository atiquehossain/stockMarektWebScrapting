# myproject/urls.py
from django.contrib import admin
from django.urls import path, include


from financeApp.views import  apple, amazon, google, microsoft, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apple/', apple, name='apple'),
    path('amazon/', amazon, name='amazon'),
    path('google/', google, name='google'),
    path('microsoft/', microsoft, name='microsoft'),
    path('', home),  # Handle the root URL
]
