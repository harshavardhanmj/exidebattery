from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from .models import UserCart
from product.models import ProductDetail

class CartListView(ListView):
    template_name = "cart.html"

    def get_queryset(self):
    	return UserCart.objects.filter(user=self.request.user)


class CartClass(View):
	def post(self, request, *args, **kwargs):
		CartObj = request.POST.get("username")
		product_to_cart = ProductDetail.objects.get(name__iexact=CartObj)
		wholecart = UserCart.objects.filter(user=self.request.user, cartitem=product_to_cart)
		print(wholecart)
		if not wholecart.exists():
			obj = UserCart.objects.create(
						user = self.request.user,
						cartitem = product_to_cart
					)
			return redirect(f"/{product_to_cart.slug}/")
		else:
			incrementitem = UserCart.objects.get(user=self.request.user, cartitem=product_to_cart)
			incrementitem.save()
		return redirect(f"/{product_to_cart.slug}/")



# class ProductDetailView(DetailView):
#     template_name = "productdetail.html"
#     queryset = ProductDetail.objects.all()


# class ProductCreateView(CreateView):
# 	form_class = ProductDetailCrateForm
# 	template_name = 'form.html'
# 	success_url = '/'