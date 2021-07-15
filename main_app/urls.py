from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('dogs/', views.dogs_index, name='index'),
  path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
  path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
  path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
  path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
  path('dogs/<int:dog_id>/add_walking/', views.add_walking, name='add_walking'),
  path('dogs/<int:dog_id>/assoc_treat/<int:treat_id>/', views.assoc_treat, name='assoc_treat'),
  path('dogs/<int:dog_id>/unassoc_treat/<int:treat_id>/', views.unassoc_treat, name='unassoc_treat'),
  path('treats/', views.TreatList.as_view(), name='treats_index'),
  path('treats/<int:pk>/', views.TreatDetail.as_view(), name='treats_detail'),
  path('treats/create/', views.TreatCreate.as_view(), name='treats_create'),
  path('treats/<int:pk>/update/', views.TreatUpdate.as_view(), name='treats_update'),
  path('treats/<int:pk>/delete/', views.TreatDelete.as_view(), name='treats_delete'),
]