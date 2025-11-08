from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('predict/', views.predict_metal_view, name='predict'),  # New endpoint
]