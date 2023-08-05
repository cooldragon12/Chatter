from django.urls import path, include
from .views import RegisterView
from . import views


urlpatterns = [
    path('login/', views.AuthenticationView.as_view({'post':'_login'}), name = 'auth_login'),
    path('logout/', views.AuthenticationView.as_view({'post':'_logout'}), name = 'auth_logout'),
    path('session/', views.SessionView.as_view(), name = 'auth_session'),
    path('me/', views.MeView.as_view(), name = 'auth_me'),
    path('register/', RegisterView.as_view(), name = 'auth_register'),
]