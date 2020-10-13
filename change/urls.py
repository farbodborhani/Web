
from django.urls import path

from . import views
app_name='change'

urlpatterns = [
    path('',views.change_home,name='change'),
]
