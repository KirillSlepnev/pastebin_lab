from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('contacts/', views.show_contacts, name='contacts'),
    path('post/<slug:user_slug>/', views.ShowPost.as_view(), name='show_post'),
]
