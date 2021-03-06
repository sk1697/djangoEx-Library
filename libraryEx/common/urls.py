from django.urls import path
from django.contrib.auth import views as auth_views
# from . import views
from .views import common_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', common_views.signup, name='signup'),
    path('profile/password/', common_views.password_edit_view, name='password_edit'),
]