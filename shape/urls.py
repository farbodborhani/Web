
from django.urls import path
from . import views

app_name='shape'
urlpatterns = [
    path('Page/',views.shape_page,name='shape_page'),
]
