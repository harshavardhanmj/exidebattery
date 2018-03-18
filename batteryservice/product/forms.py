from django import forms

from .models import ProductDetail

class ProductDetailCrateForm(forms.ModelForm):
	class Meta:
		model = ProductDetail
		fields = [
			'name',
			'description',
			'types'
		]