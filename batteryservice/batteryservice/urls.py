"""batteryservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from product.views import ProductListView, ProductDetailView, ProductCreateView
from cart.views import CartListView, CartClass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ProductListView.as_view()),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^create/$', ProductCreateView.as_view(), name='create'),
    url(r'^cart/$', CartListView.as_view(), name='cartlist'),
    url(r'^buyitem/$', CartClass.as_view(), name='BuyItem'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view()),
]
