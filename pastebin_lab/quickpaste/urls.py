from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_main_page, name='main'),
    path('contacts/', views.show_contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('save_post/<slug:user_slug>/', views.save_post, name='save_post'),
    path('post/<slug:user_slug>/', views.show_post, name='show_post')
]