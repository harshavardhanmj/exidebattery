from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator

# Create your models here.
class ProductDetail(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(max_length=300,blank=True,null=True)
	types = models.CharField(max_length=70,blank=True,null=True)
	slug = models.SlugField(null=True,blank=True)

	def __str__(self):
		return self.name

	@property
	def title(self):
		return self.name


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	#instance.category = instance.category.capitalize()
	if not instance.slug:
	 	instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=ProductDetail)