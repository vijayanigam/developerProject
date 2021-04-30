from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'addinfo'
urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.home, name='home'),
    # url(r'^(?P<pk>[0-9]+)$', views.pagenotfound)
    # [a-z0-9])[a-z0-9!@#$%&*.]{7,}
    url(r'^(?P<pk>[a-z0-9!@#$%&*.]+)$', views.pagenotfound)
]
