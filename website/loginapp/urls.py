from django.urls import path

from . import views

app_name = 'loginapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('signup/', views.UserFormView.as_view(), name='signup'),
]
