from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Product, Order


class ProductList(ListView):
    model = Product
    template_name = 'index.html'


class ProductDetail(DetailView):
    model = Product
    template_name = 'detail.html'

class CreateProduct(CreateView):
    model = Product
    template_name = 'form.html'
    fields = "__all__"
    success_url = reverse_lazy('main')


class CreateOrder(CreateView):
    model = Order
    template_name = 'form.html'
    fields = "__all__"
    success_url = reverse_lazy('main')

class UpdateOrder(UpdateView):
    model = Order
    template_name = "form.html"
    fields = "__all__"
    success_url = reverse_lazy('main')
