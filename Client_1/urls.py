"""
Client_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [

    path("i18n/", include("django.conf.urls.i18n")), #https://docs.djangoproject.com/en/4.2/topics/i18n/translation/#django.views.i18n.set_language ,
]


urlpatterns += i18n_patterns(
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', include('accounts.urls'))
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]