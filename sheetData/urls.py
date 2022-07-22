from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListView.as_view(), name='homepage'),
    path('order-upload/', views.OrderUpload.as_view(), name='order-upload')
]