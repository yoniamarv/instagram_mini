from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_auth, name='login'),
  path('logout/', views.logout_auth, name='logout'),
  path('list_users/', views.list_users, name='list_users'),
  path('profile/<int:profile_id>/', views.profile, name='profile'),
  path('home/', views.home, name='home'),
]