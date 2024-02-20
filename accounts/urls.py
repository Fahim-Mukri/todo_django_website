from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup

app_name = 'accounts'

urlpatterns = [
    # /accounts/login/
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # /accounts/signup/
    path('signup/', signup, name='signup'),
    
    # /accounts/logout/
    path('logout/', LogoutView.as_view(), name='logout'),
]
