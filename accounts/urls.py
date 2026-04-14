from django.urls import path, include
from . import views
 
urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='sign_up'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
