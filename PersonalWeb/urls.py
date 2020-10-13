
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('work/',include('work.urls',namespace='work')),
    path('shape/',include('shape.urls',namespace='shape')),
    path('change/',include('change.urls',namespace='change')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
