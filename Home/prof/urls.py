

from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.HOME, name = 'home'),
    path('login/', views.LOGIN, name = 'login'),
    path('registration/', views.REGISTRATION, name = 'registration'),
    path('logout/', views.LOGOUT, name = 'logout'),
    path('user-profile/', views.USERPROFILE, name = 'UserProfile'),
]
