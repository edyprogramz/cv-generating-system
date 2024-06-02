from django.urls import path
from user.views import login_view, signup_view, logout_view

app_name = 'user'

urlpatterns = [
    path('register/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]