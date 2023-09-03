from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='registerpage'),
    path('login/', views.login, name='loginpage'),
    path('files/<id>', views.files),
    path('approve/<id>', views.approve),
    path('reject/<id>', views.reject)
]