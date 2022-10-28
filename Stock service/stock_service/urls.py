from django.urls import path
from . import views

urlpatterns = [
    path('', views.productApi),
    path('<int:id>', views.productApi),
]
