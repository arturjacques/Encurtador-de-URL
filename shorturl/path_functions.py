import shorturl.views as short
from django.urls import path
from pages.views import home_view

urlpatterns = path('', home_view, name='home'),path('9', short.view_9),path('a', short.view_a),path('b', short.view_b),path('c', short.view_c),