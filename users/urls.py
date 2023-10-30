from django.urls import path, include
from users import views

app_name = "users"

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("login", views.login_oauth, name="login"),
    path('logout/', views.logout, name='logout'),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("", views.homepage, name="homepage"),
]