from django.urls import path, include
from users import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('login', views.login_oauth, name='login'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('', views.index),
]