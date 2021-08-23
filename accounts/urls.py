from django.urls import path
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from accounts.auth import CustomAuthToken

urlpatterns = [
    # -----------------Signup--------------------
    path('', RegisterView.as_view(), name='auth_register'),
    # path('login/', obtain_auth_token),
    path('login/', CustomAuthToken.as_view()),

]
