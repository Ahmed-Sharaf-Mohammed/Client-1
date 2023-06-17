from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    # Add more URL patterns as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
