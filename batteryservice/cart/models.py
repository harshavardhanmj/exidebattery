from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from product.models import ProductDetail

# Create your models here.
class UserCart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	cartitem = models.ForeignKey(ProductDetail)
	number = models.IntegerField(default=0)

	def __str__(self):
		return self.cartitem.name



def uc_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.number = instance.number + 1

pre_save.connect(uc_pre_save_receiver, sender=UserCart)