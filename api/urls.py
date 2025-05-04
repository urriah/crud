from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('builds/', views.getBuilds),
    path('builds/create/', views.createBuild),
    path('builds/<str:pk>/update/', views.updateBuild),
    path('builds/<str:pk>/delete/', views.deleteBuild),
    path('builds/<str:pk>/', views.getBuild),
]
