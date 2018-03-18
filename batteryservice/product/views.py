from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View
from .models import ProductDetail
from django.shortcuts import render, get_object_or_404, redirect
from cart.models import UserCart
from .forms import ProductDetailCrateForm

class ProductListView(ListView):
    template_name = "home.html"
    queryset = ProductDetail.objects.all()

class ProductDetailView(DetailView):
    template_name = "productdetail.html"
    queryset = ProductDetail.objects.all()


class ProductCreateView(CreateView):
	form_class = ProductDetailCrateForm
	template_name = 'form.html'
	success_url = '/'