from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('place/<str:name>/', views.detail, name="detail")
]