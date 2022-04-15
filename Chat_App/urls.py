from django.urls import path
from .views import index
urlpatterns = [
    path('', index, name="index"),
    path('login/', index, name='login'),
    path('sign-up/', index, name='register'),
    path('logout/', index, name='logout'),
    path('room/<str:room>/', index, name='room'),
]
