"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from gear import views
from gear.routes import api_router

urlpatterns = [
    url(r'^gear/', include('gear.urls', namespace="gear")),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^passwordreset/', include('password_reset.urls')),

        #api
    url(r'^api/v1/', include(api_router.urls)),
]
