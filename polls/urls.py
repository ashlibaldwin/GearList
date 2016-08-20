from django.conf.urls import url

from . import views

app_name = 'polls'

app_name = 'polls'
urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
    url(r'^list/', views.list, name='list'),
    url(r'^list_detail/(?P<pk>\d+)/$', views.list_detail, name='list_detail'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_item, name="delete_item"),
    url(r'^delete_list/(?P<pk>\d+)/$', views.delete_list, name="delete_list"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),



]