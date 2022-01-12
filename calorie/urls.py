from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

from .views import HomePageView,LoginPage,LogOutPage,select_food,add_food,RegisterPage,ProfilePage,update_food,delete_food

urlpatterns = [
	path('', HomePageView,name='home'),
	path('select_food/',select_food,name='select_food'),
	path('add_food/',add_food,name='add_food'),
	path('update_food/<str:pk>/',update_food,name='update_food'),
	path('delete_food/<str:pk>/',delete_food,name='delete_food'),
	path('update_profile/<int:id>',views.update_profile, name='update_profile'),
	path('profile/',ProfilePage,name='profile'),
	path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]