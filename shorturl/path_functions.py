import shorturl.views as short
from django.urls import path
from pages.views import home_view

urlpatterns = path('.', home_view, name='home'),path('1', short.view_1),path('2', short.view_2),path('3', short.view_3),path('4', short.view_4),path('5', short.view_5),path('6', short.view_6),path('7', short.view_7),path('8', short.view_8),path('9', short.view_9),path('a', short.view_a),path('b', short.view_b),