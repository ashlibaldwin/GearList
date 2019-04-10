from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from gear import views

urlpatterns = [
    url(r'^gear/', include('gear.urls', namespace="gear")),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^passwordreset/', include('password_reset.urls')),
]
