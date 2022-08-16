from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, re_path
from . import views
app_name = "users"
urlpatterns = [
	#Login Page
	path('login/', LoginView.as_view(template_name='users/login.html'),name="login"),
	re_path(r'^logout/$', views.logout_view, name='logout'),
	re_path(r'^register/$', views.register, name='register'),
]
