from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'authenticate'
urlpatterns = [
    # path('index/', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='add/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='add/logout.html'), name='logout'),
    # path('register/', user_views.register, name='register'),
    path('notloggedin/', views.notloggedin, name='not_loggedin')
    # path('done/',views.login,app_name='done'),
    # path('login/', views.login, app_name='done')

]