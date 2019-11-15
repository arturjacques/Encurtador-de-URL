import shorturl.views as short
from django.urls import path
from pages.views import home_view

urlpatterns = path('.', home_view, name='home'),path('1', short.view_1),path('2', short.view_2),path('3', short.view_3),