from django.urls import path
from . import views

urlpatterns = [
	path('', views.nutrition_homepage, name='nutrition_homepage'),
	path('day/', views.day, name='day'),
	path('week/', views.week, name='week'),
	path('scrape/', views.scrape, name='scrape'),
	path('manual/', views.manual, name='manual'),
	path('core/edit/<int:pk>', views.core_edit, name='core_edit'),
	path('item/add/', views.add_item, name='add_item'),
	path('item/edit/<int:pk>', views.edit_item, name='edit_item'),
	path('recipe/add', views.add_recipe, name='add_recipe'),
	path('recipe/edit/<int:pk>', views.edit_recipe, name='edit_recipe'),
	path('menu/', views.menu, name='menu'),
	path('error/', views.error, name='error'),
]