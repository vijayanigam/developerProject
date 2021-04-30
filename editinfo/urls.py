from django.urls import path
from . import views
app_name = 'editinfo'
urlpatterns = [
    path('', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('editdata/', views.editdata, name='editdata'),
    path('weightage/', views.get_weightage, name='weightage'),
    path('data/', views.show_data, name='data')


]