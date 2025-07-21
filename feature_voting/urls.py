from django.urls import path
from . import views

urlpatterns = [
    path('', views.feature_list, name='feature_list'),
    path('new/', views.feature_create, name='feature_create'),
    path('vote/<int:feature_id>/', views.vote_feature, name='vote_feature'),
]