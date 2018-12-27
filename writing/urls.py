from django.urls import path
from . import views

urlpatterns = [
	path('', views.site_homepage, name='site_homepage'),
	path('writing/', views.writing_home, name='writing_home'),
]