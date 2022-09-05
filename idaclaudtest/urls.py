from django.contrib import admin
from django.urls import path
from mortgagecalc import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('api/offer/', views.BanksAPIWiew.as_view()),
    path('api/offer/<int:pk>/', views.BanksAPIWiew.as_view())
]
