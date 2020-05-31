from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:animal_id>/', views.detail_animal_view, name="detail_animal"),
	path('edit/<int:animal_id>/', views.edit_animal_view, name="edit_animal"),
	path('new/', views.new_animal_view, name="new_animal"),
]
