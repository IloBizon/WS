from django.urls import path
from .views import ProductDetail, ProductList, CreateOrder, UpdateOrder

urlpatterns = [
path('main', ProductList.as_view(), name='main'),
path('detail/<int:pk>', ProductDetail.as_view(), name='detail'),
path('create', CreateOrder.as_view(), name='create'),
path('update/<int:pk>', UpdateOrder.as_view(), name='update')
]