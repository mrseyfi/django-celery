from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
	path('', views.home, name='home'),
	path('<int:num_id>/', views.nums, name='nums'),
]