from django.urls import path

from . import views

app_name = 'loginapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('successlogin/', views.successlogin, name='successlogin'),
    path('signup/', views.UserFormView.as_view(), name='signup'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
]
