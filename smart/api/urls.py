from django.urls import path
from . import views

urlpatterns=[
    path('api/',views.getData),
    path('add/',views.addItem),
    path('detail/<str:pk>/', views.getDetail),
    path('update/<str:pk>/', views.update),
    path('delete/<str:pk>/', views.delete),
]